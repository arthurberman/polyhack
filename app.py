from flask import Flask, request, render_template, redirect, url_for, send_from_directory, session, make_response
from werkzeug import secure_filename
import flask
import os
import json
import mongo
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
def makeList(filename):
    return [{"name":"Gene Gau's Chicken", "price":9.89, "claimed":True}, {"name":"Spare Ribs", "price":5.68, "claimed":False}]
@app.route('/image', methods = ["GET", "POST"])
def image():
    if request.method == "POST":
        f = request.files['file']
        if f and allowed_file(f.filename):
            filename = request.cookies['code']+"."+f.filename.split(".")[1]
            f.save("uploads/"+filename)
            ls = makeList(filename)
            mongo.change_items(request.cookies['code'], ls)
            return redirect("check/"+request.cookies['code'])

    return  '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form action="" method=post enctype=multipart/form-data>
              <p><input type=file name=file>
                 <input type=submit value=Upload>
            </form>
            '''
@app.route('/newcheck')
def newcheck():
    return render_template("newcheck.html")
@app.route('/create', methods = ["GET", "POST"])
def create():
    if request.method == "POST":
        response = make_response(redirect("image"))
        response.set_cookie('code', request.form['code'])
        mongo.new_group(request.form['code'])
        return response
    return render_template(create)
@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        response = make_response(redirect("/check/"+request.form["code"]))
        response.set_cookie('code', request.form['code'])
        return response
    else:
        pass
    return render_template("login.html")
@app.route('/check/<code>')
def check(code):
    return render_template("check.html",  items=mongo.get_items(code))
def getItems(cookie):
    return [{"name":"General Gau's Chicken", "price":9.89, "claimed":True}, {"name":"Spare Ribs", "price":5.68, "claimed":False}]
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
if __name__=="__main__":
    app.run(debug=True)
