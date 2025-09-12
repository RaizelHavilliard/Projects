import sqlite3

#connect to the database
conn = sqlite3.connect("Email_manager.db")
cursor = conn.cursor()

#Create UserProfile Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS UserProfile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

#Create Profiles table

cursor.execute("""
CREATE TABLE IF NOT EXISTS Profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL
)
""")


#Create Email templates table

cursor.execute("""
CREATE TABLE IF NOT EXISTS Templates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    body TEXT NOT NULL               
)
""")

#Create email history

cursor.execute("""
CREATE TABLE IF NOT EXISTS History (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination TEXT NOT NULL,
    subject TEXT NOT NULL,
    body TEXT NOT NULL,
    sent_at TEXT NOT NULL                              
)
""")

# Create Schedules table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Schedules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_id INTEGER NOT NULL,
    recipient_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    body TEXT NOT NULL,
    scheduled_for TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Pending',
    FOREIGN KEY (sender_id) REFERENCES UserProfile(id),
    FOREIGN KEY (recipient_id) REFERENCES Profiles(id)
)
""")

conn.commit()
conn.close()

print("data base and tables created succesfully!")






















