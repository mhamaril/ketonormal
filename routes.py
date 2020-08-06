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
        count = labs.get_count()
        total = labs.ave_total()
        ldl = labs.ave_ldl()
        hdl = labs.ave_hdl()
        triglyt = labs.ave_triglyt()
        return render_template("login.html", count=count, total  = round(total, 1), ldl = round(ldl, 1), hdl = round(hdl, 1), triglyt = round(triglyt, 1))

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/mypage")
        else:
            return render_template("error.html",message="Wrong username or password")

@app.route("/mypage", methods=["GET","POST"])
def mypage():
    #if request.method == "GET":
    lab_names = labs.get_labNames()
    return render_template("mypage.html", lab_names = lab_names)

@app.route("/results/<string:lab_name>")
def lab_name(lab_name):
    lab_name = labs.get_values(lab_name)
    return render_template("results.html", lab_name = lab_name)

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

@app.route("/query")
def query():
    return render_template("query.html")

@app.route("/result", methods=["POST"])
def send_values():
    if request.form["sex"] == "1":
        sex = "Male"
    elif request.form["sex"] == "2":
        sex = "Female"
    else:
        sex = "Undisclosed"

    lab_name = request.form["lab_name"]
    user_id = users.user_id()
    age = request.form["age"]
    diet = request.form["diet"]
    hours_fasted = request.form["hours_fasted"]
    crp = request.form["crp"]
    if request.form["units"]=="usa":
        units = "usa"
        total = request.form["total"]
        #total = float(total)*38.67
        ldl = request.form["ldl"]
        #ldl = float(ldl)*38.67
        hdl = request.form["hdl"]
        #hdl = float(hdl)*38.67
        triglyt = request.form["triglyt"]
        #triglyt = float(triglyt)*38.67
    else:
        units = "int"
        total = request.form["total"]
        ldl = request.form["ldl"]
        hdl = request.form["hdl"]
        triglyt = request.form["triglyt"]
    if labs.send_values(lab_name, user_id, sex, age, diet, hours_fasted, units, total, ldl, hdl, triglyt, crp):
        return render_template("result.html", lab_name = lab_name, sex = sex, age = age, diet = diet, hours_fasted = hours_fasted, units = units, total = total, ldl = ldl, hdl = hdl, triglyt = triglyt, crp=crp)
    else:
        return render_template("error.html",message="Something went wrong")
        
@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/send", methods=["post"])
def send():
    content = request.form["content"]
    if messages.send(content):
        list = messages.get_list()
        return render_template("messages.html", count=len(list), messages=list)
    else:
        return render_template("error.html",message="Viestin lähetys ei onnistunut")

@app.route("/new")
def new():
    return render_template("new_query.html", )