#coding:utf-8
import sys
import os
import datetime
import logging
import subprocess

from config import DEBUG

def ConfigLog(logfileName):
    #日志输出到文件
    dirPath = _GetCurrentDIR()
    today = datetime.date.today()
    logName = "%s\log\%s_%s" %(dirPath, today, logfileName)
    logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename=logName,filemode='a')
    
    #如果是调试模式，则输出到console
    if(DEBUG == True):
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(name)-8s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    logging.info("------------logging-----------")

def DeleteLog():
    #删除7天前的日志 
    dirPath = _GetCurrentDIR()
    dayWeekAgo = GetDayWeekAgo1()
    shell = "rm -f %s\log\%s*" %(dirPath,dayWeekAgo)
    subprocess.Popen(shell,stdout=subprocess.PIPE,shell=True)
    logging.info(shell)

    
def WriteLineToFile(fileName,line):
    dirPath = _GetCurrentDIR()
    filePath = "%s\log\%s" %(dirPath,fileName)
    f = open(filePath,"a")
    f.write(line.encode("utf-8") + "\n")
    f.close()


def GetYestoday():       
    today = datetime.date.today()
    yestoday = today - datetime.timedelta(days = 1)
    yestoday = yestoday.strftime("%Y%m%d")
    return yestoday


def GetYestoday1():
    today = datetime.date.today()
    yestoday = today - datetime.timedelta(days = 1)
    yestoday = yestoday.strftime("%Y-%m-%d")
    return yestoday

def GetYestoday2():
    today = datetime.date.today()
    yestoday = today - datetime.timedelta(days = 1)
    yestoday = yestoday.strftime("%Y%m%d%H%M%S")
    return yestoday


def GetYestoday3():
    today = datetime.date.today()
    yestoday = today - datetime.timedelta(days = 1)
    yestoday = yestoday.strftime("%Y-%m-%d %H:%M:%S")
    return yestoday

def GetTwodayAgo():
    today = datetime.date.today()
    twodayAgo = today - datetime.timedelta(days = 2)
    twodayAgo = twodayAgo.strftime("%Y%m%d")
    return twodayAgo

def GetThreedayAgo():
    today = datetime.date.today()
    threedayAgo = today - datetime.timedelta(days = 3)
    threedayAgo = threedayAgo.strftime("%Y%m%d")
    return threedayAgo

def GetFourdayAgo():
    today = datetime.date.today()
    fourdayAgo = today - datetime.timedelta(days = 4)
    fourdayAgo = fourdayAgo.strftime("%Y%m%d")
    return fourdayAgo

def GetFivedayAgo():
    today = datetime.date.today()
    fivedayAgo = today - datetime.timedelta(days = 5)
    fivedayAgo = fivedayAgo.strftime("%Y%m%d")
    return fivedayAgo

def GetSixdayAgo():
    today = datetime.date.today()
    sixdayAgo = today - datetime.timedelta(days = 6)
    sixdayAgo = sixdayAgo.strftime("%Y%m%d")
    return sixdayAgo

def GetSevendayAgo():
    today = datetime.date.today()
    sevendayAgo = today - datetime.timedelta(days = 7)
    sevendayAgo = sevendayAgo.strftime("%Y%m%d")
    return sevendayAgo

def GetDayMonthAgo():
    today = datetime.date.today()
    dayMonthAgo = today - datetime.timedelta(days = 28)
    dayMonthAgo = dayMonthAgo.strftime("%Y%m%d")
    return dayMonthAgo

def GetDayWeekAgo():
    today = datetime.date.today()
    dayWeekAgo = today - datetime.timedelta(days = 7)
    dayWeekAgo = dayWeekAgo.strftime("%Y%m%d")
    return dayWeekAgo

def GetDayWeekAgo1():
    today = datetime.date.today()
    dayWeekAgo = today - datetime.timedelta(days = 7)
    dayWeekAgo = dayWeekAgo.strftime("%Y-%m-%d")
    return dayWeekAgo

def ReplaceDatetime(sqlString):
    retString = None
    retString = sqlString.replace("$yestoday",GetYestoday())
    retString = retString.replace("$yestoday1",GetYestoday1())
    retString = retString.replace("$yestoday2",GetYestoday2())
    retString = retString.replace("$yestoday3",GetYestoday3())
    retString = retString.replace("$dayMonthAgo",GetDayMonthAgo())
    retString = retString.replace("$dayWeekAgo",GetDayWeekAgo())
    retString = retString.replace("$dayWeekAgo1",GetDayWeekAgo1())
    retString = retString.replace("$twodayAgo",GetTwodayAgo())
    retString = retString.replace("$threedayAgo",GetThreedayAgo())
    retString = retString.replace("$fourdayAgo",GetFourdayAgo())
    retString = retString.replace("$fivedayAgo",GetFivedayAgo())
    retString = retString.replace("$sixdayAgo",GetSixdayAgo())
    retString = retString.replace("$sevendayAgo",GetSevendayAgo())
    return retString
    

def _GetCurrentDIR():
        #获取当前路径
    path = sys.path[0]
    
    #脚本还是py2exe编译的exe
    if os.path.isdir(path):
        return path
    if os.path.isfile(path):
        return os.path.dirname(dir)

def GetCurrentDIR():
        #获取当前路径
    path = sys.path[0]
    
    #脚本还是py2exe编译的exe
    if os.path.isdir(path):
        return path
    if os.path.isfile(path):
        return os.path.dirname(dir)


if __name__ == "__main__":
    ConfigLog(".log")
    DeleteLog()