# -*- coding: utf-8 -*-
# author: songwei
# place: Shenzhen Guangdong
# time: 2020/4/30 14:53
import os, re, json, traceback
from headers import  requests_headers  # 上一篇文章中所写的自动转变headers文件
from bs4 import BeautifulSoup
import requests
header = requests_headers()  #调用requests_headers() 返回一个随机的headers文件
proxies = {'http': 'http://139.0.28.18:8080'}  #这个地方换一下ip和端口号
url = 'http://www.whatismyip.com.tw' #访问这个网站可以返回你的IP地址 以此验证是否变换成功
try:
    #每次切换一个ip代理
    wb_data = requests.get(url,headers=header,proxies=proxies,timeout=5) #timeout 限定5秒相应后就退出执行
    soup = BeautifulSoup(wb_data.text,'lxml')
    print(soup)
except(requests.exceptions.ProxyError,requests.exceptions.ConnectTimeout):
    print('failed!')

#国外IP 1.179.183.86:8080 113.53.231.201:3129 182.23.28.180:3128 182.253.177.59:3128 139.0.28.18:8080


#根据代理ip池自动ip切换
__author__ = 'Lee'
import random
ip_pool = [
    '119.98.44.192:8118',
    '111.198.219.151:8118',
    '101.86.86.101:8118',
]
def ip_proxy():
    ip = ip_pool[random.randrange(0,3)]
    proxy_ip = 'http://'+ip
    proxies = {'http':proxy_ip}
    return proxies

print(ip_proxy())























































