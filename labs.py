from db import db
import users

def get_values():
    sql = "SELECT L.content, U.username, L.lab_name, L.sex, L.age, L.diet, L.hours, L.units, L.total, L.ldl, L.hdl, L.triglyt FROM labvalues L, users U WHERE L.user_id=U.id ORDER BY L.id"
    result = db.session.execute(sql)
    return result.fetchall()

def send_values(lab_name, user_id, sex, age, diet, hours, units, total, ldl, hdl, triglyt):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO labvalues (lab_name, user_id, sex, age, diet, hours_fasted, units, total, ldl, hdl, triglyt) VALUES (:lab_name, :user_id, :sex, :age, :diet, :hours, :units, :total, :ldl, :hdl, :triglyt)"
    db.session.execute(sql, {"lab_name":lab_name, "user_id":user_id, "sex":sex, "age":age, "diet":diet, "hours":hours, "units":units, "total":total, "ldl":ldl, "hdl":hdl, "triglyt":triglyt})
    db.session.commit()
    return True