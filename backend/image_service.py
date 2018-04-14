import http.client, urllib.request, urllib.parse, urllib.error, base64
#import httplib, urllib, base64
from PIL import Image
import numpy as np
from aip import AipImageClassify
import ssl

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def image_caption(data):
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': 'c0da4e6ed24f48d5b3e5893899e83777',
    }

    #params = urllib.urlencode({
    # Request parameters
    #'visualFeatures': 'Description',
    #'language': 'en',
    #})
    params = urllib.parse.urlencode({
        # Request parameters
        'visualFeatures': 'Description',
        'language': 'en',
    })
    #conn = httplib.HTTPSConnection('api.cognitive.azure.cn')
    conn = http.client.HTTPSConnection('api.cognitive.azure.cn', context=ssl._create_unverified_context())
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, data, headers)
    response = conn.getresponse()
    data = response.read()
    dict_result = eval(data)
    print(dict_result)
    result = {}
    result['caption'] = dict_result['description']['captions'][0]['text']
    return result

#object_detection('F:/IMG_20130328_174347.jpg')
#print(image_caption('F:/IMG_20130328_174347.jpg'))

