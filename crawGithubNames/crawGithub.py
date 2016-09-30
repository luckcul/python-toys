#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-25 18:50:14
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

def getLeecodeName():
	isFile = os.path.isfile(r'content.txt')
	if isFile :
		f = open('content.txt')
		content = f.read()
		return content
	url = r'https://github.com/haoel/leetcode'
	page = urllib.urlopen(url);
	content = page.read()
	with open('content.txt', 'w') as out:
		for line in content: 
			out.write(line)
	return content
	# print content
def findName():
	con = getLeecodeName()
	st = r'leetcode.com/problems/.+/">(.*)</a></td>'
	reg = re.compile(st)
	return re.findall(reg, con)
def creatDir():
	names = findName()
	dire = 'E:\\myGithub\\LeetCode\\algorithms'
	for name in names:
		nowDir = dire + '\\' + name 
		isDir = os.path.exists(nowDir)
		if isDir:
			continue
		else:
			try:
				os.makedirs(nowDir)
			except:
				print name
	print 'ok'

if __name__ == '__main__':
	creatDir()