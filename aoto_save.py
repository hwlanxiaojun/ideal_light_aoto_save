#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
from html import unescape

file = open('D:\\out.txt','w',encoding='UTF-8')
url = "{api接口}"
headers = {'content-type': 'application/json'}
ret = requests.get(url, headers=headers)
json_data=json.loads(ret.text)
for i in range(0,40):
    long = len(json_data.get('body').get('examItems')[i].get('jsonData').get('single').get('options'))
    file.write(str(i+1)+'.【单选题】'+unescape(json_data.get('body').get('examItems')[i].get('questionContent'))+'\n')
    for j in range(0,long):
        file.write(chr(65+j)+'.'+json_data.get('body').get('examItems')[i].get('jsonData').get('single').get('options')[j].get('optionsContent')+'\n')
for i in range(40,60):
    file.write(str(i+1)+'.【多选题】'+unescape(json_data.get('body').get('examItems')[i].get('questionContent'))+'\n')
    long = len(json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options'))
    for j in range(0, long):
        file.write(chr(65+j)+'.'+json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options')[j].get('optionsContent')+'\n')
for i in range(60,80):
    file.write(str(i+1)+'.【填空题】'+unescape(json_data.get('body').get('examItems')[i].get('questionContent'))+'\n')



