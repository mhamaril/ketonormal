from db import db
import users

def get_count():
    result = db.session.execute("SELECT COUNT(*) FROM labvalues")
    return result.fetchone()[0]

def ave_total():
    result = db.session.execute("SELECT SUM(total)/COUNT(total) FROM labvalues")
    return result.fetchone()[0]

def ave_ldl():
    result = db.session.execute("SELECT SUM(ldl)/count(ldl) FROM labvalues")
    return result.fetchone()[0]

def ave_hdl():
    result = db.session.execute("SELECT SUM(hdl)/COUNT(hdl) FROM labvalues")
    return result.fetchone()[0]

def ave_triglyt():
    result = db.session.execute("SELECT SUM(triglyt)/COUNT(triglyt) FROM labvalues")
    return result.fetchone()[0]


def get_labNames():
    sql = "SELECT L.lab_name FROM labvalues L, users U WHERE L.user_id=U.id ORDER BY L.lab_name"
    result = db.session.execute(sql)
    return result.fetchall()

def get_values(lab_name):
    sql = "SELECT L.lab_name, L.sex, L.age, L.diet, L.hours_fasted, L.units, L.total, L.ldl, L.hdl, L.triglyt, L.crp FROM labvalues L, users U WHERE L.user_id=U.id AND L.lab_name = :lab_name"
    result = db.session.execute(sql, {"lab_name":lab_name})
    return result.fetchall()

def get_query_total(sex, age, hours_fasted, crp):
    minAge = 0
    maxAge = 0
    minHours = 0
    maxHours = 0
    minCRP = 0
    maxCRP = 0
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
    sql = "SELECT AVG(total)-1.96*STDDEV(total), AVG(total), AVG(total)+1.96*STDDEV(total) FROM labvalues WHERE sex = :sex AND age BETWEEN :minAge AND :maxAge AND hours_fasted BETWEEN :minHours AND :maxHours AND crp BETWEEN :minCRP AND :maxCRP"
    result = db.session.execute(sql, {"sex":sex, "minAge":minAge, "maxAge":maxAge, "minHours":minHours, "maxHours":maxHours, "minCRP":minCRP, "maxCRP":maxCRP})
    return result.fetchall()

""" def get_query(sex, age, hours_fasted, crp):
    minAge = 0
    maxAge = 0
    minHours = 0
    maxHours = 0
    minCRP = 0
    maxCRP = 0
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
    sql = "SELECT total, ldl, hdl, triglyt FROM labvalues WHERE sex = :sex AND age BETWEEN :minAge AND :maxAge AND hours_fasted BETWEEN :minHours AND :maxHours AND crp BETWEEN :minCRP AND :maxCRP"
    result = db.session.execute(sql, {"sex":sex, "minAge":minAge, "maxAge":maxAge, "minHours":minHours, "maxHours":maxHours, "minCRP":minCRP, "maxCRP":maxCRP})
    return result.fetchall() """

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
    sql = "INSERT INTO labvalues (lab_name, user_id, sex, age, diet, hours_fasted, units, total, ldl, hdl, triglyt, crp) VALUES (:lab_name, :user_id, :sex, :age, :diet, :hours_fasted, :units, :total, :ldl, :hdl, :triglyt, :crp)"
    db.session.execute(sql, {"lab_name":lab_name, "user_id":user_id, "sex":sex, "age":age, "diet":diet, "hours_fasted":hours_fasted, "units":units, "total":total, "ldl":ldl, "hdl":hdl, "triglyt":triglyt, "crp":crp})
    db.session.commit()
    return True

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

 