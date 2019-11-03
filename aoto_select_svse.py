# -*- coding: utf-8 -*-
import requests
import json
from html import unescape
import pymysql

file = open('out.txt','w',encoding='UTF-8')

db= pymysql.connect(host="{数据库ip}",user="{用户名}",password="{密码}",db="data",port=3306)
cur = db.cursor()

url = "{api接口}"
headers = {'content-type': 'application/json'}
ret = requests.get(url, headers=headers)
json_data=json.loads(ret.text)

count_single = 0
count_multiple = 0
count_vacancy = 0
questionContent=""
optionsA=""
optionsB=""
optionsC=""
optionsD=""
optionsE=""
for i in range(0,40):
    long = len(json_data.get('body').get('examItems')[i].get('jsonData').get('single').get('options'))
    questionContent=unescape(json_data.get('body').get('examItems')[i].get('questionContent'))
    sql_select = "SELECT `select` from single where questionContent = '%s'" % questionContent
    cur.execute(sql_select)
    result = cur.fetchall()
    if result:
        if result[0][0]:
            file.write(str(i+1)+'.【单选题】 答案：'+ result[0][0] + "\n")
            count_single = count_single + 1
        else:
            file.write(str(i+1)+'.【单选题】'+unescape(json_data.get('body').get('examItems')[i].get('questionContent'))+'\n')
            for j in range(0, long):
                file.write(chr(65 + j) + '.' + json_data.get('body').get('examItems')[i].get('jsonData').get('single').get('options')[j].get('optionsContent') + '\n')
    else:
        if long== 4:
            optionsA='A.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('single').get('options')[0].get('optionsContent'))
            optionsB='B.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('single').get('options')[1].get('optionsContent'))
            optionsC='C.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('single').get('options')[2].get('optionsContent'))
            optionsD='D.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('single').get('options')[3].get('optionsContent'))
            sql_insert = "insert into single(questionContent,optionsA,optionsB,optionsC,optionsD) values('%s','%s','%s','%s','%s')" % (questionContent, optionsA,optionsB,optionsC,optionsD)
        else:
            optionsA='A.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('single').get('options')[0].get('optionsContent'))
            optionsB='B.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('single').get('options')[1].get('optionsContent'))
            optionsC='C.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('single').get('options')[2].get('optionsContent'))
            sql_insert = "insert into single(questionContent,optionsA,optionsB,optionsC) values('%s','%s','%s','%s')" % (questionContent, optionsA,optionsB,optionsC)
        cur.execute(sql_insert)
        db.commit()
        file.write(str(i + 1) + '.【单选题】' + unescape(json_data.get('body').get('examItems')[i].get('questionContent')) + '\n')
        for j in range(0, long):
            file.write(chr(65 + j) + '.' + json_data.get('body').get('examItems')[i].get('jsonData').get('single').get('options')[j].get('optionsContent') + '\n')
for i in range(40,60):
    questionContent = unescape(json_data.get('body').get('examItems')[i].get('questionContent'))
    long = len(json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options'))
    sql_select = "SELECT `select` from multiple where questionContent = '%s'" % questionContent
    cur.execute(sql_select)
    result = cur.fetchall()
    if result:
        if result[0][0]:
            file.write(str(i + 1) + '.【多选题】 答案：' + result[0][0] + "\n")
            count_multiple = count_multiple + 1
        else:
            file.write(str(i + 1) + '.【多选题】' + unescape(json_data.get('body').get('examItems')[i].get('questionContent')) + '\n')
            for j in range(0, long):
                file.write(chr(65 + j) + '.' + json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options')[j].get('optionsContent') + '\n')
    else:
        if long == 4:
            optionsA='A.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options')[0].get('optionsContent'))
            optionsB='B.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options')[1].get('optionsContent'))
            optionsC='C.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options')[2].get('optionsContent'))
            optionsD='D.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options')[3].get('optionsContent'))
            sql_insert = "insert into multiple(questionContent,optionsA,optionsB,optionsC,optionsD) values('%s','%s','%s','%s','%s')" % (questionContent, optionsA,optionsB,optionsC,optionsD)
        elif long == 5:
            optionsA='A.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options')[0].get('optionsContent'))
            optionsB='B.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options')[1].get('optionsContent'))
            optionsC='C.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options')[2].get('optionsContent'))
            optionsD='D.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options')[3].get('optionsContent'))
            optionsE='E.'+unescape(json_data.get('body').get('examItems')[i].get('jsonData').get('multiple').get('options')[4].get('optionsContent'))
            sql_insert = "insert into multiple(questionContent,optionsA,optionsB,optionsC,optionsD,optionsE) values('%s','%s','%s','%s','%s','%s')" % (questionContent, optionsA,optionsB,optionsC,optionsD,optionsE)
        else:
            print("not find")
        cur.execute(sql_insert)
        db.commit()
for i in range(60,80):
    questionContent=unescape(json_data.get('body').get('examItems')[i].get('questionContent'))
    sql_select = "SELECT answer from vacancy where questionContent = '%s'" % questionContent
    cur.execute(sql_select)
    result = cur.fetchall()
    if result:
        if result[0][0]:
            file.write(str(i + 1) + '.【填空题】 答案：' + result[0][0] + "\n")
            count_vacancy = count_vacancy + 1
        else:
            file.write(str(i + 1) + '.【填空题】' + unescape(json_data.get('body').get('examItems')[i].get('questionContent')) + '\n')
    else:
        sql_insert = "insert into vacancy(questionContent) values('%s')" % (questionContent)
        cur.execute(sql_insert)
        db.commit()
        file.write(str(i + 1) + '.【填空题】' + unescape(json_data.get('body').get('examItems')[i].get('questionContent')) + '\n')
db.close()
print("单选题题库中查询到：" + str(count_single) + "道题")
print("多选题题库中查询到：" + str(count_multiple) + "道题")
print("填空题库中查询到：" + str(count_vacancy) + "道题")