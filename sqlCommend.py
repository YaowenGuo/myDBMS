#!/usr/bin/env python
import file
from synax import analyses
from DataBase import DataBase


def createDB( a_list, env ):
	db = DataBase()
	print 'a_list[0]', a_list[0]
	if db.creatDB(a_list[0], env):
		db.save()


def loadDB(db_name ):
	return file.loadDbDic(db_name)

def showDBs( a_list, env):
	db = DataBase()
	dbname_list = db.getAllDB()
	if dbname_list:
		showAsTable(['Databases'],dbname_list)
	else:
		print "There is no databases!"


def showTbl(a_list, env):
	if env:
		user = env['user']
		if user.weight < 0:
			print "You are not login systeam,Please login first!"
			return
		if env['useDatabase']:
			db = env['useDatabase']
			if user.name in db.user or user.weight == 1:
				tables = db.getTables()
				if tables :
					showAsTable(['Table',tables])
				else:
					print "No Table in this database!"
		else:
			print 'Please select a database to use first!'
	else:
		print 'Please select a database to use first!'


def creatTbl(a_list, env):
	if env:
		user = env['user']
		if user.weight < 0:
			print "You are not login systeam,Please login first!"
			return
		if env['useDatabase']:
			db = env['useDatabase']
			db.creatTable( a_list )
		else:
			print 'Please select a database to use first!'
	else:
		print 'Please select a database to use first!'


def useDB(a_list,env):
	user = env['user']
	if user.weight < 0:
		print "You are not login systeam,Please login first!"
		return
	db = loadDB( a_list[0] )
	if not db:
		print "%s database has not bean creat please creat it first!" % a_list[0]
		return
	if user.name in db.user or user.weight == 1:
		env['useDatabase']  = db
		# print "Current use database :",db.name
		# print db.user
		# print db.charset
		# print 'zxcvzx'
	else:
		print "You are not allowed to use this database!"
			

def dropDB(a_list, env):
	return file.dropDB(a_list[0])


opreate = {
'creDatabase':createDB,
'shoDatabases':showDBs,
'shoTables':showTbl,
'creTable':creatTbl,
'useDatabase':useDB,
'droDatabase':dropDB,
'droTable':dropTbl
}


def executeSql( sqlCommend ,env):
	# str_list = stripSql( sqlCommend )
	# if str_list is None:
	# 	return str_list
	# sqlDict = lexicalAnalysis( str_list )
	# if sqlDict is None:
	# 	return None
	# result = gramerAnaly( sqlDict )
	# if not result:
	# 	return None
	# medelCode = changeType( result )
	# if not medelCode:
	# 	return None
	ret = analyses(sqlCommend)
	if not ret:
		print "You have a synax error!"
		return False

	print ret
	opreate[ ret[0] ]( ret[1:], env)
	return True


def showAsTable(title,contain):
	length_list = []
	for str in title:
		length_list.append(len(str))
	for cow in range(len(title)):
		for row in range(len(contain)):
			length = len(contain[row][cow])
			if length_list[cow] < length:
				length_list[cow] = length
	str_line = '+'
	for max_len in length_list:
		str_line += '-'*(max_len+2) + '+'
	print str_line
	for cow in range(len(title)):
		print '|',title[cow].ljust(length_list[cow]),
	print '|'
	print str_line
	for row in range(len(contain)):
		for cow in range(len(title)):
			print '|',contain[row][cow].ljust(length_list[cow]),
		print '|'
	print str_line
