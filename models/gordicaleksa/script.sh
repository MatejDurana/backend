params=$1
. models/gordicaleksa/py_env/venv/bin/activate
python models/gordicaleksa/neural_style_transfer.py  --content_img_name content_image.jpg --style_img_name style_image.jpg $params
deactivate