
import requests
from requests.exceptions import RequestException


base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}


def get_response(url,params={},options={}):
    headers = dict(base_headers, **options)
    try:
        response = requests.get(url,params=params,headers=headers)
        if response.status_code == 200:
            if response.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(response.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = response.apparent_encoding

                #如果设置为replace，则会用?取代非法字符；
                encode_content = response.content.decode(encoding, 'replace')
                return encode_content
            return response.text
        return None
    except RequestException as e:
        print('err: %s,%s' % e,url)
