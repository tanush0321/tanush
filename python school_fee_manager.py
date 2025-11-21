import json
import os
filename = "database.json"
def load_data():
    if os.path.exists(filename):
        f = open(filename, 'r')
        data = json.load(f)
        f.close()
        return data
    else:
        return {}
def save_data(data):
    f = open(filename, 'w')
    json.dump(data, f, indent=4)
    f.close()
def add_student(db):
    print("\n--- ADD NEW STUDENT ---")
    roll_no = input("Enter Roll No: ")
    if roll_no in db:
        print("Roll number already exists.")
        return
    name = input("Enter Name: ")
    grade = input("Enter Class/Grade: ")
    total = float(input("Total Fee Amount: "))
    paid = input("Paid Amount (Press Enter for 0): ")
    if paid == "":
        paid = 0.0
    else:
        paid = float(paid)
    pending = total - paid
    db[roll_no] = {
        "name": name,
        "grade": grade,
        "total": total,
        "paid": paid,
        "pending": pending}
    save_data(db)
    print("Saved!")
def view_student(db):
    roll_no = input("\nEnter Roll No to search: ")
    if roll_no in db:
        s = db[roll_no]
        print("Name:", s['name'])
        print("Grade:", s['grade'])
        print("Total Fee:", s['total'])
        print("Paid:", s['paid'])
        print("Pending:", s['pending'])
    else:
        print("Student not found.")
def show_all(db):
    print(" ALL RECORDS")
    if len(db) == 0:
        print("No data available.")
        return
    print("Roll No\tName\t\tPending")
    for key in db:
        s = db[key]
        print(f"{key}\t{s['name']}\t\t{s['pending']}")
def update_details(db):
    roll_no = input("Enter Roll No to update: ")
    if roll_no not in db:
        print("Invalid Roll No.")
        return
    s = db[roll_no]
    print("Current Name:", s['name'])
    new_name = input("New Name (leave empty to keep same): ")
    if new_name != "":
        s['name'] = new_name
    print("Current Total Fee:", s['total'])
    new_total = input("New Total (leave empty to keep same): ")
    if new_total != "":
        s['total'] = float(new_total)
        s['pending'] = s['total'] - s['paid']
    save_data(db)
    print("Updated!")
def pay_fees(db):
    roll_no = input("Enter Roll No: ")
    if roll_no in db:
        amount = float(input("Enter amount being paid: "))
        db[roll_no]['paid'] += amount
        db[roll_no]['pending'] = db[roll_no]['total'] - db[roll_no]['paid']
        save_data(db)
        print(f"Payment of {amount} recorded.")
        if db[roll_no]['pending'] <= 0:
            print("Fully paid!")
        else:
            print(f"Remaining: {db[roll_no]['pending']}")
    else:
        print("Student not found.")
def main():
    students = load_data()
    while True:
        print("\n=== FEE MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View Details")
        print("3. Show All List")
        print("4. Update Student")
        print("5. Pay Fees")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_student(students)
        elif choice == '3':
            show_all(students)
        elif choice == '4':
            update_details(students)
        elif choice == '5':
            pay_fees(students)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Wrong choice.")
main()