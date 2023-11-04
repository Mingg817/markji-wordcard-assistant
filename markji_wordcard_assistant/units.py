import sys

from dotenv import load_dotenv

from markji_wordcard_assistant.markji_api import api
from markji_wordcard_assistant.voice import edge, markji_native, youdao

load_dotenv()


async def requestAudioID(word: str, locale: str = "en-GB", by: str = "default", speed: str = "+0%") -> str:
    """

    :param speed:
    :param word:
    :param locale:
        - en-GB or en-US
    :param by:
        - default 使用Markji自带的tts
          youdao 使用有道的发音api
    :return:
    """
    try:
        if by == "default":
            return f"[Audio#ID/{api.getIdFromUrl(markji_native.tts(word, locale))}#]"
        if by == "youdao":
            codes = {"en-GB": 1, "en-US": 2}
            return f"[Audio#ID/{api.uploadVoice(youdao.tts(word, codes[locale]))}#]"
        if by == "edge":
            return f"[Audio#ID/{api.uploadVoice(await edge.tts(word, rate=speed))}#]"

    except ValueError as e:
        print(e)
        sys.exit(1)


