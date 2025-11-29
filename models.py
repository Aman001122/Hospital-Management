from datetime import datetime
from random import randint

def generate_token(department):
    t=datetime.now().strftime("%y%m%d%H%M%S")
    r=randint(10,99)
    dep=department[:3].upper()
    return f"{dep}-{t}-{r}"

def format_patient_row(row):
    return {
        "id":row["id"],
        "name":row["name"],
        "age":row["age"],
        "department":row["department"],
        "token":row["token"],
        "doctor_id":row["doctor_id"],
        "status":row["status"],
        "created_at":row["created_at"]
    }
