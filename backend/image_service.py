import http.client, urllib.request, urllib.parse, urllib.error, base64
from PIL import Image
import numpy as np
from aip import AipImageClassify
from aip import AipOcr
import platform
import ssl

def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
                return fp.read()

def image_caption(image_path):
        headers = {
                # Request headers
                'Content-Type': 'application/octet-stream',
                'Ocp-Apim-Subscription-Key': 'c0da4e6ed24f48d5b3e5893899e83777',
        }

        params = urllib.parse.urlencode({
                # Request parameters
                'visualFeatures': 'Description',
                'language': 'en',
        })
        conn = http.client.HTTPSConnection('api.cognitive.azure.cn', context=ssl._create_unverified_context())
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, get_file_content(image_path), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        dict_result = eval(data)
        result = {}
        result['caption'] = dict_result['description']['captions'][0]['text']
        return result

def object_detection(image_path):
        headers = {
                # Request headers
                'Content-Type': 'application/octet-stream',
                'Ocp-Apim-Subscription-Key': 'c0da4e6ed24f48d5b3e5893899e83777',
        }

        params = urllib.parse.urlencode({
                # Request parameters
                'visualFeatures': 'Categories',
                'language': 'en',
        })
        obj_list = ['car','']
        APP_ID = '11099177'
        API_KEY = '537mYO15okLxK5kEIX9ons8N'
        SECRET_KEY = 'GoNqKxvwUNdOSLDxIg2O1kteSRygYl2q'
        client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
        image = get_file_content(image_path)
        
        result_temp = client.objectDetect(image)
        im = Image.open(image_path)
        left = result_temp['result']['left']
        top = result_temp['result']['top']
        width = result_temp['result']['width']
        height = result_temp['result']['height']
        region = im.crop((left, top, left + width, top + height))
        conn = http.client.HTTPSConnection('api.cognitive.azure.cn', context=ssl._create_unverified_context())
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, image, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        dict_result = eval(data)
        key = dict_result['categories'][0]['name']
        if key == 'people_crowd'  or key == 'portrait':
                key = 'people'
        if len(key.split('_')) > 1:
                key = key.split('_')[1]
        if key == '':
                return 'Regional security, please go straight.'
        middle = [im.size[0] / 2, im.size[1] / 2]
        left_up = [middle[0] / 2, middle[1] / 2]
        left_down = [left_up[0], left_up[1] + middle[1]]
        right_up = [left_up[0] + middle[0], left_up[1]]
        right_down = [right_up[0], left_down[1]]
        points = [middle, left_up, left_down, right_up, right_down]
        dis = [0,0,0,0,0]
        our_middle = [(left + width) / 2, (top + height) / 2]
        for i in range(5):
                dis[i] = (our_middle[0] - points[i][0]) * (our_middle[0] - points[i][0]) + (our_middle[1] - points[i][1]) * (our_middle[1] - points[i][1])
        id = np.argmin(dis)
        if id == 0:
                tip = 'There is a ' + key + ' in front of you. Please be careful'
        elif id == 1:
                tip = 'Please note that there is a ' + key + ' in left front'
        elif id == 2:
                tip = 'On the left there is a ' + key + ', please be careful'
        elif id == 3:
                tip = 'There is a ' + key +' in front of the right, please be careful'
        else:
                tip = 'On the right there is a ' + key + ', please be careful'
        return tip

def word_detection(image_path):
        APP_ID = '10673557'
        API_KEY = 'LMXCGq3dCDmNS9xXGB9HrzuG'
        SECRET_KEY = 'jyqeWRBZ5S3cmAPO7LTk8taBo6GdB55s'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        image = get_file_content(image_path)
        result_temp = client.basicGeneral(image)
        words = result_temp['words_result']
        result = ''
        for word in words:
                result += word['words'] + '\n'
        if result == '':
                return 'No any word.'
        return result

#print(object_detection('F:/IMG_20130328_174347.jpg'))
#print(image_caption('F:/IMG_20130328_174347.jpg'))
#print(word_detection('F:/IMG_20130328_174347.jpg'))

