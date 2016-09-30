#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-30 16:12:59
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import re
import urllib
import urllib2
import HTMLParser
import cookielib
import sys
import string 
import zlib
import base64

headers = {
	"Host":"gw.buaa.edu.cn:803",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
	"Accept": "*/*",
	"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Referer": "https://gw.buaa.edu.cn:803/beihanglogin.php?ac_id=20&url=http://gw.buaa.edu.cn:803/beihangview.php",
	"Cookie" : "cookie=25027385",
	"Connection" : "keep-alive"

}
postdata = {
	"action" : "login",
	"username" : "",
	"password" : "",
	"ac_id" : "1",
	"user_ip" : "",
	"nas_ip" : "",
	"user_mac" : "",
	"save_me" : "0",
	"ajax" : "1"
}
def addInfo(username, password):
	password = base64.b64encode(password)
	password = "{B}" + password
	postdata["username"] = username
	postdata["password"] = password

def login():
	global headers, postdata
	hosturl = r'http://gw.buaa.edu.cn/ac_detect.php'
	posturl = r"http://gw.buaa.edu.cn/beihanglogin.php"
	urltemp = r'http://gw.buaa.edu.cn/beihangview.php'
	cookjar = cookielib.LWPCookieJar()
	cookie_support = urllib2.HTTPCookieProcessor(cookjar)
	opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
	urllib2.install_opener(opener)
	req = urllib2.Request(hosturl)
	res = urllib2.urlopen(req)
	ans = res.read()
	# print ans
	with open('1.txt', "w") as o:
		for line in ans:
			o.write(line)
	pd = urllib.urlencode(postdata)
	req = urllib2.Request(posturl, pd, headers)
	res = urllib2.urlopen(req)
	# ans = res.read()
	req1 = urllib2.Request(urltemp)
	res = urllib2.urlopen(req1)
	ans = res.read()
	# print ans
	with open("out.txt", "w") as out:
		for line in ans:
			out.write(line)


if __name__ == '__main__':
	

	username = "sy1606318"
	password = "000000"
	addInfo(username, password)
	print postdata["password"]
	login()
