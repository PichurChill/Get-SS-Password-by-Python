from urllib import request
import json
#z=抓取网页信息
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
    print(pw2+" "+pw3)
try:
    # 定位密码
    with open('C:\\Users\\Administrator\\Desktop\\gui-config.json', 'r') as r:
        rcontent=r.read()
        idx1=rcontent.find("US1.ISS.TF")
        idx2=rcontent.find("HK2.ISS.TF")
        idx3=rcontent.find("jp3.iss.tf")
    with open('C:\\Users\\Administrator\\Desktop\\gui-config.json', 'w') as r:
        # 定位密码
        rcontent=rcontent.replace(rcontent[idx1+48:idx1+56],pw1)
        rcontent=rcontent.replace(rcontent[idx2+49:idx2+57],pw2)
        rcontent=rcontent.replace(rcontent[idx3+48:idx3+56],pw3)
        r.write(rcontent)
except Exception as e:
    print (e)
