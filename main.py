from db import init_db,get_doctors,add_doctor,add_patient,get_doctor_by_id,get_queue_by_doctor,get_next_patient,mark_consulted,search_patients_by_name,search_by_token
from models import generate_token,format_patient_row
from utils import export_daily_report_txt,export_patients_json
import sys

def ensure_sample_doctors():
    docs=get_doctors()
    if not docs:
        add_doctor("Dr. Aman","General")
        add_doctor("Dr. Priya","Pediatrics")
        add_doctor("Dr. Raju","Cardiology")

def list_doctors():
    docs=get_doctors()
    print("Doctors:")
    for d in docs:
        print(f"{d['id']}. {d['name']} - {d['department']}")

def register_patient():
    name=input("Patient name: ").strip()
    age=input("Age: ").strip()
    list_doctors()
    did=input("Enter doctor id to assign (or 0 for department selection): ").strip()
    if did=="0" or did=="":
        department=input("Enter department name: ").strip()
        doctor_id=None
    else:
        doctor_id=int(did)
        dep=get_doctor_by_id(doctor_id)
        department=dep["department"] if dep else input("Department: ").strip()
    token=generate_token(department)
    add_patient(name,int(age) if age.isdigit() else None,department,token,doctor_id)
    print(f"Registered. Token: {token}")

def show_queue():
    list_doctors()
    did=input("Doctor id: ").strip()
    doc_id=int(did)
    q=get_queue_by_doctor(doc_id)
    if not q:
        print("Queue empty")
        return
    for p in q:
        print(f"Patient {p['id']} | {p['name']} | Token: {p['token']} | Status: {p['status']}")

def call_next():
    list_doctors()
    did=input("Doctor id: ").strip()
    doc_id=int(did)
    p=get_next_patient(doc_id)
    if not p:
        print("No waiting patients")
        return
    print("Now calling:")
    print(f"{p['id']} {p['name']} Token:{p['token']}")
    confirm=input("Mark as consulted now? (y/n): ").strip().lower()
    if confirm=="y":
        mark_consulted(p["id"])
        print("Marked consulted")

def search_patient():
    typ=input("Search by (1) name (2) token: ").strip()
    if typ=="1":
        name=input("Name: ").strip()
        rows=search_patients_by_name(name)
        for r in rows:
            print(format_patient_row(r))
    else:
        token=input("Token: ").strip()
        r=search_by_token(token)
        if r:
            print(format_patient_row(r))
        else:
            print("Not found")

def export_reports():
    p1=export_daily_report_txt()
    p2=export_patients_json()
    print("Exported:",p1,p2)

def main_menu():
    init_db()
    ensure_sample_doctors()
    while True:
        print("""
1 Register patient
2 Show doctor queue
3 Call next patient
4 Search patient
5 Export reports
6 List doctors
0 Exit
""")
        c=input("Choose: ").strip()
        if c=="1":
            register_patient()
        elif c=="2":
            show_queue()
        elif c=="3":
            call_next()
        elif c=="4":
            search_patient()
        elif c=="5":
            export_reports()
        elif c=="6":
            list_doctors()
        elif c=="0":
            print("Bye")
            sys.exit(0)
        else:
            print("Invalid")

if __name__=="__main__":
    main_menu()
