# -- coding: utf-8 --
#!/usr/bin/python3

from  apiweb.comm_url import MyUrl
from item.job_item import JobItem
import json

class JobWebApi(MyUrl):
	def __init__(self):
		MyUrl.__init__(self)

	def postUrl(self, job:JobItem):
		url = job.jobmain
		#print(job.jobcontent)
		params = json.loads(job.jobcontent)
		#print(params)
		return MyUrl.postUrl(self, url, params)

