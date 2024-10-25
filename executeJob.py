#encoding=utf-8

import gc
import sys;
import time
# import ssl
from item.job_item import JobItem

from service.job_sercive import JobService

#from db.crawl_db import MyCrawl
#from url.crawl_url import UrlCrawl
#from util.string_tool import MyString


# ssl._create_default_https_context = ssl._create_unverified_context
#mycrawl = MyCrawl()
#mystring = MyString()
class ExcuteJob(object):
	isProxy = False  # True / False
	def __init__(self):
		self.jobService = JobService()

	def run(self):
		iduck = 1;
		while iduck<50005:
			job = self.jobService.getOneJob()
			if (job==None):
				print("没有任务了...")
				time.sleep(30)
			else:
				self.jobService.excuteJob(job)
				print (iduck)
			if iduck > 50000:
				gc.collect() # 对象销毁
				self.jobService = JobService()
				iduck = 1
			time.sleep(5)
			iduck = iduck + 1
