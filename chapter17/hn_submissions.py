#encoding=utf-8

import requests
from operator import itemgetter

#ִ��API���ò��洢��Ӧ
url = 'http://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)
