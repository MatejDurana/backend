from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import base64
import os
import numpy as np
import cv2
import subprocess
import psutil


app = FastAPI()
output_path = "images/output.jpg"

process = None
params = ''


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ImageRequest(BaseModel):
    id: str
    contentData: str
    styleData: str
    params: str


@app.post("/startProcess")
async def start_process(data: ImageRequest):
    global process
    global params
    saveImages(data.contentData, data.styleData)

    selected_script = None

    if (data.id == "anaoas"):
        selected_script = 'models/crowsonkb/script.sh'
        params = data.params

    elif (data.id == "msg-net-istucnn"):
        selected_script = 'models/zhanghang/script.sh'

    elif (data.id == "istucnn-2"):
        selected_script = 'models/gordicaleksa/script.sh'
        params = data.params

    elif (data.id == "nnst"):
        selected_script = 'models/nkolkin/script.sh'
        params = data.params
    else:
        return {"error": "Neznámy model."}

    if process is not None:
        return {"error": "Proces už beží."}

    delete_image(output_path)

    process = subprocess.Popen(['sh', selected_script, params])

    params = ''

    return {"message": f"Štartujem model {data.id}."}


@app.post("/checkProcess")
def check_process():
    global process

    if process is None:
        return {"message": "Žiadny proces nebeží.", "isRunning": False}

    if os.path.exists(output_path):
        image = cv2.imread(output_path)
        _, buffer = cv2.imencode('.jpg', image)
        base64_image = base64.b64encode(buffer).decode('utf-8')
        base64_image = "data:image/jpeg;base64," + base64_image
    else:
        return {"message": "Výsledný obrázok sa nenašiel.", "isRunning": True, "output_image": ""}

    if process.poll() is not None:
        process = None
        return {"message": "Proces dokončený.", "isRunning": False, "output_image": base64_image}

    return {"message": "Proces beží.", "isRunning": True, "output_image": base64_image}


@app.post("/closeProcess")
async def close_process():
    global process
    if process is not None:
        process_pid = process.pid
        kill_process_and_children(process_pid)
        process = None
        return {"message": "Proces ukončený"}
    else:
        return {"message": "Žiadny proces aktuálne nie je spustený"}


def kill_process_and_children(pid):
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    parent.kill()


def saveImages(content, style):
    cv2.imwrite("images/content_image.jpg", decodeImage(content))
    cv2.imwrite("images/style_image.jpg", decodeImage(style))


def decodeImage(img):
    image_bytes = base64.b64decode(img.split(',')[1])
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    return cv2.imdecode(image_array, flags=cv2.IMREAD_COLOR)


def delete_image(image_path):
    try:
        os.remove(image_path)
        print("Obrázok " + image_path + " bol odstránený!")
    except FileNotFoundError:
        print("Obrázok " + image_path + " sa nenašiel!")
