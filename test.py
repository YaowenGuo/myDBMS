#!/usr/bin/env python

# from re import split
# from re import search
# str = '''select (a.name, b.name, `  c .nam`)frome a where a=b;'''
# print split('\s\s+|\t|(|)',str.strip())

# print search(r'`[^\s]+`|[\w]+|[(|)]',str).group()

# print ',',None,',','asdfs'
# insert into f (a,c) values (134,'asf');
# use database a;
import string
import os
import pickle
from string import Template
from DataBase import DataBase
from Table import Table
from Item import Item
from synax import stripSql
from user import user




def insertTbl(a_list,table):
	#insert into tbl_name (rowname,rowname2) valuses ( v1,v2);
	count = 0
	items = []
	item = []
	for str in a_list[3:]:
		if str == '(':
			count += 1
		elif str == ')':
			count -= 1
		if str == 'values' or str == ',' or str == ';' or str == '(':
			pass
		elif str == ')' and count  == 0:
			items.append(item)
			item = []
		elif count == 1:
			item.append(str)
		else:
			print 'There is an error in input commend!',str
			return 
	print items
	rows = table.items
	print "length rows ",len(rows)
	if len(items) > len(rows):
		print 'Insert rows cant more than this table',table.name
		return
	rows_val = [None] * len(rows)
	rows_name = [row.name for row in rows ]
	for i,item in enumerate(items[0]):
		if item in rows_name :
			j = rows_name.index(item)
			if rows[j].type == 'int':
			 	if items[1][i].isalnum():
					rows_val[j] = items[1][i]
				else:
					print 'Row %s type is %s,but input error!'% (rows_name[i],'int')
					return
			elif rows[j].type == 'char':
				if items[1][i].startswith("'") and items[1][i].endswith("'"):
					str_temp = items[1][i].strip("'")
					rows_val[j] = items[1][i].strip("'")
				
				else:
					print "%s is not recognize!"% items[1][i]
					return

		else:
			print 'Error,There is no %s in table %s'%(item,table.name)
			return 		
	else:
		print rows_val
		for i in range(len(rows)):
			print rows[i].cannull
			if not rows[i].cannull and  rows_val[i] is None:
				print '%s cant be null'% rows[i].name
				return
		return rows_val
def selectAll(str_list,table_path):
	ret_list = []
	if len(str_list) > 2 and str_list[2] == 'from':
	 	data_file = open(table_path,'r')
	 	for eachline in data_file:
	 		line_list = eachline.strip().split(',')
	 		ret_list.append(line_list)
	 	data_file.close()
	 	return ret_list
	else:
	 	print "Input error! in ", str_list

def drop(path):
	if os.path.exists(path):
		if os.path.isfile(path):
			os.remove(path)
		else:
			for file in os.listdir(path):
				os.remove(path+'/'+file)
			os.removedirs(path)
		print "Seccessfully drop!"
	else:
		print "Data file is not exists!"




def loadTbl(db_name):
	if os.path.exists(DA_PATH+db_name):
		print DA_PATH+db_name
		database = DataBase()
		for file_name in os.listdir(DA_PATH+db_name):
			database.name = db_name
			file_path = DA_PATH+db_name+'/'+file_name
			if file_name.endswith('.dic') and os.path.isfile(file_path):
				table_dic =  open(file_path,'rb')
				#with open('test.bin', 'rb') as fp:
				#	p = pickle.load(fp)
    			#	print p
				table = pickle.load(table_dic)#--------------------------load file
				database.tables.append(table)
	return database

	db_config_file = open(DB_PATH+'/'+db_name+'.conf','wb')

CREAT = {'database':creatDB,'table':creatTbl}
if __name__ == '__main__'://///////////////////////////////////////////////////////////////
	
	
	while 'q;' != inputStr:

		if(str_list[0] == 'create'):
			
		elif str_list[0] == 'insert':		
			if str_list[1] == 'into':
				if use_database is None:
					print "please select which database to contain this table!"
				else:
					rows_val = None
					for i,name in enumerate([table.name for table in use_database.tables]):
						if name == str_list[2] :
							table = use_database.tables[i]
							rows_val = insertTbl(str_list,use_database.tables[i])
							if rows_val is not None:
								str = ""
								for item in rows_val:
									if item is None:
										item = ""
									str += item +','
								str = str[0:-1]
								table_data_path = DA_PATH+use_database.name+'/'+table.name+'.dat'
								table_data = open(table_data_path,"aw")
								table_data.write(str+'\n')
								table_data.close()

							break
					else:
						print "No table %s in %s database"%(str_list[2],use_database.name)

		elif str_list[0] == 'select':
			if str_list[1] == '*':
				if use_database is None:
					print "please select which database to select this table!"
				else:
					rows_val = None
					tables_name = [table.name for table in use_database.tables]
					if str_list[3] in tables_name:
						index = tables_name.index(str_list[3])
						table = use_database.tables[index]
						title = [row.name for row in table.items]
						table_path = DA_PATH+use_database.name+'/'+str_list[3]+'.dat'
						table = selectAll(str_list,table_path)
						if table != [] or table is not None:
							print title
							showAsTable(title,table)



		
 		elif str_list[0] == 'drop':
 			if(str_list[1] == 'database'):
 				if str_list[2] in data_bases:
 					dir_path = DA_PATH+str_list[2];
 					drop(dir_path)
 					data_bases.remove(str_list[2])
 				else:
 					print "No databasse %s" % str_list[2]
 			elif str_list[1] == 'table':
 				if use_database is None:
					print "please select which database to select this table!"
				else:
					rows_val = None
					tables_name = [table.name for table in use_database.tables]
					if str_list[2] in tables_name:
						index = tables_name.index(str_list[2])
						table = use_database.tables[index]
						table_path = DA_PATH+use_database.name+'/'+table.name
						print table_path+'.dat'
						print table_path+'.dic'
						drop(table_path+'.dat')
						drop(table_path+'.dic')
						del use_database.tables[index]
					else:
						print "No table %s!" % str_list[2]
							print DA_PATH+db_name
			database = DataBase()
			for file_name in os.listdir(DA_PATH+db_name):
				database.name = db_name
				file_path = DA_PATH+db_name+'/'+file_name
				if file_name.endswith('.dic') and os.path.isfile(file_path):
					table_dic =  open(file_path,'rb')
					#with open('test.bin', 'rb') as fp:
					#	p = pickle.load(fp)
	    			#	print p
					table = pickle.load(table_dic)#--------------------------load file
					database.tables.append(table)
		return database
		inputStr = getCommend()

a = ['sdf',[123,'asdfas'],None,241]
fp = open('testoutput.txt','w')
fp.write(str(a))
fp.close()
s = str(a)

b = list(s)
print b