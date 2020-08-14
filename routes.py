from app import app
from flask import render_template, request, redirect
import labs, users, messages
from db import db
import os
from flask import send_from_directory


@app.route("/")
def index():
    
    return render_template("login.html")

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        averages = labs.get_averages()
        return render_template("login.html", averages=averages)

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/mypage")
        else:
            return render_template("error.html",message="Wrong username or password")

@app.route("/mypage")
def mypage():  
    user_id = users.user_id()
    lab_names = labs.get_lab_names(user_id)
    lista = messages.get_limited_list()
    table = labs.read_table()
    return render_template("mypage.html", lab_names = lab_names, messages = lista, table = table)
 
@app.route("/results/<int:id>")
def lab_name(id):
    lab_name = labs.get_values(id)
    return render_template("results.html", lab_name = lab_name)

@app.route("/topic/<int:id>")
def topic(id):
    topic = messages.get_messages(id)
    return render_template("topic.html", topic = topic)


@app.route("/query")
def query():
    return render_template("query.html")

@app.route("/query_result", methods=["POST"])
def get_query_total():
    sex = request.form["sex"]
    age = request.form["age"]
    diet = request.form["diet"]
    hours_fasted = request.form["hours_fasted"]
    crp = request.form["crp"]
    units = request.form["units"]
    tulos = labs.get_query_total(sex, age, diet, hours_fasted, crp, units)
    return render_template("query_result.html", tulos = tulos, sex = sex, age = age, diet = diet, hours_fasted = hours_fasted, crp = crp, units = units)


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
            return render_template("error.html",message="Username Is Already Taken")

@app.route("/submitlabs")
def submit():
    return render_template("submitlabs.html")

@app.route("/result", methods=["POST"])
def send_values():
    
    sex = request.form["sex"]
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

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["post"])
def send():
    topic = request.form["topic"]
    content = request.form["content"]
    if messages.send(topic, content):
        return redirect("/forum")
    else:
        return render_template("error.html",message="Viestin lähetys ei onnistunut")
    
 
@app.route("/forum")
def forum():
    lista = messages.get_list()
    return render_template("forum.html", messages = lista)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
                    
@app.route('/logo.jpg')
def logo():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'logo.jpg', mimetype='image/jpeg')
                    