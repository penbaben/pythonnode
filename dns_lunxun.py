#!/usr/bin/python
#conding:utf-8

import dns.resolver
import os, http.client

def get_iplist(domain=""): #域名解析函数
    try:
        A = dns.resolver.query(domain, 'A')     #解析A记录
    except Exception as e:
        print("dns resolver error:" + str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                iplist.append(j.address)
    return True

def checkip(ip):
    checkurl = ip + ":80"
    getcontect = ""
    http.client.socket.setdefaulttimeout(5)     #定义http连接超时
    conn = http.client.HTTPConnection(checkurl)  #创建http连接对象

    try:
        conn.request("GET", "/", headers = {"Host": appdomain}) #发起url请求添加host主机头
        r = conn.getresponse()
        getcontent = r.read(15) #获取url页前15个字符，以便做可用性校验

    finally:
        if getcontent.decode() == '<!DOCTYPE html>':
            print(ip + " [ok] ")
        else:
            print(ip + " [error] ")

if __name__ == "__main__":    
    iplist = []      
    appdomain = input("please input appdomain:\n")
            
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print("dns resolver error.")

