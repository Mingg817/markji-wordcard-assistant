import argparse
import asyncio
import sys

from . import trans

parser = argparse.ArgumentParser(
    prog='python -m markji_wordcard_assistant',
    epilog='More examples see README.md')
parser.add_argument('-f', required=True, metavar='FilePath', help="input word file", )
args = parser.parse_args()

try:
    asyncio.run(trans.trans(args.f))
except FileNotFoundError as e:
    print(e)
    sys.exit(-1)
