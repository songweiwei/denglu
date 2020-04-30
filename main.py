# -*- coding: utf-8 -*-
# author: songwei
# place: Shenzhen Guangdong
# time: 2020/4/30 10:56
import os, re, json, traceback

'''
小红书模拟登陆
'''

''' 第一步 '''
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
r=requests.get('http://post.xiaohongshu.com/api/homerus/login/captcha')
token = json.loads(r.text)['data']['token']     # get请求到的token
#print token
img_url=json.loads(r.text)['data']['url']
picture = opener.open(img_url).read()
local = open('F:/code.jpg', 'wb')               # 保存验证码到本地
local.write(picture)
local.close()
''' 第二步 '''
secret_code = raw_input('输入验证码： ')
login_data = {
    'phone': '136****0000',
    'passwd': 'XXXXXXXXXXXX',
    'token': token,                             # 获取的token
    'captcha': secret_code,                     # 手动输入的验证码
    'zone': '86'
}
headers = {'content-type': 'application/json'}  # payload请求方式
res = requests.post('http://post.xiaohongshu.com/web_api/sns/v1/homerus/user/login_with_passwd'
                    ,data=json.dumps(login_data),headers=headers)                                                      # 模拟登录
header={ ''' 第三步 '''
    'Accept': 'application / json, text / plain',
    'Connection': 'keep - alive',
    'Cookie': res.headers['Set-Cookie'].replace(' Path=/','')+'xhs_spid.6d29=21fa0111a09b6c3c'
                         '1516671392.1.15166716811516671392.6d3c3921-2e47-4cbe-b695-698499ac4636; xhs_spses.6d29=*',   # 登录成功的cookie拼装在header
    'Referer': 'http: // post.xiaohongshu.com /',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
resp = requests.get('http://post.xiaohongshu.com/web_api/sns/v1/homerus/note/list?page=1&page_size=200',headers=header)
data = json.loads(resp.text)























































