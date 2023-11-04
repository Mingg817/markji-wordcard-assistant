from pydantic import BaseModel


class R(BaseModel):
    status: str = ""
    message: str = ""
    data: dict = {}

    @staticmethod
    def success(data: dict = None):
        return R(status="success", data=data)

    @staticmethod
    def fail(message: str = None, data: dict = None):
        return R(status="fail", message=message)