import db

def add_patient(name, age, department, doctor, token, time):
    con = db.get_db()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO patients (name, age, department, doctor, token, time, status) VALUES (?,?,?,?,?,?,?)",
        (name, age, department, doctor, token, time, "Waiting")
    )
    con.commit()
    con.close()

def get_last_token(doctor):
    con = db.get_db()
    cur = con.cursor()
    cur.execute(
        "SELECT MAX(token) FROM patients WHERE doctor=?",
        (doctor,)
    )
    t = cur.fetchone()[0]
    con.close()
    return t if t else 0

def get_queue(doctor):
    con = db.get_db()
    cur = con.cursor()
    cur.execute(
        "SELECT token, name, time, status FROM patients WHERE doctor=? ORDER BY token",
        (doctor,)
    )
    rows = cur.fetchall()
    con.close()
    return rows

def mark_consulted(token):
    con = db.get_db()
    cur = con.cursor()
    cur.execute(
        "UPDATE patients SET status='Consulted' WHERE token=?",
        (token,)
    )
    con.commit()
    con.close()

def search_patient(value):
    con = db.get_db()
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM patients WHERE name LIKE ? OR token=?",
        (f"%{value}%", value if value.isdigit() else -1)
    )
    rows = cur.fetchall()
    con.close()
    return rows
def get_ongoing_consultations():
    con = db.get_db()
    cur = con.cursor()
    cur.execute(
        "SELECT doctor, token, name, time FROM patients WHERE status='Waiting' ORDER BY doctor, token"
    )
    rows = cur.fetchall()
    con.close()
    return rows
