from db import db
import users

def get_list():
    sql = "SELECT M.id, M.topic, U.username, M.content, M.sent_at FROM messages M, users U WHERE M.user_id=U.id ORDER BY M.id"
    result = db.session.execute(sql)
    return result.fetchall()

def get_limited_list():
    sql = "SELECT M.id, M.topic, U.username, M.content, M.sent_at FROM messages M, users U WHERE M.user_id=U.id ORDER BY M.id LIMIT 3"
    result = db.session.execute(sql)
    return result.fetchall()


def send(topic, content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO messages (topic, content, user_id, sent_at) VALUES (:topic, :content, :user_id, NOW())"
    db.session.execute(sql, {"topic":topic, "content":content, "user_id":user_id})
    db.session.commit()
    return True

def get_messages(id):
    sql = "SELECT M.id, M.topic, M.content, M.sent_at FROM messages M WHERE M.id = :id ORDER BY M.sent_at"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

