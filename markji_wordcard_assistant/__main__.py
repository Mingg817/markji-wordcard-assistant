# import argparse
# import asyncio
# import sys
#
# from . import trans
import os

import uvicorn

# parser = argparse.ArgumentParser(
#     prog='python -m markji_wordcard_assistant',
#     epilog='More examples see README.md')
# parser.add_argument('-f',
#                     required=True,
#                     metavar='',
#                     help="指定输入的文件", )
# parser.add_argument("-v", "--voice",
#                     metavar='',
#                     default="en-GB",
#                     help="[可选]指定英式美式发英,默认`en-GB`,可选`en-US`", )
# parser.add_argument("-b", "--by",
#                     metavar='',
#                     default="default",
#                     help="[可选]指定选定的语音来源,默认default,可选youdao edge", )
# parser.add_argument("-s", "--speed",
#                     metavar='',
#                     default="+0%",
#                     help="[可选]语音的速度", )
# args = parser.parse_args()
#
# try:
#     asyncio.run(trans.trans(args.f, args.voice, args.by, args.speed))
# except FileNotFoundError as e:
#     print(e)
#     sys.exit(-1)

if __name__ == "__main__":
    uvicorn.run("open_api.main:app",
                app_dir=os.path.dirname(os.path.abspath(__file__)),
                host="0.0.0.0",
                port=8000,
                reload=True)
