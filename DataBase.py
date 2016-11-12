#!/usr/bin/env python
import file
from string import Template
from Table import Table
from Item import Item


class DataBase(object):
	"""docstring for DataBase
	using for descrabe a database,include it's tables"""
	def __init__(self):
		super(DataBase, self).__init__()
		#dataBase = {'user':'root','charset':'UTF-8','db_name':None.Table}
		self.user = []
		self.charset = 'UTF-8'
		self.name = ''
		self.tables = []
		self.path = ''
	

	def creatDB(self, db_name, env):
		#['creDatabase', 'id']
		db_exist_error_msg = Template('database name ${db_name} has bean used,'
			'please select another name as your database')
		user = env['user']
		if db_name and user.weight > 0:
			if file.existsDB( db_name ):
				print "This database have exists,Please select another name!"
				return
			self.user.append(env["user"])
			self.name = db_name
			self.path = env["db_path"]
			return True
		else:
			print "Did not generate database,you are not login or don't have enough weight!"
			return False


	def save(self):
		file.saveDB(self)



	def getAllDB(self):
		return file.getAllDbName()
	

	def creatTable(self,a_list):
		if file.existsTbl(self.name, a_list[0]):
			print "Table named %s have exists,please select another table name!" % a_list[0]
		table = Table()
		table.name = a_list[0]
		for cow in a_list[1:]:
			item = Item()
			item.name = cow[0]
			if cow[1] == 'int':
				item.type  = cow[1]
			else:
				item.type = 'char'
				item.length = cow[1]
			if len(cow) > 2:
				if cow[2] == 'key':
					item.iskey = True
					item.cannull = False
				if cow[2] == 'notNull':
					item.cannull = False
			table.items.append(item)
		file.saveTable(table,self)
		self.tables.append(table.name)


	def getTables(self):
		return self.tables


	def loadTable(self,tbl_name ):

		if file.existsTbl(self.name, tbl_name):
			return file.loadTable(self.name, tbl_name)
		else:
			print "There is no table is nameed %s,Plese ensure you write and try again!"
			return  
