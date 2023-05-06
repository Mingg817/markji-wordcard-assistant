import argparse
import asyncio

from . import trans

parser = argparse.ArgumentParser(
    prog='python -m markji_wordcard_assistant',
    epilog='More examples see README.md')
parser.add_argument('-f', required=True, metavar='FilePath', help="input word file", )
args = parser.parse_args()

asyncio.run(trans.trans(args.f))
