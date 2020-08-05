from db import db
import users

def get_count():
    result = db.session.execute("SELECT COUNT(*) FROM labvalues")
    return result.fetchone()[0]

def get_labNames():
    sql = "SELECT L.lab_name FROM labvalues L, users U WHERE L.user_id=U.id ORDER BY L.lab_name"
    result = db.session.execute(sql)
    return result.fetchall()

def get_values(lab_name):
    sql = "SELECT L.lab_name, L.sex, L.age, L.diet, L.hours_fasted, L.units, L.total, L.ldl, L.hdl, L.triglyt, L.crp FROM labvalues L, users U WHERE L.user_id=U.id AND L.lab_name = :lab_name"
    result = db.session.execute(sql, {"lab_name":lab_name})
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
    sql = "INSERT INTO labvalues (lab_name, user_id, sex, age, diet, hours_fasted, units, total, ldl, hdl, triglyt, crp) VALUES (:lab_name, :user_id, :sex, :age, :diet, :hours_fasted, :units, :total, :ldl, :hdl, :triglyt, :crp)"
    db.session.execute(sql, {"lab_name":lab_name, "user_id":user_id, "sex":sex, "age":age, "diet":diet, "hours_fasted":hours_fasted, "units":units, "total":total, "ldl":ldl, "hdl":hdl, "triglyt":triglyt, "crp":crp})
    db.session.commit()
    return True

def query(age):
    minAge = 0
    maxAge = 0
    if age == "under":
        minAge = 0
        maxAge = 19
    if age == "20to40":
        minAge = 20
        maxAge = 39
    if age == "40to60":
        minAge = 40
        maxAge = 59
    if age == "over60":
        minAge = 60
        maxAge = 130
    if age == "all_ages":
        minAge = 0
        maxAge = 130
    sql = "SELECT SUM(ldl)/COUNT(ldl) FROM labvalues WHERE age BETWEEN :minAge AND :maxAge"
    result = db.session.execute(sql, {"minAge":minAge, "maxAge":maxAge})
    return result.fetchone()[0]
    
     

""" def query(sex, age, diet, hours_fasted, units, crp):
    if sex == "male":
        sexChosen == "Male"
    if sex == "female":
        sexChosen == "Female"
    if sex == "all_sexes"
        sexChosen == "*"

    if units == "usa":
        total = float(total)/38.67
        ldl = float(ldl)/38.67
        hdl = float(hdl)/38.67
        triglyt = float(triglyt)/38.67
    sql = "SELECT L.total, L.ldl, L.hdl, L.triglyt FROM labvalues L, users U WHERE L.age BETWEEN :min AND :max AND L.hours_fasted BETWEEN :f_min AND :f_max AND L.crp BETWEEN :min_crp AND :max_crp AND L.sex = :sexChosen AND L.total = :total AND L.ldl = :ldl AND L.hdl = :hdl AND L.triglyt = :triglyt"
    result = db.session.execute(sql, {"lab_name":lab_name})
    return result.fetchall()
    
 """