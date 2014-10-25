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
	group = handle.mygroups.find({"gname":groupname})
	oid = handle.mygroups.update(group, {"gname":groupname, "gitems":items})

def get_items(groupname):
	group = handle.mygroups.find({"gname":groupname})
	return group.items

def del_group(groupname):
	group = handle.mygroups.find({"gname":groupname})
	handle.mygroups.remove(group)

def delete_all():
	handle.mygroups.remove()
