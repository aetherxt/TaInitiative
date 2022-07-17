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

@app.route("/aboutus")
@app.route("/aboutus/eng")
def aboutus_eng():
    return render_template("aboutus_eng.html")

@app.route("/aboutus/chi")
def aboutus_chi():
    return render_template("aboutus_chi.html")