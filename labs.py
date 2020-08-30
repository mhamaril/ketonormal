from db import db
import users
import pandas as pd
from os import getenv
import json
    
def get_averages():
    result = db.session.execute("SELECT COUNT(*), ROUND(CAST (AVG(total) AS numeric),2), ROUND(CAST (AVG(ldl) AS numeric),2),\
        ROUND(CAST (AVG(hdl) AS numeric),2), ROUND(CAST (AVG(triglyt) AS numeric),2) FROM labvalues")
    return result.fetchall()

def get_lab_names(user_id):
    
    sql = "SELECT id, lab_name FROM labvalues WHERE user_id = :user_id ORDER BY lab_name"
    result = db.session.execute(sql, {"user_id":user_id}) 
    return result.fetchall()

def get_values(id):
    sql = "SELECT L.id, L.lab_name, L.sex, L.age, L.diet, L.hours_fasted, L.units, L.total, L.ldl, L.hdl, L.triglyt, L.crp \
        FROM labvalues L, users U WHERE L.user_id=U.id AND L.id = :id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_query_total(sex, age, diet, hours_fasted, crp, units):
    if age == "under":
        minAge = 10
        maxAge = 39
    if age == "40to59":
        minAge = 40
        maxAge = 59
    if age == "over60":
        minAge = 60
        maxAge = 130
    if age == "all_ages":
        minAge = 0
        maxAge = 130
    if hours_fasted == "under":
        minHours = 0
        maxHours = 11
    if hours_fasted == "between":
        minHours = 12
        maxHours = 14
    if hours_fasted == "over":
        minHours = 15
        maxHours = 999
    if hours_fasted == "all_hours":
        minHours = 0
        maxHours = 999
    if crp == "good":
        minCRP = 0
        maxCRP = 1
    if crp == "normal":
        minCRP = 1
        maxCRP = 3
    if crp == "higher":
        minCRP = 3
        maxCRP = 999
    if crp == "all_crp":
        minCRP = 0
        maxCRP = 999
    minDiet = 0
    maxDiet = 0
    if diet == 'all':
        minDiet = 0
        maxDiet = 6
    if diet == 'ketozero':
        minDiet = 0
        maxDiet = 4
    if diet == 'LCHF':
        minDiet = 4
        maxDiet = 6
    if diet == 'keto':
        minDiet = 2
        maxDiet = 4
    if diet == 'zero':
        minDiet = 0
        maxDiet = 2
        
    sql = "SELECT ROUND(CAST (AVG(total)-1.96*STDDEV(total) AS numeric),2), ROUND(CAST (AVG(total) AS numeric),2),\
        ROUND(CAST (AVG(total)+1.96*STDDEV(total) AS numeric),2), ROUND(CAST (AVG(ldl)-1.96*STDDEV(ldl) AS numeric),2),\
        ROUND(CAST (AVG(ldl) AS numeric),2), ROUND(CAST (AVG(ldl)+1.96*STDDEV(ldl) AS numeric),2),\
        ROUND(CAST (AVG(hdl)-1.96*STDDEV(hdl) AS numeric),2), ROUND(CAST (AVG(hdl) AS numeric),2),\
        ROUND(CAST (AVG(hdl)+1.96*STDDEV(hdl) AS numeric),2), ROUND(CAST (AVG(triglyt)-1.96*STDDEV(triglyt) AS numeric),2),\
        ROUND(CAST (AVG(triglyt) AS numeric),2), ROUND(CAST (AVG(triglyt)+1.96*STDDEV(triglyt) AS numeric),2), COUNT(*)\
        FROM labvalues WHERE sex = :sex AND age BETWEEN :minAge AND :maxAge \
        AND diet BETWEEN :minDiet AND :maxDiet AND hours_fasted BETWEEN :minHours AND :maxHours AND crp BETWEEN :minCRP AND :maxCRP"
    result = db.session.execute(sql, {"sex":sex, "minAge":minAge, "maxAge":maxAge, "minDiet":minDiet,"maxDiet":maxDiet,\
        "minHours":minHours, "maxHours":maxHours, "minCRP":minCRP, "maxCRP":maxCRP, "units":units})
    return result.fetchall()

def get_gender_from_profile():
    user_id = users.user_id()
    sql = "SELECT gender FROM profiles WHERE user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchone()[0]

def get_age_from_profile():
    user_id = users.user_id()
    sql = "SELECT age FROM profiles WHERE user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchone()[0]

def get_diet_from_profile():
    user_id = users.user_id()
    sql = "SELECT diet FROM profiles WHERE user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchone()[0]

def get_units_from_profile():
    user_id = users.user_id()
    sql = "SELECT units FROM profiles WHERE user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchone()[0]

def get_profile_ranges():
    user_id = users.user_id()
    sex = get_gender_from_profile()
    age = get_age_from_profile()
    diet = get_diet_from_profile()
    minDiet = 0
    maxDiet = 0
    units = get_units_from_profile()
    minAge = 0
    maxAge = 0
    
    if age > 10 and age < 40:
        minAge = 10
        maxAge = 39
    if age >= 40 and age < 60:
        minAge = 40
        maxAge = 59
    if age >= 60:
        minAge = 60
        maxAge = 130
     
    sql = "SELECT ROUND(CAST (AVG(total)-1.96*STDDEV(total) AS numeric),2), ROUND(CAST (AVG(total) AS numeric),2),\
        ROUND(CAST (AVG(total)+1.96*STDDEV(total) AS numeric),2),ROUND(CAST (AVG(ldl)-1.96*STDDEV(ldl) AS numeric),2),\
        ROUND(CAST (AVG(ldl) AS numeric),2), ROUND(CAST (AVG(ldl)+1.96*STDDEV(ldl) AS numeric),2),\
        ROUND(CAST (AVG(hdl)-1.96*STDDEV(hdl) AS numeric),2), ROUND(CAST (AVG(hdl) AS numeric),2),\
        ROUND(CAST (AVG(hdl)+1.96*STDDEV(hdl) AS numeric),2), ROUND(CAST (AVG(triglyt)-1.96*STDDEV(triglyt) AS numeric),2),\
        ROUND(CAST (AVG(triglyt) AS numeric),2), ROUND(CAST (AVG(triglyt)+1.96*STDDEV(triglyt) AS numeric),2), COUNT(*)\
        FROM labvalues WHERE sex = :sex AND age BETWEEN :minAge AND :maxAge AND diet = :diet\
        AND hours_fasted BETWEEN 11 AND 15 AND crp BETWEEN 0 AND 3"
    result = db.session.execute(sql, {"sex":sex, "minAge":minAge, "maxAge":maxAge, "diet":diet, "units":units})
    return result.fetchall()

def send_values(lab_name, user_id, sex, age, diet, hours_fasted, units, total, ldl, hdl, triglyt, crp):
    user_id = users.user_id()
    if user_id == 0:
        return False
    if units == "usa":
        total = float(total)/38.67
        ldl = float(ldl)/38.67
        hdl = float(hdl)/38.67
        triglyt = float(triglyt)/38.67
    if crp == "good":
        crp = 0.5
    if crp == "normal":
        crp = 2
    if crp == "higher":
        crp = 5
    sql = "INSERT INTO labvalues (lab_name, user_id, sex, age, diet, hours_fasted, units, total, ldl, hdl, triglyt, crp)\
         VALUES (:lab_name, :user_id, :sex, :age, :diet, :hours_fasted, :units, :total, :ldl, :hdl, :triglyt, :crp)"
    db.session.execute(sql, {"lab_name":lab_name, "user_id":user_id, "sex":sex, "age":age, "diet":diet,\
         "hours_fasted":hours_fasted, "units":units, "total":total, "ldl":ldl, "hdl":hdl, "triglyt":triglyt, "crp":crp})
    db.session.commit()
    return True

def remove_lab(id):
    if id == 0:
        return False
    sql = "DELETE FROM labvalues WHERE id = :id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True