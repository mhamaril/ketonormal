CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
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
    diet TEXT,
    hours_fasted INTEGER,
    units BOOLEAN,
    total INTEGER,
    ldl INTEGER,
    hdl INTEGER,
    triglyt INTEGER
);