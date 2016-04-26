#!/usr/bin/env python3
from urllib import request
import json,os
from collections import OrderedDict


def updatePw(pw1,pw2,pw3,j):
    length=len(j["configs"])
    for x in range(length):
        if ((j["configs"][x]["server"]).upper()=="US1.ISS.TF"):
            j["configs"][x]["password"]=pw1
        if ((j["configs"][x]["server"]).upper()=="HK2.ISS.TF"):
            j["configs"][x]["password"]=pw2
        if ((j["configs"][x]["server"]).upper()=="JP3.ISS.TF"):
            j["configs"][x]["password"]=pw3

# z=抓取网页信息
with request.urlopen('http://www.ishadowsocks.net/') as f:
    data = f.read()
# 从转成string格式
    data=data.decode()  
# 获取密码
    ind1=data.find("A密码:")
    pw1=data[ind1+4:ind1+12]
    ind2=data.find("B密码:")
    pw2=data[ind2+4:ind2+12]
    ind3=data.find("C密码:")
    pw3=data[ind3+4:ind3+12]
try:
    # 定位密码
    if os.path.exists('./gui-config.json'):
        with open('./gui-config.json', 'r') as r:
            rcontent=r.read()
            #转成json格式
            j=json.loads(rcontent,object_pairs_hook=OrderedDict)
            updatePw(pw1,pw2,pw3,j)
        with open('./gui-config.json', 'w') as r:
            r.write(json.dumps(j))
    else:
        with open('./gui-config.json', 'w') as r:
            with open('./config.json', 'r') as r2:
                content=r2.read()
                jnew=json.loads(content,object_pairs_hook=OrderedDict)
                updatePw(pw1,pw2,pw3,jnew)
            r.write(json.dumps(jnew))
except Exception as e:
    print (e)


