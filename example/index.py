
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
            return response.text
        return None
    except RequestException as e:
        print('err: %s,%s' % e,url)


def main():
	url = 'http://localhost:5555/random'
	html = get_response(url)
	print(html)
	
if __name__ == '__main__':
	main()
