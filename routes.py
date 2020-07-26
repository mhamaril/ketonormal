from app import app
from flask import render_template, request, redirect
import messages, users

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")

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
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")

@app.route("/submitlabs")
def submit():
    return render_template("submitlabs.html")

@app.route("/result", methods=["POST"])
def result():
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
 