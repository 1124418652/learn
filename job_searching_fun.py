#!usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from bs4 import BeautifulSoup as bs 
import re
import time
import requests
import xlwt
import xlrd
from xlutils.copy import copy 
from random import choice

__version__ = '1.1.20170525'

def createxls(keyword):
	wb = xlwt.Workbook(encoding = 'ascii')
	time9 = time.strftime("%Y-%m-%d", time.localtime())
	ws = wb.add_sheet(time9+'智联招聘')      #新建工作表
	ws.write(0, 0, 'job_name')
	ws.write(0, 1, 'enterprise_name')
	ws.write(0, 2, 'payment')
	ws.write(0, 3, 'work_place')
	ws.write(0, 4, 'note_time')
	ws.write(0, 5, 'place')
	ws.write(0, 6, 'company_type')
	ws.write(0, 7, 'company_size')
	ws.write(0, 8, 'education')
	ws.write(0, 9, 'responsibility')
	wb.save(keyword+'job_imformation.xls')        #保存工作表	

def useragent():        #自定义客户端
	USER = [
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727;\
			Media Center PC 5.0; .NET CLR 3.0.04506)",
			"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322;\
			.NET CLR 2.0.50727)",
			"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729;\
			.NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 \
			Safari/535.11",
			]
	headers = chioce(USER)
	return headers

def get_urllist(keyword):         #get uniform resource locator
	urllist = ['']*90
	page = 1
	d = 0
	while d < 90:
		urllist[d] = 'http://sou.zhaopin.com/jobs/searchresult.ashx?ji=选择地区&kw='+keyword+\
			'&isadv=0&sg=91f598e913974f4687a7bfb86b54c91d&p='+str(page)
		d = d+1
		page = page+1
	return urllist
	
def open_page(url):
	print('正在打开网页：\n'+str(url))
	try:
		user = useragent()
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
			AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
		r = requests.get(url, headers = headers, timeout = 10)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except Exception as e:
		print('Error:',e)
		time3 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
		content = time3 + ' ' + str(e)
		logpath = '51joblog.txt'
		with open(logpath, 'a') as f:
			f.write(content + "\n")
		pass
		
def write_xls(html, k, temp, keyword):
	time3 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	print('正在爬取第'+str(k+1)+'页'+time3)
	soup = bs(html, 'lxml')
	name = soup.findAll('a', href = re.compile())














	
