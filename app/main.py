from fastapi import FastAPI

from app.api import router as global_router
from app.models.order import Order  # noqa: F401

app = FastAPI(
    title="FastDrop",
    description="System for delivering orders in the shortest possible time",
)

app.include_router(global_router)


@app.get("/ping")
async def ping():
    return {"ping": "pong"}
