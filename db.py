import sqlite3

def get_db():
    con = sqlite3.connect("hospital.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            department TEXT,
            doctor TEXT,
            token INTEGER,
            time TEXT,
            status TEXT
        )
    """)
    con.commit()
    return con
