import logging
import urllib.request

from fastapi import FastAPI, APIRouter

from .controller import trans_file, jobs_controller, trans_text
from .exception import *

logging.info("启动FastApi服务")
logging.info(f"当前代理：{urllib.request.getproxies()}")
try:
    urllib.request.urlopen('https://www.google.com')
except Exception as e:
    logging.error("代理测试失败,请检查代理")
    logging.error(e)
else:
    logging.info("代理测试成功")

tags_metadata = [
    {
        "name": "file",
        "description": "上传文件并生成任务",
    },
    {
        "name": "text",
        "description": "文本转化MARKJI音频ID"
    },
    {
        "name": "jobs",
        "description": "有关任务调度的接口"
    },
]

app = FastAPI(title="MarkJi WordCard Assistant",
              version="0.4",
              contact={
                  "name": "MingLi",
                  "url": "https://github.com/Mingg817",
                  "email": "li@eming.ing"
              },
              license_info={
                  "name": "MIT License",
              },
              openapi_tags=tags_metadata)
api_router = APIRouter()

configure_exceptions(app)

api_router.include_router(trans_file.router, prefix="/file", tags=['file'])
api_router.include_router(trans_text.router, prefix="/text", tags=['text'])
api_router.include_router(jobs_controller.router, prefix="/jobs", tags=['jobs'])

app.include_router(api_router, prefix="/api")
