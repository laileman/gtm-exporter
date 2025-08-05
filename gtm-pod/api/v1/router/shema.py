from pydantic import BaseModel


class Gtm(BaseModel):
    name: str
    src_ip: str
    src_port: int
    protocol: str
    package: int
    code: int
