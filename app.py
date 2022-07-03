from flask import Flask, render_template, request, session, url_for, redirect, make_response, jsonify
from db import *

app = Flask(__name__)
app.secret_key = "test"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")