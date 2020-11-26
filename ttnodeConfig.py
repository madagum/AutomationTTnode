#!/usr/bin/python3
#coding=utf-8
import urllib3
import json
import datetime as dt
import time
import sys
def getCode(phone):#获取验证码！
    print(phone)
    url="http://tiantang.mogencloud.com/web/api/login/code"
    body_json="phone="+phone
    encoded_body=body_json.encode('utf-8')
    http = urllib3.PoolManager()
    header={"Content-Type":"application/x-www-form-urlencoded"}
    response= http.request('POST', url,body=encoded_body,headers=header)
    if response.status!=201 and response.status!=200:
       print("getCode方法请求失败，结束程序")

       exit()
    data=response.data.decode('utf-8')
    data=json.loads(data)

    if data['errCode']!=0:
        print("请输入正确的手机号码！")
        exit()
    data=data['data']
    return

def getAuthorization(phone,authCode):#获取Authorization
    url="http://tiantang.mogencloud.com/web/api/login"
    body_json="phone="+phone+"&authCode="+authCode
    encoded_body=body_json.encode('utf-8')
    header={"Content-Type":"application/x-www-form-urlencoded"}
    http = urllib3.PoolManager()
    response= http.request('POST', url,body=encoded_body,headers=header)
    if response.status!=201 and response.status!=200:
       print("getAuthorization方法请求失败，结束程序")
       exit()
    data=response.data.decode('utf-8')
    data=json.loads(data)

    if data['errCode']!=0:
        print("验证码错误!等待1分钟后重新运行再次获取验证码！\n")
        exit()
    data=data['data']

    return data['token']

#********************************main******************************************
path=sys.path[0]
print("免责声明：\n本程序唯一下载地址：https://www.right.com.cn/forum/thread-4048219-1-1.html 如果你在别的地方下载的，出现问题与作者无关！\n本程序开源，开源自己查阅源码是否有后门。一切个人信息只用于甜糖程序api，请放心使用！，同时禁止转载本相关程序文件！\n禁止使用本程序用于一切商业活动，本程序只供个人学习研究使用。如有侵权请联系作者删除相关内容！\n开源地址：https://github.com/744287383/AutomationTTnode\n")
stats=input("接受此免责声明：输入1为接受，输入任意字符为不接受,结束程序\n")
if stats!='1':
	exit()
phonenum=input("请输入手机号码回车键提交:\n")
phonenum=str(phonenum)
if len(phonenum)!=11:
    print("请输入正确的手机号码!!请重新运行")
    exit()
getCode(phonenum)
print("验证码发送成功请耐性等待！\n")
authCode=input("请确保你输入验证码短信是甜糖发的验证码短信，以免造成经济损失，概不负责。\n请输入验证码：\n")
authCode=str(authCode)
if len(authCode)!=6:
    print("请输入正确的验证码!!请重新运行")
    exit()
authorization=getAuthorization(phonenum,authCode)
print("你的authorization：\n\n"+authorization+"\n\n")

sckey=input("请进入http://sc.ftqq.com/登录并绑定微信后获取sckey!\n请输入你的server酱的sckey码：\n")
config={}
config["authorization"]=authorization
config["sckey"]=sckey
try:
    file=open(path+"/ttnodeConfig.config","w+",encoding="utf-8",errors="ignore")
    file.write(str(config))
    file.flush()
finally:
    if file:
        file.close()
print("已经配置成功了，请用python执行sendTTnodeMSG.py文件，以及配置定时程序。填写邀请码123463支持作者！")
exit()