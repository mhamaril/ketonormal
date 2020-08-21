from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,password):
    
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            session["username"] = username
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username,password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, is_admin) VALUES (:username, :password, FALSE) RETURNING ID" 
        result = db.session.execute(sql, {"username":username,"password":hash_value})
        user_id = result.fetchone()[0]
       
        sql = "INSERT INTO profiles (user_id, age, gender, diet, units) VALUES (:user_id, 999, '', 0, '')"
        db.session.execute(sql, {"user_id":user_id})
        db.session.commit()
    except:
        return False
    return login(username,password)

def user_id():
    return session.get("user_id",0)

def update(age, gender, diet, units, user_id):
    
    if user_id == 0:
        return False
    sql = "UPDATE profiles SET age = :age, gender = :gender, diet = :diet, units = :units WHERE user_id = :user_id"
    result = db.session.execute(sql, {"age":age, "gender":gender, "diet":diet, "units":units, "user_id":user_id})
    db.session.commit()
    return True