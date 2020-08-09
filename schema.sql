CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,	
    topic TEXT,
    created_at TIMESTAMP
);
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    message_id INTEGER REFERENCES subjects,
    sent_at TIMESTAMP
);
CREATE TABLE labvalues (
    id SERIAL PRIMARY KEY,
    lab_name TEXT,
    user_id INTEGER REFERENCES users,
    sex TEXT,
    age INTEGER,
    diet TEXT,
    hours_fasted INTEGER,
    units TEXT,
    total REAL,
    ldl REAL,
    hdl REAL,
    triglyt REAL,
    crp REAL
);