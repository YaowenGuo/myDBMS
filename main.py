#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Author:guo
#
import file
import sys
from user import User
from sqlCommend import executeSql

def getCommend():
	operate = raw_input("guo's SQL>").strip()

	while operate and  not operate.endswith(";"):
		operate += raw_input("        ->")
	operate = operate.split(";")
	return operate

def getUserPwd(alist):
	#get user name and pwd
	argvNum = len(alist)
	for i in range( argvNum ):
		if alist[i] == '-u':
			if i+1 < argvNum:
				user = alist[i+1] 
			else:
				print "Error no user name follow argument -u"
				return False
		if alist[i] == '-p':
			if i+1 < argvNum:
				pwd = alist[i+1]
			else:
				pwd = raw_input('passworld: ')
				# while True:   
				# 	newChar = msvcrt.getch()
			 #        if newChar in '\r\n': # 如果是换行，则输入结束
			 #            print ''
			 #            break
			 #        else:
			 #            pwd.append(newChar)
			 #            sys.stdout.write('*') # 显示为星号
	return (user, pwd)


def main():
	welcomeMsg='''
Welcome use guo's SQL! Version:0.1
Copyright:2016~2017
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
'''	
	conf = file.getConfig()
	#file.printConf()
	user = User()
	if len(sys.argv) >= 4:
		(name,pwd ) = getUserPwd( sys.argv[1:] )
		if not user.login( name, pwd ):
			return -1
	use_database = None
	env = {}
	env['user'] = user
	env['useDatabase'] = None 
	env['db_path'] = ""
	print  welcomeMsg
	exit = True
	while True and exit:
		inputStr = getCommend()
		for str in inputStr:
			if str and str == "exit":
				exit = False
			elif str:
				executeSql( str, env )
	#savedata:
	
	#save database
	return 1


if __name__ == '__main__':
	main()
	

