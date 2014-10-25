# Database Implimentation

import pymongo
from pymongo import MongoClient

#connection to check-mates's mongodb database
def connect():
	connection = MongoClient("ds049180.mongolab.com", 49180)
	handle = connection["heroku_app30983762"]
	handle.authenticate("admin", "tuftshack")
	return handle

#check-mates's database
handle = connect()

#make a group
def new_group(groupname):
	oid = handle.mygroups.insert({"gname":groupname, "gitems":{}})

#add/change items in list
def change_items(groupname, items):
	oid = handle.mygroups.update({"gname":groupname}, {"gname":groupname, "gitems":items})

#get items in list
def get_items(groupname):
	group = handle.mygroups.find_one({"gname":groupname})
	return group["gitems"]

#get all items in list (not used by client)
def get_all(groupname):
	return handle.mygroups.find_one({"gname":groupname})

#delete a group
def del_group(groupname):
	handle.mygroups.remove({"gname":groupname})

#clear database (not used by client)
def delete_all():
	handle.mygroups.remove()
