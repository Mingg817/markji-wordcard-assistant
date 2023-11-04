import tempfile

from fastapi import FastAPI, BackgroundTasks, UploadFile

from .jobs import *
from .result import R
from .. import units

app = FastAPI()


class Web_auth(BaseModel):
    markji_api_key: str | None


@app.post("/trans")
async def trans(
        file: UploadFile,
        background_tasks: BackgroundTasks
):
    async def trans(q: Queue, upload_file: str, locale: str = "en-GB", by: str = "default", speed: str = "+0%"):
        _, tmpPath = tempfile.mkstemp(suffix=".txt", prefix="OUT_", text=True)
        logging.info(f"保存在 {tmpPath}")
        with open(tmpPath, "w") as tmpFile:
            with upload_file.file as f:
                data = [i.decode("utf-8") for i in f.readlines()]
                total_len = len(data)
                now_line = 0
                for line in data:
                    now_line += 1
                    if line[0:3] == "###":
                        tmpFile.write(line + "\n")
                        tmpFile.flush()
                        await q.put((now_line * 1.0 / total_len, line))
                        continue
                    splitChar = '\t' if '#' not in line else '#'
                    line = [i.strip() for i in line.split(splitChar)]
                    word = line[0]
                    if (word == ""):
                        continue
                    while word.isdigit():
                        line.pop(0)
                        word = line[0]
                    tmp = [await units.requestAudioID(word=word, locale=locale, by=by, speed=speed), "---",
                           "\n".join(line)]
                    s = "\n".join(tmp)
                    tmpFile.write(f"{s}\n\n")
                    tmpFile.flush()
                    await q.put((now_line / total_len, f"{s}\n"))

        await q.put((100.0, tmpPath))
        await q.put(tuple())

    j = new_job(trans)
    background_tasks.add_task(j.start, upload_file=file)
    return R.success({'job_id': j.uid})


@app.get("/jobs/progress/{id}")
async def job_progress(id: str):
    j = jobs.get(UUID(id), None)
    if j is None:
        return R.fail(message="Job not found")
    else:
        return R.success(j.model_dump())
