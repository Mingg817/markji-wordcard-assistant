import asyncio
import logging
from asyncio import Queue
from typing import Dict, Callable, Any
from uuid import UUID, uuid4

from pydantic import Field, BaseModel

tasks = set()


class Job(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    func: Any = Field(exclude=True, default=None)
    status: str = "in_progress"
    progress: float = 0
    result: str = None

    async def start(self, *args, **kwargs):
        queue = Queue()
        task = asyncio.create_task(self.func(queue, *args, **kwargs))
        tasks.add(task)

        while info := await queue.get():
            logging.info("队列获取数据" + str(info))
            if len(info) == 0:
                break
            assert len(info) == 2
            assert isinstance(info[0], float)
            assert isinstance(info[1], str)
            self.progress, self.result = info

        self.status = "complete"


jobs: Dict[UUID, Job] = {}


def new_job(func: Callable) -> Job:
    job = Job()
    job.func = func
    jobs[job.uid] = job
    return job

