from models import (
    add_patient,
    get_last_token,
    get_queue,
    mark_consulted,
    search_patient,
    get_ongoing_consultations
)
from utils import estimate_time

doctors = {
    "1": "Dr. Sharma",
    "2": "Dr. Mehta",
    "3": "Dr. Singh"
}

while True:
    print("\nHOSPITAL APPOINTMENT SYSTEM")
    print("1 Register Patient")
    print("2 View Doctor Queue")
    print("3 Mark Consultation Done")
    print("4 Search Patient")
    print("5 View Ongoing Consultations")
    print("6 Exit")

    ch = input("Choose option: ")

    if ch == "1":
        name = input("Patient name: ")
        age = int(input("Age: "))
        dept = input("Department: ")

        print("Choose Doctor:")
        for k, v in doctors.items():
            print(k, v)

        d = input("Enter doctor number: ")

        if d not in doctors:
            print("Invalid doctor selection")
            continue

        doctor = doctors[d]
        token = get_last_token(doctor) + 1
        time = estimate_time(token)

        add_patient(name, age, dept, doctor, token, time)
        print(f"Registered | Token {token} | Time {time}")

    elif ch == "2":
        print("Choose Doctor:")
        for k, v in doctors.items():
            print(k, v)

        d = input("Enter doctor number: ")

        if d not in doctors:
            print("Invalid doctor selection")
            continue

        doctor = doctors[d]
        queue = get_queue(doctor)

        print(f"\nQueue for {doctor}")
        for q in queue:
            print(q)

    elif ch == "3":
        token = int(input("Enter token number: "))
        mark_consulted(token)
        print("Consultation marked complete")

    elif ch == "4":
        val = input("Enter patient name or token: ")
        results = search_patient(val)
        for r in results:
            print(r)

    elif ch == "5":
        ongoing = get_ongoing_consultations()
        if not ongoing:
            print("No ongoing consultations")
        else:
            print("\nOngoing Consultations:")
            for o in ongoing:
                print(o)

    elif ch == "6":
        print("Exiting system")
        break

    else:
        print("Invalid option")
