import pymongo
from pymongo import MongoClient

def connect():
	connection = MongoClient("ds049180.mongolab.com", 49180)
	handle = connection["heroku_app30983762"]
	handle.authenticate("admin", "tuftshack")
	return handle

handle = connect()


def new_group(groupname):
	oid = handle.mygroups.insert({"gname":groupname, "gitems":{}})

def change_items(groupname, items):
	oid = handle.mygroups.update({"gname":groupname}, {"gname":groupname, "gitems":items})

def get_items(groupname):
	group = handle.mygroups.find_one({"gname":groupname})
	return group["gitems"]

def get_all(groupname):
	return handle.mygroups.find_one({"gname":groupname})

def del_group(groupname):
	handle.mygroups.remove({"gname":groupname})

def delete_all():
	handle.mygroups.remove()
