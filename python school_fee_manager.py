import json
import os
# for loading data:-
data_file = 'students.json'
students = {}
if os.path.exists(data_file):
    with open(data_file, 'r') as f:
        try:
            students = json.load(f)
        except json.JSONDecodeError:
            students = {}
    print(f"Loaded {len(students)} records\n")
while True:
    print("="*50)
    print("SCHOOL FEE MANAGER")
    print("="*50)
    print("1. Add Student")
    print("2. View Student")
    print("3. View All")
    print("4. Update Student")
    print("5. Add Payment")
    print("6. Delete Student")
    print("7. Exit")
    print("="*50)
    choice = input("\nChoice (1-7): ")

    # to Add new student
    if choice == '1':
        print("\n Add Student")
        id = input("Student ID: ")
        if id in students:
            print("ID already exists")
        else:
            name = input("Name: ")
            grade = input("Grade: ")
            total = float(input("Total Fee: "))
            paid = float(input("Paid : ") or 0)
            students[id] = {'name': name,
                'grade': grade,
                'total_fee': total,
                'paid_fee': paid,
                'pending': total - paid}
            # to Save to file
            with open(data_file, 'w') as f:
                json.dump(students, f, )
            print(f" Student {name} added!")

    # to View single student
    elif choice == '2':
        print("\n View Student")
        id = input("Student ID: ")
        if id in students:
            s = students[id]
            print("\n" + "="*50)
            print(f"ID: {id}")
            print(f"Name: {s['name']}")
            print(f"Grade: {s['grade']}")
            print(f"Total Fee: ₹{s['total_fee']:.2f}")
            print(f"Paid Fee: ₹{s['paid_fee']:.2f}")
            print(f"Pending: ₹{s['pending']:.2f}")
            status = "PAID" if s['paid_fee'] >= s['total_fee'] else "PARTIAL" if s['paid_fee'] > 0 else "UNPAID"
            print(f"Status: {status}")
            print("="*50)
        else:
            print(" Student not found!")

    # to View all students
    elif choice == '3':
        print("\nAll Students")
        if not students:
            print("No records found!")
        else:
            print("\n" + "="*90)
            print(f"{'ID':<10} {'Name':<20} {'Grade':<8} {'Total':<12} {'Paid':<12} {'Pending':<12}")
            print("="*90)
            for id, s in students.items():
                print(f"{id:<10} {s['name']:<20} {s['grade']:<8} "
                      f"₹{s['total_fee']:<11.2f} ₹{s['paid_fee']:<11.2f} ₹{s['pending']:<11.2f}")
            print("="*90)
            print(f"Total: {len(students)} students\n")

    # to Update student info
    elif choice == '4':
        print("\n Update Student")
        id = input("Student ID: ")
        if id not in students:
            print(" Student not found")
            continue
        s = students[id]
        print("Leave blank to keep current value")
        name = input(f"Name ({s['name']}): ")
        grade = input(f"Grade ({s['grade']}): ")
        total = input(f"Total Fee ({s['total_fee']}): ")
        paid = input(f"Paid Fee ({s['paid_fee']}): ")
        if name: s['name'] = name
        if grade: s['grade'] = grade
        if total: s['total_fee'] = float(total)
        if paid: s['paid_fee'] = float(paid)
        s['pending'] = s['total_fee'] - s['paid_fee']
        # to Save to file
        with open(data_file, 'w') as f:
            json.dump(students, f, )
        print(" Updated successfully!")

    # to Add payment
    elif choice == '5':
        print("\n--- Add Payment ---")
        id = input("Student ID: ")
        if id not in students:
            print(" Student not found!")
        else:
            amount = float(input("Payment Amount: "))
            students[id]['paid_fee'] += amount
            students[id]['pending'] = students[id]['total_fee'] - students[id]['paid_fee']
            # to Save to file
            with open(data_file, 'w') as f:
                json.dump(students, f, )
            print(f" Payment of ₹{amount} added!")

    # to Remove student
    elif choice == '6':
        print("\n--- Delete Student ---")
        id = input("Student ID: ")
        if id not in students:
            print(" Student not found!")
            continue
        confirm = input(f"Delete {students[id]['name']}? (yes/no): ")
        if confirm.lower() == 'yes':
            del students[id]
            # to Save to file
            with open(data_file, 'w') as f:
                json.dump(students, f, )
            print(" Deleted successfully")
    # for exit from student fee manager:-
    elif choice == '7':
        print("\nThank you")
        break
    else:
        print("Invalid choice")