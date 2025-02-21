# main.py

import logging 
from fastapi import FastAPI,Request
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", filename='logs.txt')
logger = logging.getLogger(__name__)
app = FastAPI()

@app.get("/ping")
async def ping(request:Request):
    client_host = request.client.host
    logger.info(f"Получен запрос от {client_host}")
    return {"status": "ok"}