#encoding=utf-8
import time

from db.job_db import MyJob
from item.job_item import JobItem
from apiweb.job_apiweb import  JobWebApi

class JobService(object):
    def __init__(self):
        self.myJob = MyJob()
        self.jobWebApi = JobWebApi()

    def getOneJob(self):
        return self.myJob.getOneItem()

    def excuteJob(self, job:JobItem):
        if(job.jobtype=="openapi"):
            self.excuteOpenApiJob(job)
        elif(job.jobtype=="java"):
            self.excuteJavaJob(job)
        elif(job.jobtype=="python"):
            self.excutePythonJob(job)

    def excuteOpenApiJob(self, job:JobItem):
        pageContent = self.jobWebApi.postUrl(job)
        keyword = job.keyword
        i=0
        while(keyword!="" and pageContent!=None):
            pos = pageContent.find(keyword)
            print(pageContent)
            print(keyword)
            print(pos)
            if pos >= 0:
                time.sleep(2) #休息1秒钟
                i=i+1
                if(i>20): #一次执行20次
                    break
                pageContent = self.jobWebApi.postUrl(job)
            else:
                keyword="" #任务完成，结束退出循环

        if (keyword==""):
            self.myJob.setNextTime(job) #任务全部完成后，才设置下一次执行时间
        self.myJob.setUpdateTime(job)

    def excuteJavaJob(self, job:JobItem):
        print(job.jobname)

    def excutePythonJob(self, job:JobItem):
        print(job.jobname)
