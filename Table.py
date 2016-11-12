#!/usr/bin/env python

class Table(object):
	"""docstring for Table"""
	def __init__(self):
		super(Table, self).__init__()
		self.name = ''
		self.items = []		#contain all cows as cow_name:cow_object ...
		self.keys = ()		#contain all main key
		self.forKey = {}		#contain a foreign key like foreign_key_name:


