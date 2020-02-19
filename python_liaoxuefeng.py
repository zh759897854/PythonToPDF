# coding=utf-8
from __future__ import unicode_literals

import logging
import os
import re
import time

from fake_useragent import UserAgent

try:
	from urllib.parse import urlparse  # py3
except:
	from urlparse import urlparse  # py2

import pdfkit
import requests
from bs4 import BeautifulSoup
from pprint import pprint

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""


class Crawler(object):
	"""
	爬虫基类，所有爬虫都应该继承此类
	"""
	name = None

	def __init__(self, name, start_url):
		"""
		初始化
		:param name: 将要被保存为PDF的文件名称
		:param start_url: 爬虫入口URL
		"""
		self.name = name
		self.start_url = start_url
		uri = urlparse(self.start_url)
		self.domain = '{uri.scheme}://{uri.netloc}'.format(uri=uri)
		self.headers={'User-Agent': UserAgent().random,
					  'Host': uri.netloc,
					  'Cache-Control':'no-cache',
					  'Connection':'keep-alive',
					  'Pragma':'no-cache',
					  'DNT':'1',
					  'Referer':self.start_url,
					  'Upgrade-Insecure-Requests': '1',
					  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
					  'Accept-Encoding':"gzip, deflate, br",
					  'Accept-Language':"zh-CN,zh;q=0.9,en;q=0.8,la;q=0.7",
					  }

	@staticmethod
	def request(url, headers):
		"""
		网络请求,返回response对象
		:return:
		"""
		#headers = {'User-Agent': UserAgent().random, 'referer': 'https://www.liaoxuefeng.com/'}
		#response = requests.get(url, headers=headers)
		response=R_SESSION.get(url, headers=headers)
		pprint('------------------------------------------------------------')
		pprint(url)
		pprint(headers)
		pprint(response.reason)
		return response

	def parse_menu(self, response):
		"""
		从response中解析出所有目录的URL链接
		"""
		raise NotImplementedError

	def parse_body(self, response):
		"""
		解析正文,由子类实现
		:param response: 爬虫返回的response对象
		:return: 返回经过处理的html正文文本
		"""
		raise NotImplementedError

	def run(self):
		start = time.time()
		options = {
			'page-size': 'Letter',
			'margin-top': '0.75in',
			'margin-right': '0.75in',
			'margin-bottom': '0.75in',
			'margin-left': '0.75in',
			'encoding': "UTF-8",
			'custom-header': [
				('Accept-Encoding', 'gzip')
			],
			'cookie': [
				('cookie-name1', 'cookie-value1'),
				('cookie-name2', 'cookie-value2'),
			],
			'outline-depth': 10,
		}
		htmls = []

		#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
		aaaa=self.parse_menu(self.request(self.start_url,self.headers))
		for index, url in enumerate(aaaa):
			time.sleep(1)
			html = self.parse_body(self.request(url,self.headers))
			self.headers['Referer']=url
			f_name = ".".join([str(index), "html"])
			with open(f_name, 'wb') as f:
				f.write(html)
			htmls.append(f_name)


		print('------------------------------------------------------------')
		print(htmls)
		pdfkit.from_file(htmls, self.name + ".pdf", options=options)
		for html in htmls:
			os.remove(html)
		total_time = time.time() - start
		print(u"总共耗时：%f 秒" % total_time)


class LiaoxuefengPythonCrawler(Crawler):
	"""
	廖雪峰Python3教程
	"""

	def parse_menu(self, response):
		"""
		解析目录结构,获取所有URL目录列表
		:param response 爬虫返回的response对象
		:return: url生成器
		"""
		soup = BeautifulSoup(response.content, "html.parser")
		menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[3]
		for li in menu_tag.find_all("li"):
			url = li.a.get("href")
			if not url.startswith("http"):
				url = "".join([self.domain, url])  # 补全为全路径
			yield url

	def parse_body(self, response):
		"""
		解析正文
		:param response: 爬虫返回的response对象
		:return: 返回处理后的html文本
		"""
		try:
			soup = BeautifulSoup(response.content, 'html.parser')
			body = soup.find_all(class_="x-wiki-content")[0]

			# 加入标题, 居中显示
			title = soup.find('h4').get_text()
			center_tag = soup.new_tag("center")
			title_tag = soup.new_tag('h1')
			title_tag.string = title
			center_tag.insert(1, title_tag)
			body.insert(1, center_tag)

			html = str(body)
			# body中的img标签的src相对路径的改成绝对路径
			pattern = "(<img .*?src=\")(.*?)(\")"

			def func(m):
				if not m.group(2).startswith("http"):
					rtn = "".join([m.group(1), self.domain, m.group(2), m.group(3)])
					return rtn
				else:
					return "".join([m.group(1), m.group(2), m.group(3)])

			html = re.compile(pattern).sub(func, html)
			html = html_template.format(content=html)
			html = html.encode("utf-8")
			return html
		except Exception as e:
			logging.error("解析错误", exc_info=True)


if __name__ == '__main__':
	start_url = "http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000"
	crawler = LiaoxuefengPythonCrawler("廖雪峰Git", start_url)
	R_SESSION=requests.session()
	crawler.run()
