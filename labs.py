from db import db
import users

def get_values():
    sql = "SELECT U.username, L.lab_name, L.sex, L.age, L.diet, L.hours, L.units, L.total, L.ldl, L.hdl, L.triglyt FROM labvalues L, users U WHERE L.user_id=U.id ORDER BY L.id"
    result = db.session.execute(sql)
    return result.fetchall()

def send_values(lab_name, user_id, sex, age, diet, hours, units, total, ldl, hdl, triglyt):
    user_id = users.user_id()
    if user_id == 0:
        return False
    if units == usa:
        total = float(total)/38.67
        ldl = float(ldl)/38.67
        hdl = float(hdl)/38.67
        trigly = float(trigly)/38.67
    sql = "INSERT INTO labvalues (lab_name, user_id, sex, age, diet, hours_fasted, units, total, ldl, hdl, triglyt) VALUES (:lab_name, :user_id, :sex, :age, :diet, :hours, :units, :total, :ldl, :hdl, :triglyt)"
    db.session.execute(sql, {"lab_name":lab_name, "user_id":user_id, "sex":sex, "age":age, "diet":diet, "hours":hours, "units":units, "total":total, "ldl":ldl, "hdl":hdl, "triglyt":triglyt})
    db.session.commit()
    return True

