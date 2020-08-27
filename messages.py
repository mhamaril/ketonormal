from db import db
import users

def get_list():
    sql = "SELECT T.id, T.topic, U.username, M.content, M.sent_at FROM messages M, users U, topics T \
        WHERE M.user_id=U.id AND T.id = M.topic_id ORDER BY M.id DESC"
    result = db.session.execute(sql)
    return result.fetchall()

def get_my_posts(user_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT T.topic, U.username, M.content, M.sent_at, T.id, M.id FROM messages M, users U, topics T \
        WHERE M.user_id=U.id AND M.user_id = :user_id AND T.id = M.topic_id ORDER BY M.id DESC"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()

def get_limited_list():
    sql = "SELECT T.topic, U.username, M.content, M.sent_at, T.id FROM messages M, users U, topics T \
        WHERE M.user_id=U.id AND T.id = M.topic_id ORDER BY M.id DESC LIMIT 3"
    result = db.session.execute(sql)
    return result.fetchall()

def send(topic, content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO topics (topic, user_id, created_at) VALUES (:topic, :user_id, NOW()) RETURNING id"
    result = db.session.execute(sql, {"topic":topic, "user_id":user_id})
    topic_id = result.fetchone()[0]
    sql = "INSERT INTO messages (topic_id, content, user_id, sent_at) VALUES (:topic_id, :content, :user_id, NOW())"
    db.session.execute(sql, {"topic_id":topic_id, "content":content, "user_id":user_id})
    db.session.commit()
    return True

def send_reply(topic_id, content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO messages (topic_id, content, user_id, sent_at) VALUES (:topic_id, :content, :user_id, NOW())"
    db.session.execute(sql, {"topic_id":topic_id, "content":content, "user_id":user_id})
    db.session.commit()
    return True

def get_messages(id):
    sql = "SELECT T.id, T.topic, M.content, U.username, M.sent_at FROM messages M, users U, topics T \
        WHERE M.user_id = U.id AND  T.id = M.topic_id AND T.id = :id ORDER BY M.sent_at DESC"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_topic_id(id):
    sql = "SELECT T.id FROM topics T WHERE T.id = :id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def get_topics():
    sql = "SELECT T.id, T.topic, FIRST_VALUE(M.content) OVER (PARTITION BY T.topic ORDER BY M.sent_at DESC) AS latest \
        FROM messages M, topics T where T.id = M.topic_id"
    result = db.session.execute(sql)
    return result.fetchall()

def delete_post(id):
    if id == 0:
        return False
    sql = "DELETE FROM messages WHERE id = :id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True
