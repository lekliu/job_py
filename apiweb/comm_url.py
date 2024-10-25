# -- coding: utf-8 --
#!/usr/bin/python3

import  urllib3, requests
from urllib3.exceptions import NewConnectionError, ConnectTimeoutError, MaxRetryError,HTTPError,RequestError,ReadTimeoutError,ResponseError
from util.string_tool import MyString

#  忽略警告：InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
requests.packages.urllib3.disable_warnings()

class MyUrl(object):
	def __init__(self):
		self.status = 0
		self.content = ""
		self.mystring = MyString()

	def getUrl(self, url):
		#print(url)
		self.content=""
		# 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
		http = urllib3.PoolManager()
		# 通过request()方法创建一个请求：
		r = http.request('GET', url )
		self.status = r.status
		if r.status== 200:
			html = r.data
			#html = html.replace("\r\n\t\xa0","\r\n\t")
			#html = html.replace("\xa0\r\n","\r\n")
			try:
				html = html.decode('utf-8')     #python3版本中需要加入
			except UnicodeDecodeError as err:
				html = html.hex()
				html = html.replace("0d0a09a0", "0d0a09")
				html = html.replace("a00d0a", "0d0a")
				html = bytes.fromhex(html)
				html = html.decode('utf-8')  # python3版本中需要加入
			self.content = html
			return self.content

	def postUrl(self, url, params):
		#print(url)
		self.content=""
		# 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
		http = urllib3.PoolManager()
		#params = {'name': 'xiaoli', 'age': '1'}
		# 通过request()方法创建一个请求：
		r = http.request('POST', url, fields=params, retries=3)  # retries重试次数：默认为3
		self.status = r.status
		if r.status== 200:
			html = r.data
			try:
				html = html.decode('utf-8')     #python3版本中需要加入
			except UnicodeDecodeError as err:
				html = html.hex()
				html = html.replace("0d0a09a0", "0d0a09")
				html = html.replace("a00d0a", "0d0a")
				html = bytes.fromhex(html)
				html = html.decode('utf-8')  # python3版本中需要加入
			self.content = html
			return self.content

	def getUrlProxy(self, url):
		#print(url)
		self.content=""
		try:
			proxy = urllib3.ProxyManager('http://127.0.0.1:8087/', headers={
				'user-agent': 'Mozilla/5.0 (Darwin; FreeBSD 5.6; en-GB; rv:1.9.1b3pre)Gecko/20081211 K-Meleon/1.5.2'})
			r = proxy.request('GET', url, preload_content=False, retries=2,timeout=urllib3.Timeout(connect=45, read=240))
			self.status = r.status

			if r.status == 200:
				html = r.data
				try:
					html = html.decode('utf-8')  # python3版本中需要加入
				except UnicodeDecodeError as err:
					html = html.hex()
					html = html.replace("0d0a09a0", "0d0a09")
					html = html.replace("a00d0a", "0d0a")
					html = bytes.fromhex(html)
					html = html.decode('utf-8')  # python3版本中需要加入
				self.content = html
		except (NewConnectionError, ConnectTimeoutError, MaxRetryError, HTTPError, RequestError, ReadTimeoutError,
				ResponseError) as error:
			print('Data  failed because : %s' % str(error))
		finally:
			pass
		return self.content