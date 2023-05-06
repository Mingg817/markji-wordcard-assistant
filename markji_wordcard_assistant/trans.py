import asyncio

import pyperclip

from . import units


async def trans(filepath: str):
    transed = []
    with open(filepath, "r") as f:
        for word in f:
            word = word.strip()
            if (word == ""):
                continue
            tmp = [units.requestAudioID(word), "---", word]
            transed.append("\n".join(tmp))
            await asyncio.sleep(1)
    result = "\n\n".join(transed)
    print(result)
    pyperclip.copy(result)
    print("\n完成！已复制到剪切板")
