from db import db
import users

def get_count():
    result = db.session.execute("SELECT COUNT(*) FROM labvalues")
    return result.fetchone()[0]

def get_values():
    sql = "SELECT U.username, L.lab_name, L.sex, L.age, L.diet, L.hours_fasted, L.units, L.total, L.ldl, L.hdl, L.triglyt, L.crp FROM labvalues L, users U WHERE L.user_id=U.id ORDER BY L.id"
    result = db.session.execute(sql)
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

