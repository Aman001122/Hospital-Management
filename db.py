import sqlite3
from pathlib import Path

DB_PATH=Path("hospital.db")

def get_conn():
    conn=sqlite3.connect(DB_PATH)
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS doctors(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT,
        token TEXT,
        doctor_id INTEGER,
        status TEXT DEFAULT 'waiting',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS settings(
        key TEXT PRIMARY KEY,
        value TEXT
    )""")
    conn.commit()
    conn.close()

def add_doctor(name,department):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("INSERT INTO doctors(name,department) VALUES(?,?)",(name,department))
    conn.commit()
    conn.close()

def get_doctors():
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("SELECT * FROM doctors")
    rows=cur.fetchall()
    conn.close()
    return rows

def get_doctor_by_id(did):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("SELECT * FROM doctors WHERE id=?",(did,))
    row=cur.fetchone()
    conn.close()
    return row

def add_patient(name,age,department,token,doctor_id):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("INSERT INTO patients(name,age,department,token,doctor_id) VALUES(?,?,?,?,?)",
                (name,age,department,token,doctor_id))
    conn.commit()
    conn.close()

def get_queue_by_doctor(doctor_id):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("SELECT * FROM patients WHERE doctor_id=? AND status!='consulted' ORDER BY id",(doctor_id,))
    rows=cur.fetchall()
    conn.close()
    return rows

def get_next_patient(doctor_id):
    q=get_queue_by_doctor(doctor_id)
    return q[0] if q else None

def mark_consulted(patient_id):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("UPDATE patients SET status='consulted' WHERE id=?",(patient_id,))
    conn.commit()
    conn.close()

def search_patients_by_name(name):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("SELECT * FROM patients WHERE name LIKE ? ORDER BY created_at DESC",('%'+name+'%',))
    rows=cur.fetchall()
    conn.close()
    return rows

def search_by_token(token):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("SELECT * FROM patients WHERE token=?",(token,))
    row=cur.fetchone()
    conn.close()
    return row

def get_all_patients():
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("SELECT * FROM patients ORDER BY created_at DESC")
    rows=cur.fetchall()
    conn.close()
    return rows

def get_daily_summary():
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("SELECT department, COUNT(*) as total, SUM(CASE WHEN status='consulted' THEN 1 ELSE 0 END) as consulted FROM patients GROUP BY department")
    rows=cur.fetchall()
    conn.close()
    return rows
