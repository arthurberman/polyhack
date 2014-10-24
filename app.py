from flask import Flask, request, render_template
import flask
import os
import json
#import dbc

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():

    return render_template("index.html")
if __name__=="__main__":
    app.run()
