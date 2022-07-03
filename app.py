from flask import Flask, render_template, request, session, url_for, redirect, make_response, jsonify
from db import *

app = Flask(__name__)
app.secret_key = "test"

@app.route("/")
@app.route("/en")
@app.route("/home/eng")
def home_eng():
    return render_template("home_eng.html")

@app.route("/chi")
@app.route("/home/chi")
def home_chi():
    return render_template("home_chi.html")