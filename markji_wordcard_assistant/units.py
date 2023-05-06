import json
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()


def requestAudioID(word: str, locale: str = "en-GB") -> str:
    try:
        return f"[Audio#ID/{_getIdFromUrl(_tts(word, locale))}#]"
    except Exception as e:
        print(e)
        sys.exit(1)


def _tts(word: str, locale: str = "en-GB"):
    token = os.getenv("TOKEN")
    if token is None:
        raise TypeError("【错误】TOKEN未提供")
    url = "https://www.markji.com/api/v1/files/tts"

    payload = json.dumps({
        "content_slices": [
            {
                "text": word,
                "locale": locale
            }
        ]
    })
    headers = {
        'authority': 'www.markji.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.markji.com',
        'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'token': token,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if (response.status_code == 400):
        raise ValueError("【错误】请检查输入的单词文件是否有问题")
    if (response.status_code == 401):
        raise ValueError("【错误】TOKEN错误，请检查")
    return json.loads(response.text)['data']['url']


def _getIdFromUrl(wordUrl: str):
    token = os.getenv("TOKEN")
    url = "https://www.markji.com/api/v1/files/url"

    payload = json.dumps({"url": wordUrl})
    headers = {
        'authority': 'www.markji.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.markji.com',
        'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'token': token,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)['data']['file']['id']
