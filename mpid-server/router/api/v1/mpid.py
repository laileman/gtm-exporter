from fastapi import APIRouter
from router.api.v1.schema import MPID
from router.api.v1.response import Response
from redis_api.api import redis_api
from router.api.v1.schema import MPIDUpdate

router = APIRouter()


# 创建mpid
@router.post("/", response_model=Response)
@router.post("")
async def create_mpid(mpid: MPID):
    redis_api.set(mpid.mpid, mpid.ip)
    return Response(code=0, msg="success", data=mpid.dict())


# 获取mpid列表
@router.get("/", response_model=Response)
@router.get("")
async def get_all_mpid():
    mpid_list = redis_api.get_all()
    return Response(code=0, msg="success", data=mpid_list)


# 删除mpid
@router.delete("/{mpid}", response_model=Response)
@router.delete("")
async def delete_mpid(mpid: int):
    if redis_api.get(mpid) is None:
        return Response(code=1, msg="mpid not found", data=None)
    else:
        redis_api.delete(mpid)
        return Response(code=0, msg="success", data=None)


# update mpid
@router.put("/{mpid}", response_model=Response)
@router.put("")
async def update_mpid(mpid: int, mpid_update: MPIDUpdate):
    if redis_api.get(mpid) is None:
        return Response(code=1, msg="mpid not found", data=None)
    redis_api.update(mpid, mpid_update.ip)
    return Response(code=0, msg="success", data=None)


# 获取mpid
@router.get("/{mpid}", response_model=Response)
async def get_mpid(mpid: int):
    ip = redis_api.get(mpid)
    if ip is None:
        return Response(code=1, msg="mpid not found", data={})
    return Response(code=0, msg="success", data={"mpid": mpid, "ip": ip})


# 从 ip 获取 mpid
@router.get("/ip/{ip}", response_model=Response)
async def get_mpid_by_ip(ip: str):
    mpid = redis_api.get_by_ip(ip)
    if mpid is None:
        return Response(code=1, msg="ip not found", data=None)
    return Response(code=0, msg="success", data={"mpid": int(mpid), "ip": ip})
