#!/usr/bin/env python

class User(object):
	"""use to descrabe peaple who use this DBMS"""
	def __init__(self):
		super(User, self).__init__()
		self.name = ''
		self.pwd = ''
		self.weight = -1;


	def login(self, name, pwd):
		self.name = 'root'
		self.pwd = 'root'
		self.weight = 1
		# if haveUser(name):
		# 	(userpwd ,weight) = executeSql("select pwd from user where name = "+ name)

		# 	if pwd != userpwd:
		# 		print "Your passworld is not right! please input again"
		# 		return False
		# 	else:
		# 		self.name = name
		# 		self.pwd = pwd
		# 		self.weight = weight
		# 		return True
		# else:
		# 	if name == "root" and pwd == "root":
		# 		pass
		# 	else:
		# 		print "No user "+name + ",Please ensure your user name is right!"
		return True


	def haveUser(name):
		have = selSelect("select name from user where name = " + name)
		if have is None:
			return False
		else:
			return True
	def updateUser( item, value):
		executeSql("update user " + item + "" + value)
		
	

if __name__ == '__main__':
	"""test User"""
	

		
		