#!/usr/bin/env python
import sys

def main(argv):
	print sys.argv
	print len(sys.argv)

if __name__ == '__main__':
	main( sys.argv )

def loadDB():
	databases = {}
	if os.path.exists(DA_PATH):
		for db_name in os.listdir(DA_PATH):
			databases[db_name] = None;
		else:
			return databases
	else:
		return {}
	def getAllDB(data_bases):
		if data_bases is not None:
			title = []
			contain = []
			title.append("Database")
			contain = [[db_name] for db_name in data_bases.keys()]
			return (title,contain)
		else:
			return (None,None)
		
def showDB(databases):
	max_len = len('Database')
	db_name_len = 0
	if data_bases:
		for db_name in databases.keys():
			db_name_len = len(db_name)
			if max_len < db_name_len:
				max_len = db_name_len

		str_line = '+' + '-'*(max_len+2) +'+'
		print str_line
		print '|','Database'.ljust(max_len), '|'
		print str_line
		for db_name in databases.keys():
			print '|',db_name.ljust(max_len), '|'
		print str_line
	else:
		print "No database creat,Please cerat database first!"


create table d ( a int primary key,b char(20) not null,c char(30) );

		elif str_list[0] == 'show':
			title = []
			conatin = []
			
			elif str_list[1] == 'tables':
				if use_database is None:
					print "please select which database to select this table!"
				else:
					rows_val = None
					tables_name = [[table.name] for table in use_database.tables]
					title = ['Table']
					showAsTable(title,tables_name)