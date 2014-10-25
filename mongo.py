import pymongo
from pymongo import MongoClient
import flask
from flask import Flask, render_template, request, redirect
import os

def connect():
	connection = MongoClient("ds049180.mongolab.com", 49180)
	handle = connection["heroku_app30983762"]
	handle.authenticate("admin", "tuftshack")
	return handle

app = Flask(__name__)
handle = connect()

@app.route("/index" , methods=['GET'])
@app.route("/", methods=['GET'])
def index():
	data = [x for x in handle.mygroups.find()]
	return render_template('index.html', database=data)

def new_group(groupname):
	oid = handle.mygroups.insert({"gname":groupname, "gitems":{}})

def change_items(groupname, items):
	group = db.mygroups.find({"gname":groupname})
	oid = handle.mygroups.update(group, {"gname":groupname, "gitems":items})

def get_items(groupname):
	group = db.mygroups.find({"gname":groupname})
	return group.items

def del_group(groupname):
	group = db.mygroups.find({"gname":groupname})
	db.mygroups.remove(group)

def delete_all():
	handle.mygroups.remove()

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))

	app.run(host='0.0.0.0', port=port, debug=True)
