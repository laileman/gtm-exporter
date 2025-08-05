from pydantic import BaseModel


class Response(BaseModel):
    code: int
    msg: str
    data: dict | list | None = None
