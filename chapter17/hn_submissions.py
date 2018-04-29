#encoding=utf-8

import requests
from operator import itemgetter

#执行API调用并存储响应
url = 'http://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)
