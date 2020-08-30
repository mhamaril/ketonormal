CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    topic TEXT,
    created_at TIMESTAMP    
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topics,
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);
CREATE TABLE labvalues (
    id SERIAL PRIMARY KEY,
    lab_name TEXT,
    user_id INTEGER REFERENCES users,
    sex TEXT,
    age INTEGER,
    diet INTEGER,
    hours_fasted INTEGER,
    units TEXT,
    total REAL,
    ldl REAL,
    hdl REAL,
    triglyt REAL,
    crp REAL
);
CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    age INTEGER,
    gender TEXT,
    diet TEXT,
    units TEXT
);