import csv
import datetime

print("ATTENDANCE OF IT (O BATCH STUDENT):-")

# List of 24 students
students = [
    {'id': 'F001', 'name': 'OM'},
    {'id': 'F002', 'name': 'OMRAJE'},
    {'id': 'F003', 'name': 'Nishtha'},
    {'id': 'F004', 'name': 'VISHAL'},
    {'id': 'F005', 'name': 'SARVADNYA'},
    {'id': 'F006', 'name': 'YASH'},
    {'id': 'F007', 'name': 'RAHUL'},
    {'id': 'F008', 'name': 'GANESH'},
    {'id': 'F009', 'name': 'ATHARVA'},
    {'id': 'F010', 'name': 'VIPUL'},
    {'id': 'F011', 'name': 'ATHARVA'},
    {'id': 'F012', 'name': 'SHIVAM'},
    {'id': 'F013', 'name': 'SIDHANT'},
    {'id': 'F014', 'name': 'HARSHIT'},
    {'id': 'F015', 'name': 'DHRUV'},
    {'id': 'F016', 'name': 'SHREJAL'},
    {'id': 'F017', 'name': 'SANIKA'},
    {'id': 'F018', 'name': 'SIDDHESH'},
    {'id': 'F019', 'name': 'SOHAM'},
    {'id': 'F020', 'name': 'MADHAV'},
    {'id': 'F021', 'name': 'ANIKET'},
    {'id': 'F022', 'name': 'MADHURA'},
    {'id': 'F023', 'name': 'PARTH'},
    {'id': 'F024', 'name': 'MOHIT'}
]

# Function to mark attendance
def mark_attendance():
    date_today = datetime.date.today().strftime("%Y-%m-%d")
    present_students = []
    print(f"Marking attendance for {date_today}")

    # Loop through all students and ask for attendance
    for student in students:
        attendance = input(f"Is {student['name']} ({student['id']}) present? (y/n): ")
        if attendance.lower() == 'y':
            present_students.append(student['id'])

    # Save the attendance record to a CSV file
    with open('attendance.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for student in students:
            status = 'Present' if student['id'] in present_students else 'Absent'
            writer.writerow([date_today, student['id'], student['name'], status])

    print(f"Attendance for {date_today} has been recorded.")

# Function to view attendance
def view_attendance():
    print("View Attendance Records:")
    try:
        with open('attendance.csv', mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]}, ID: {row[1]}, Name: {row[2]}, Status: {row[3]}")
    except FileNotFoundError:
        print("No attendance records found.")

# Main function to interact with the system
def main():
    while True:
        print("\nAttendance System")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            mark_attendance()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the system
if __name__ == "__main__":
    main()
