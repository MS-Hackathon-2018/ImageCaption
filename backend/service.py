import http.client
import hashlib
import urllib
import random
import json

paramDict = {
    'zh-en': {
        "fromLang": 'zh-CHS',
        "toLang": 'EN',
    },
    'en-zh': {
        "toLang": 'zh-CHS',
        "fromLang": 'EN',
    },
}

def _translate(text, suite):
    appKey = '2d96e4bbc2a5844f'
    secretKey = '1eJgJsttAz2ahuH8rtFhJNPrs5yqPwST'
    httpClient = None
    myurl = '/api'
    q = text
    salt = random.randint(1, 65536)

    fromLang = paramDict.get(suite)["fromLang"]
    toLang = paramDict.get(suite)["toLang"]

    sign = appKey+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode('utf-8'))
    sign = m1.hexdigest()
    myurl = myurl+'?appKey='+appKey+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

    httpClient = http.client.HTTPConnection('openapi.youdao.com')
    httpClient.request('GET', myurl)
    #response是HTTPResponse对象
    response = httpClient.getresponse()

    result = response.read()

    # 返回json
    return(json.loads(result))

def Chinese2English(chinese):
    return _translate(chinese, "zh-en")
def English2Chinese(english):
    return _translate(english, "zh-en")

