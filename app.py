from flask import Flask, request, render_template, redirect, url_for, send_from_directory, session, make_response
from werkzeug import secure_filename
import flask
import os
import json
#import dbc

ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"
app.secret_key = "ThomasWroteSOMETHINGCOOL"
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
@app.route('/', methods = ["GET", "POST"])
def index():
    return render_template("index.html")
@app.route('/image', methods = ["GET", "POST"])
def image():
    if request.method == "POST":
        f = request.files['file']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save("uploads/"+filename)
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    return  '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form action="" method=post enctype=multipart/form-data>
              <p><input type=file name=file>
                 <input type=submit value=Upload>
            </form>
            '''
@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session['code'] = request.form['code']
        response = make_response(redirect("/check"))
        response.set_cookie('code', session['code'])
        return response
    else:
        pass
    return render_template("login.html")
@app.route('/check')
def check():
    return render_template("check.html",  items=getItems(request.cookies["code"]))
def getItems(cookie):
    return [cookie]
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__=="__main__":
    app.run(debug=True)