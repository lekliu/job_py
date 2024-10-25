#encoding=utf-8

from db.comm_db import Mysql
import datetime

class JobItem():
    id=0
    jobname=""
    jobtype="openapi"
    jobmain=""
    jobcontent=""
    keyword=""
    #executetime=datetime.datetime.now()
    months=0
    days=1
    hours=0
    minutes=0
    #updatetime=datetime.datetime.now()

    def __init__(self):
        self.temp = 0
