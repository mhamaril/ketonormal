from app import app
from flask import render_template, request, redirect
import labs, users
from db import db

@app.route("/")
def index():
    
    return redirect("login")

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        #result = db.session.execute("SELECT COUNT(*) FROM labvalues")
        #count = result.fetchone()[0]  , labvalues = labvalues
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/mypage")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")

@app.route("/mypage")
def mypage():
    return render_template("mypage.html")
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/login")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")

@app.route("/submitlabs")
def submit():
    return render_template("submitlabs.html")

@app.route("/result", methods=["POST"])
def result():
    lab_name = request.form["lab_name"]
    sex = request.form["sex"]
    age = request.form["age"]
    diet = request.form["diet"]
    hours = request.form["hours"]
    units = request.form["units"]
    total = request.form["total"]
    ldl = request.form["ldl"]
    hdl = request.form["hdl"]
    trigly = request.form["trigly"]
    return render_template("result.html", sex = sex, age = age, diet = diet, hours = hours, units = units, total = total, ldl = ldl, Hdl = hdl, trigly = trigly)
 
@app.route("/info")
def info():
    return render_template("info.html")