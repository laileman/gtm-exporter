from fastapi import APIRouter
from api.v1.router.shema import Gtm
from log.format import format_logger

gtmRouter = APIRouter()


@gtmRouter.get("/")
@gtmRouter.get("")
def read_gtm():
    return {"code": 0, "msg": "success", "data": None}


@gtmRouter.post("/")
@gtmRouter.post("")
def post_gtm(gtm: Gtm):
    format_logger(gtm.__dict__)
    return {"code": 0, "msg": "success", "data": None}
