from app import app
from flask import render_template, request, redirect, flash
import labs, users, messages
from db import db
import os
from flask import session
from flask import send_from_directory
import json, random

@app.route("/")
def index():
    
    return render_template("login.html")

@app.route("/login", methods=["GET","POST"])
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
    gender = labs.get_gender_from_profile()
    lista = messages.get_limited_list()
    age = labs.get_age_from_profile()
    diet = labs.get_diet_from_profile()
    units = labs.get_units_from_profile()
    ranges = labs.get_profile_ranges()
    return render_template("mypage.html", lab_names = lab_names, messages = lista, age = age, user_id = user_id, gender = gender, \
        diet = diet, units = units, ranges = ranges)
 
@app.route("/results/<int:id>")
def lab_name(id):
    lab_name = labs.get_values(id)

    return render_template("results.html", lab_name = lab_name)

@app.route("/remove_lab", methods=["POST"])
def remove_lab():
    id = request.form["id"]
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    
    if labs.remove_lab(id):
        return redirect("/mypage")
    else:
        return render_template("error.html",message="Something went wrong!")


@app.route("/topic/<int:id>")
def topic(id):
    topic_id = messages.get_topic_id(id)
    topic = messages.get_messages(id)
    lista = messages.get_list()
    return render_template("topic.html", topic = topic,  messages = lista, topic_id = topic_id)

    

@app.route("/send_reply", methods=["POST"])
def send_reply():
    topic_id = request.form["topic_id"]
    content = request.form["content"]
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if messages.send_reply(topic_id, content):
        return redirect("/topic/"+str(topic_id))
    else:
        return render_template("error.html",message="Viestin lähetys ei onnistunut")

@app.route("/query")
def query():
    return render_template("query.html")

@app.route("/query_result", methods=["POST"])
def get_query_total():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
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

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        if len(username)<5:
            return render_template("error.html", message="Username Is Too Short")
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/mypage")
        else:
            return render_template("error.html", message="Username Is Already Taken")

@app.route("/submitlabs")
def submit():
    return render_template("submitlabs.html")

@app.route("/result", methods=["POST"])
def send_values():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
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
        ldl = request.form["ldl"]
        hdl = request.form["hdl"]
        triglyt = request.form["triglyt"]
    else:
        units = "int"
        total = request.form["total"]
        ldl = request.form["ldl"]
        hdl = request.form["hdl"]
        triglyt = request.form["triglyt"]
    if labs.send_values(lab_name, user_id, sex, age, diet, hours_fasted, units, total, ldl, hdl, triglyt, crp):
        flash('Labs were successfully submitted')
        return redirect("/mypage")
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
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
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
              
@app.route("/update_profile")
def update_profile():
    
    return render_template("update_profile.html")

@app.route("/update", methods=["post"])
def update():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    user_id = users.user_id()
    age = request.form["age"]
    gender = request.form["gender"]
    diet = request.form["diet"]
    units = request.form["units"]
    if users.update(age, gender, diet, units, user_id):
        return redirect("/mypage")
    else:
        return render_template("error.html",message="Update was not succesful")

@app.route("/edit_posts")
def edit_posts():
    user_id = users.user_id()
    lista = messages.get_my_posts(user_id)
    
    return render_template("edit_posts.html", lista = lista) 

@app.route("/delete_post", methods=["post"])
def delete_post():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    user_id = users.user_id()
    id = request.form["id"]
    if messages.delete_post(id):
        return redirect("/forum")
    else:
        return render_template("error.html",message="Something went wrong!")
    
