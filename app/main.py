from fastapi import FastAPI

app = FastAPI(
    title="FastDrop",
    description="System for delivering orders in the shortest possible time",
)


@app.get("/ping")
async def ping():
    return {"ping": "pong"}
