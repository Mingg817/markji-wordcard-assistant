from unit import *

if __name__ == '__main__':
    url=tts("assistant")
    id=getIdFromUrl(url)
    print(id)
    print(f"[Audio#ID/{id}#]")
