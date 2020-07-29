from app import app
from flask import render_template, request, redirect
import labs, users, messages
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
            return render_template("error.html",message="Wrong username or password")

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
            return redirect("/mypage")
        else:
            return render_template("error.html",message="Something went wrong, try again")

@app.route("/submitlabs")
def submit():
    return render_template("submitlabs.html")

@app.route("/result", methods=["POST"])
def send_values():
    if request.form["sex"] == 1:
        sex = "Male"
    elif request.form["sex"] == 2:
        sex = "Female"
    else:
        sex = "Undisclosed"

    lab_name = request.form["lab_name"]
    
    age = request.form["age"]
    diet = request.form["diet"]
    hours = request.form["hours"]
    if request.form["units"]=="usa":
        units = "usa"
        total = request.form["total"]
        total = float(total)/38.67
        ldl = request.form["ldl"]
        ldl = float(ldl)/38.67
        hdl = request.form["hdl"]
        hdl = float(hdl)/38.67
        trigly = request.form["trigly"]
        trigly = float(trigly)/38.67
    else:
        units = "int"
        total = request.form["total"]
        ldl = request.form["ldl"]
        hdl = request.form["hdl"]
        trigly = request.form["trigly"]
    return render_template("result.html", lab_name = lab_name, sex = sex, age = age, diet = diet, hours = hours, units = units, total = total, ldl = ldl, hdl = hdl, trigly = trigly)
 
@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/messages", methods=["post"])
def send():
    content = request.form["content"]
    if messages.send(content):
        return redirect("/messages.html")
    else:
        return render_template("error.html",message="Viestin lähetys ei onnistunut")

@app.route("/new")
def new():
    return render_template("new.html")