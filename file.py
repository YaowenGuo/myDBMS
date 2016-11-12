#!/usr/bin/env python
import os
import ConfigParser
import pickle

global DA_PATH ; DA_PATH = "./data/"
global DB_PATH ; DB_PATH = "./data/"


def getConfig():
	conf = ConfigParser.ConfigParser()
	conf.read("db_config.ini")
	conf.add_section("database")
	path = os.getcwd()
	path += '/'+'data'
	conf.set("database","path",path)
	DA_PATH = conf.get("database", "path")
	DB_PATH = conf.get("database", "path")



def existsDB(db_name):
	path = DA_PATH + "/" + db_name
	return os.path.exists(path)

def saveDB(database):
	os.makedirs(DB_PATH + database.name)
	dictionary_path = DB_PATH + database.name + '/' + database.name+'.dic'
	print "table_dic_path:",dictionary_path
 	data_dictionary = open( dictionary_path, "wb")
	pickle.dump(database, data_dictionary)
	data_dictionary.close()


def loadDbDic(db_name):
	db = None
	if os.path.exists(DA_PATH+db_name):
		print DA_PATH+db_name
		dic_path = DA_PATH+db_name+'/'+db_name+'.dic'
		if os.path.exists(dic_path) and os.path.isfile(dic_path):
			dic_file = open(dic_path,'rb')
			db = pickle.load(dic_file)
			
			dic_file.close()
			return db

		else:
			print "There is no data dictionary find,May be this dictionary is destroyed!"
			return False
	else:
		print "On such database named",db_name
		return False


def getAllDbName():
	databases = []
	if os.path.exists(DA_PATH):
		for db_name in os.listdir(DA_PATH):
				databases.append([db_name]);
		
	return databases


def printConf():
	print DA_PATH
	print DB_PATH


def existsTbl( db_name, tbl_name ):
	tbl_path  = DA_PATH + db_name + '/' + tbl_path + ".tbl"
	if os.path.exists(tbl_path):
		return True
	else:
		return False


def saveTable(table, db ):
	# print db.name
	# print table.name
	table_dic_path = DA_PATH+db.name+'/'+table.name+'.tbl'
	print "table_dic_path:",table_dic_path
	table_data_path = DA_PATH+db.name+'/'+table.name+'.dat'
 	table_dictionary = open(table_dic_path,"wb")
	pickle.dump(table,table_dictionary)
	table_dictionary.close()
	table_data = open(table_data_path,"w")
	table_data.close()
		

def loadTable(db_name, tbl_name):
	dic_path = DA_PATH + db_name + '/' + tbl_name + ".tbl"
	if os.path.exists( dic_path ):
		print dic_path
		
		dic_file = open(dic_path,'rb')
		table = pickle.load(dic_path)
			
		dic_file.close()
		return Table

	else:
		return False


def dropDB( db_name ):
	db_path = DA_PATH + db_name
	if os.path.exists(db_path):
		if os.path.isfile(path):
			os.remove(path)
		else:
			for file in os.listdir(path):
				os.remove(path+'/'+file)
			os.removedirs(path)
		print "Seccessfully drop!"
	else:
		print "DataBase is not exists!"
		return False