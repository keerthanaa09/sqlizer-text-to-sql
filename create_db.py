import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("INSERT INTO students VALUES (1, 'Asha', 85)")
cursor.execute("INSERT INTO students VALUES (2, 'Ravi', 72)")
cursor.execute("INSERT INTO students VALUES (3, 'Meena', 91)")

conn.commit()
conn.close()

print("Database created successfully")
