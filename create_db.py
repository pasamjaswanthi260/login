import sqlite3

db = sqlite3.connect("users.db")
db.execute("""
CREATE TABLE users (
    username TEXT,
    password TEXT
)
""")
db.commit()
db.close()

print("Database created successfully")