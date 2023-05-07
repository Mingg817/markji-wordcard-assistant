import asyncio
import random
import tempfile

import pyperclip

from . import units


async def trans(filepath: str):
    transed = []
    _, tmpPath = tempfile.mkstemp(suffix=".txt", prefix="OUT_", text=True)
    tmpFile = open(tmpPath, "w")
    with open(filepath, "r") as f:
        for line in f:
            line = [i.strip() for i in line.split("\t")]
            word = line[0]
            if (word == ""):
                continue
            if (word.isdigit()):
                line.pop(0)
                word = line[0]
            tmp = [units.requestAudioID(word), "---", "\n".join(line)]
            transed.append("\n".join(tmp))
            tmpFile.write(f"{transed[-1]}\n\n")
            tmpFile.flush()
            print(f"{transed[-1]}\n")
            await asyncio.sleep(random.random())
    result = "\n\n".join(transed)
    pyperclip.copy(result)
    print("\n完成！已复制到剪切板")
    print(f"保存在 {tmpPath}")
