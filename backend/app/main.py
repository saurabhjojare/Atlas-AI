from fastapi import FastAPI
from app.api.send_message import router

app = FastAPI()
app.include_router(router)