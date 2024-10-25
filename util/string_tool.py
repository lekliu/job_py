# -- coding: utf-8 --
#!/usr/bin/python3

class MyString(object):
	strAll = ""
	def leftString(self, strAll , strSub): 
		pos = strAll.find(strSub)
		if pos>=0:			
			return strAll[0:pos]
		else:
			return ""

	def rightString(self, strAll , strSub):
		pos = strAll.find(strSub)
		if pos>=0:
			return strAll [pos+len(strSub):]
		else:
			return ""

	def midString(self, strAll , strSub1, strSub2):
		pos = strAll.find(strSub1)
		if pos>=0:
			strAll = strAll [pos+len(strSub1):]
			pos = strAll .find(strSub2)
			if pos>=0:
				self.strAll = strAll [pos+len(strSub2):]
				return strAll [0:pos]
			else:
				self.strAll  = ""
				return ""
		else:
			self.strAll  = ""
			return ""
		
	def getNumberAndDot(self, strAll):
		str = "0123456789."
		strR =""
		for c in strAll:
			if str.find(c)>=0:
				if len(self.rightString(strR,"."))<2: # 保留两位小数
					strR = strR + c			
		else:
			return strR

	def delNoShowChar(self, strAll):
		return strAll.replace('\r','').replace('\n','').replace('\t','')

	def countSubStr(self, strAll, subStr):
		return strAll.count(subStr)  # 统计指定的字符串出现的次数

	def addZero(self, str, length):
		return str.zfill(length )  # 获取固定长度，右对齐，左边不足用0补齐
