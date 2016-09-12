#coding:utf-8

#调试模式
DEBUG=True


class EmptyArrayError(Exception):
	def __init__(self,value):
		self.description = "EmptyArrayError"
		self.value = value

	def __str__(self):
		return "%s,%s" %(self.description,self.value)

class EmptyDicError(Exception):
	def __init__(self,value):
		self.description = "EmptyDicError"
		self.value = value

	def __str__(self):
		return "%s,%s" %(self.description,self.value)