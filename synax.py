#!/usr/bin/env python
#Author:guo
#Create:4/23/2016

import re
OPERATE_WORD = ('create','show','drop','alter','use','insert','delete','update','grant','select','revoke')
TYPE_WORD = ('databases','database','tables','table','index','view','user','int','char','varchar')
LOGICAL_WORD = ('where','frome','in','and','or','not')
DESCRIBE_WORD = ('add','drop','change','modify','default','null','asc','desc','order','by',
	'primary','key','foreign','distinct','all','casecade','set','restrict')
RELATION_WORD = ('>', '>=', '=', '<', '<=')
SEPARATOR = ( '(' ,')' ,',')


def stripSql(str):
	ret = []
	start = 0
	end = 0
	length = len(str)
	while(start < length):
		while re.match('\s',str[start]) is not None: start += 1
		end = start+1
		if str[start] == '`':
			while end < length and str[end] != '`':
				end += 1
			else:
				end +=1
		elif str[start] in ['(',')',',','=',';']:
			pass
		else:			
			while end < length and re.match('\s|\(|\)|,|=|;',str[end]) is None: end += 1		
		ret.append(str[start:end])
		start = end
	return ret



# op:operate
# ty:type
# lo:logical
# de:describe
# id:idertifier

def lexicalAnalysis(str_list):
	ret = ["#"]
	if str_list is not None:
		for i,astr in enumerate( str_list ):
			lower_str = astr
			if astr.isalpha():
				lower_str = astr.lower()
			if  lower_str in OPERATE_WORD:
				ret.append(lower_str)
				str_list[i] = lower_str
			elif lower_str in TYPE_WORD:
				ret.append(lower_str)
				str_list[i] = lower_str
			elif lower_str in LOGICAL_WORD:
				ret.append(lower_str)
				str_list[i] = lower_str
			elif lower_str in DESCRIBE_WORD:
				ret.append( lower_str )
				str_list[i] = lower_str
			elif lower_str in RELATION_WORD:
				ret.append( lower_str )
				str_list[i] = lower_str
			elif astr in SEPARATOR:
				ret.append(astr)
			else:
				astr = astr.strip('`')
				ret.append('id')
				str_list[i] = astr
		ret.append("#")
	return ret

def gramerAnaly(a_list):
	#types = {'databases':createDB,'table',}
	#op = {'create':}
	length = len(a_list)
	ret = []
	if length < 2:
		print "error in input,please input right synay!"
	elif (a_list[0][0] == 'op'):
		if(len >a_list[1][0] == 'type'):
			op = [a_list[0][0],a_list[1],[0]]
			ret.append(op)
		else:
			print "you have a error near ",a_list[1],[1]
	index  = 2
	while (index < length and a_list[index][0] != ';'):
		pass
def tableCode(a_list):
	length = len(a_list)
	ret = []
	ret.append( a_list[0] )

	item = []
	num = 0
	items = []
	for s in a_list[1:]:
		if s == '(':
			num += 1
		elif s == ')':
			num -= 1
			if num == 0:
				items.append(item)
				break
		elif s != ',':
			item.append(s)
		elif s == ',':
			items.append(item)
			item = []
		else:
			print "Error in create table commend!"
	print "item:",items

	for item in items:
		length = len(item)
		cow = [ item[0],item[1] ]
		index  = 3
		at = 2
		if item[1] == "char":
			cow[1]  = item[2]
			at += 1
		if length > 3 and item[at] == "primary" and item[at+1] == "key":
			cow.append('key')
		if length > 3 and item[at] == "not" and item[at+1] == "null":
			cow.append('notNull')
		ret.append(cow)

	print ret ,"ret"
	return ret

def generateCode(a_list):
	ret = []
	if a_list[0] == "create":
		if a_list[1] == "database":
			ret.append("creDatabase")
			ret += a_list[2:]
		if a_list[1] == 'table':
			ret.append("creTable")
			ret += tableCode(a_list[2:])
	elif a_list[0] == "show":
		if a_list[1] == "databases":
			ret.append("shoDatabases")
		if a_list[1] == "tables":
			ret.append("shoTables")
	elif a_list[0] == 'use':
		if a_list[1] == 'database':
			ret.append("useDatabase")
			ret += a_list[2]
	elif a_list[0] == 'drop':
		if a_list[1] == 'database':
			ret.append("droDatabase")
			ret += a_list[2]
		if a_list[1] == 'table':
			ret.append("droTable")
			ret += a_list[2]
		

	return ret


def analyses( str ):
	str_list = stripSql(str)
	ret = lexicalAnalysis(str_list)
	# ret = gramerAnaly(ret)
	# if not ret:
	# 	return False
	print str_list
	ret = generateCode( str_list )
	return ret

if __name__ == '__main__':
	str = '''select (a.name, b.name, ` c .nam`)frome a where a=b;'''
	print lexicalAnalysis(str)
 