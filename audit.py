#coding:utf-8
import StringIO
import urllib
import sys
import math
import time

from config import *
from _common import *

def main():
	dirPath = GetCurrentDIR()
	serverFile = "%s/%s" %(dirPath, "server.txt")
	userFile = "%s/%s" %(dirPath, "name.txt")
	passwd = "tx@vpn@321"
	f1 = open(serverFile)
	f2 = open(userFile)
	for ip in f1:
		for user in f2:
			try:
				ret = SshClient(ip,user,passwd)
				if(ret==True):
					WriteLineToFile("weakpasswd.txt","%s,%s,%s"%(ip,user,passwd))
			except:
				continue
if __name__ == '__main__':
    #配置日志
    ConfigLog(".log")
    DeleteLog()
    main()