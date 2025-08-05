import uvicorn
from fastapi import FastAPI
from api.v1.router.gtm import gtmRouter
from etc.config import config

app = FastAPI()

app.include_router(gtmRouter, prefix="/api/v1/gtm")


@app.get("/health")
def read_health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host=config["host"], port=config["port"])
