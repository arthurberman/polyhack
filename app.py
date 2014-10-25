from flask import Flask, request, render_template, redirect, url_for, send_from_directory, session, make_response
from werkzeug import secure_filename
import flask
import os
import json
import mongo
import requests
import urllib2, urllib
import base64
#import dbc

ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
mongo.connect()
app.config['UPLOAD_FOLDER'] = "uploads"
app.secret_key = "ThomasWroteSOMETHINGCOOL"
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
@app.route('/', methods = ["GET", "POST"])
def index():
    return render_template("index.html")
@app.route('/butts')
def butts():
    return open("static/butts.html").read()

def makeList(filename):
    """call ThomasAPI using the image described by filename"""
    page = "https://doctorwho.noip.me/tcolgr01/test.php"
    data = {"name":"uploadedFile"}
    files = {'uploadFile':open("uploads/"+filename)}
    response = requests.post(page, data=data, files=files, verify=False)
    return response.content 

@app.route('/image', methods = ["GET", "POST"])
def image():
    """GET: get the upload page. POST: redirect to the check page"""
    if request.method == "POST":
        f = request.files['uploadFile']
        if f and allowed_file(f.filename):
            filename = request.cookies['code']+"."+f.filename.split(".")[1]
            f.save("uploads/"+filename)

            ls = makeList(filename)
            print ls
            ls = '{"thing":'+ls+"}"
            print ls
            ls = json.loads(ls)
            ls =  ls["thing"]
            ls = map(lambda x: {"name":x[0], "price":x[1], "claimed":False},ls)

            mongo.change_items(request.cookies['code'], ls)
            return redirect("check/"+request.cookies['code'])

    return render_template("uploadimage.html") 
@app.route('/newcheck')
def newcheck():
    """return the new check page"""
    return render_template("newcheck.html")

@app.route('/create', methods = ["GET", "POST"])
def create():
    """create a new group"""
    if request.method == "POST":
        response = make_response(redirect("image"))
        response.set_cookie('code', request.form['code'])
        mongo.new_group(request.form['code'])
        return response
    return render_template(create)
@app.route('/login', methods = ["GET", "POST"])
def login():
    """join an existing group"""
    if request.method == "POST":
        response = make_response(redirect("/check/"+request.form["code"]))
        response.set_cookie('code', request.form['code'])
        return response
    else:
        pass
    return render_template("login.html")
@app.route('/check/<code>')
def check(code):
    """see the current check"""
    return render_template("check.html",  items=mongo.get_items(code))
if __name__=="__main__":
    app.run(debug=True)
