#encoding=utf-8
import logging

import pymysql
 
class Mysql(object):
	def __init__(self):
		self.conn = pymysql.connect(
	        host = "localhost", # 192.168.0.118   localhost
	        port = 3306,
	        user = "root2",
	        passwd = "root258",
	        db = "dbstock",
	        charset = "utf8")
		self.conn.autocommit(True)

	def get_cursor(self):
		return self.conn.cursor()
	
	def query(self, sql):
		cursor = self.get_cursor()
		try:
			cursor.execute(sql, None)
			result = cursor.fetchall()
		except Exception as e:
			logging.error("python: mysql query error: %s", e)
			cursor.close()
			return ()
		finally:
			cursor.close()
		return result

	def queryone(self, sql):
		cursor = self.get_cursor()
		try:
			cursor.execute(sql, None)
			result = cursor.fetchone()
		except Exception as e:
			logging.error("python: mysql query error: %s", e)
			cursor.close()
			return None
		finally:
			cursor.close()
		return result
	
	def execute(self, sql, param=None):
		cursor = self.get_cursor()
		try:
			cursor.execute(sql, param)
			self.conn.commit()
			affected_row = cursor.rowcount
		except Exception as  e:
			logging.error("python: mysql execute error: %s", e)
			cursor.close()
			return 0
		finally:
			cursor.close()
		return affected_row
	
	def executemany(self, sql, params=None):
		cursor = self.get_cursor()
		try:
			cursor.executemany(sql, params)
			self.conn.commit()
			affected_rows = cursor.rowcount
		except Exception as e:
			logging.error("python: mysql executemany error: %s", e)
			cursor.close()
			return 0
		finally:
			cursor.close()
		return affected_rows
	
	def close(self):
		try:
			self.conn.close()
		except:
			pass
	
	def __del__(self):
		self.close()


	def query_records(self,tbname,tbfields,condition):
		# tbfields format: fields1,fields2,fields3,fields4...
		# SQL 查询语句
		sql = "SELECT %s FROM %s  WHERE  %s" % (tbfields,tbname,condition)
		return self.query(sql)

	def query_one_records(self,tbname,tbfields,condition):
		# tbfields format: fields1,fields2,fields3,fields4...
		# SQL 查询语句
		sql = "SELECT %s FROM %s  WHERE  %s" % (tbfields,tbname,condition)
		return self.queryone(sql)
