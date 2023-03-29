source env/bin/activate

PORT=10100
fuser -k $PORT/tcp
uvicorn main:app --host 158.196.145.23 --port $PORT 
