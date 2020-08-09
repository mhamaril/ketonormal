from db import db
import users

def get_topics():
    sql = "SELECT S.topic, U.username, S.created_at FROM subjects S, users U WHERE S.user_id=U.id ORDER BY S.id DESC" # LIMIT 3
    result = db.session.execute(sql)
    return result.fetchall()

def set_topic():
    sql = "INSERT INTO subjects (topic, created_at) VALUES (:topic, NOW())"
    db.session.execute(sql, {"topic":topic})
    db.session.commit()
    return True

def create_message():
    topic = request.form["topic"]
    sql = "INSERT INTO messages (topic, content, sent_at) VALUES (:topic, :content, NOW()) RETURNING id"
    result = db.session.execute(sql, {"topic":topic, "content":content})
    message_id = result.fetchone()[0]
    choices = request.form.getlist("choice")
    for choice in choices:
        if choice != "":
            sql = "INSERT INTO choices (poll_id, choice) VALUES (:poll_id, :choice)"
            db.session.execute(sql, {"poll_id":poll_id, "choice":choice})
    db.session.commit()
    return redirect("/forum")