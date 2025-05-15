DROP TABLE IF EXISTS users;
CREATE TABLE users (
    email TEXT PRIMARY KEY,
    name TEXT,
    picture TEXT,
    role TEXT DEFAULT 'user'
);

DROP TABLE IF EXISTS search_history;
CREATE TABLE search_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    query TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS downloads;
CREATE TABLE downloads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    olid TEXT,
    title TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS purchases;
CREATE TABLE purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    olid TEXT,
    title TEXT,
    amount REAL,
    status TEXT,
    transaction_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS wishlist;
CREATE TABLE wishlist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    olid TEXT,
    title TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
