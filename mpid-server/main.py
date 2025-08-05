from fastapi import FastAPI
from router.api.v1.mpid import router
from etc.config import config
import uvicorn

app = FastAPI()
app.include_router(router, prefix="/api/v1/mpid")


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host=config.server_host, port=config.server_port)
