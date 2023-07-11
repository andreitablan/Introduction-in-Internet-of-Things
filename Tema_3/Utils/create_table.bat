sqlite3 Storage.db
CREATE TABLE sensors_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_name TEXT NOT NULL,
    value INTEGER,
    timestamp TEXT NOT NULL,
    unique (sensor_name, value, timestamp)
);