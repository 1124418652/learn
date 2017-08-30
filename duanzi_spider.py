# -*- coding: utf-8 -*-

import urllib2,urllib
import re
import sys

class spider(object):
	"""
	Define a class of the spider class 
	"""
	
	def __init__(self):
		self.enable = True
		self.page = 1
		
	def load_page(self, url):
		"""
		return the stable html page of the url you've input
		and extract data from the page
		"""

		user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"
		headers = {"User-Agent": user_agent}
		req = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(req)
		html = response.read().decode('gbk').encode('utf-8')
		pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
		data = pattern.findall(html)
		return data
				
	def get_url(self, page):
		"""
		return the url of the page that you want to overview
		the result of this function can be the input of load_page
		"""
		
		url = "http://www.neihan8.com/article/list_5_"
		url = url + str(page) + ".html"
		return url

	def do_work(self):
		"""
		this is the API which allows people to interact with the program
		"""
		sys.stdout.write("input the page that you want to read:")
		page = input()
		while self.enable:
			url = self.get_url(page)
			print("starting loading data of page %d ..." %(page))
			data = self.load_page(url)
			print("finish loading data of page %d" %(page))
			
			for tmp in data:
				print("================")
				print(tmp.replace(r'<p>', '').replace(r'/p','').replace(r'<br />','').replace('<>',''))
				
			print('-------------page %d-------------\n' %(page))
			sys.stdout.write("press ENTER to continue, else input quit to exit:")
			command = raw_input()
			
			if command == 'quit':
				self.enable = False
				break
			page += 1


if __name__ == "__main__":
	spider1 = spider()
	spider1.do_work()
	






