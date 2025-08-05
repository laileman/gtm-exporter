from pydantic import BaseModel


class MPID(BaseModel):
    mpid: int
    ip: str


# update
class MPIDUpdate(BaseModel):
    ip: str
