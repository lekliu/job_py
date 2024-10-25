#encoding=utf-8

from db.comm_db import Mysql
from item.job_item import JobItem

class MyJob(Mysql):
    #para = MyPara()
    def __init__(self):
        Mysql.__init__(self)

    def getOneItem(self):
        jobItem = JobItem()
        table= "tbjob"
        fields = "id,jobname,jobtype,jobmain,jobcontent,keyword,months,days,hours,minutes"
        contition = "executetime<now() order by executetime limit 1"
        result = self.query_one_records(table, fields, contition)
        if(result==None):
            return None
        else:
            jobItem.id=result[0]
            jobItem.jobname=result[1]
            jobItem.jobtype=result[2]
            jobItem.jobmain=result[3]
            jobItem.jobcontent=result[4]
            jobItem.keyword=result[5]
            jobItem.months=result[6]
            jobItem.days=result[7]
            jobItem.hours=result[8]
            jobItem.minutes=result[9]
            return jobItem

    def setNextTime(self,job:JobItem):
        months = job.months
        days = job.days
        hours = job.hours
        minutes = job.minutes
        if(months==0 and days==0 and hours==0 and minutes==0):
            self.deleteJob(job)
        else:
            sql="UPDATE `tbjob` SET executetime=date_add(date_add(date_add(date_add(executetime, "\
                +" interval "+ str(job.minutes) +" minute), "\
                +" interval "+ str(job.hours) +" hour), "\
                +" interval "+ str(job.days) +" day), "\
                +" interval "+ str(job.months) +" month) WHERE `id`=" + str(job.id)
            self.execute(sql)

    def deleteJob(self,job:JobItem):
        sql="DELETE FROM `tbjob` WHERE id=" + str(job.id)
        self.execute(sql)

    def setUpdateTime(self,job:JobItem):
        sql="UPDATE `tbjob` SET updatetime=now() WHERE id=" + str(job.id)
        self.execute(sql)
