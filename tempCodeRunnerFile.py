import csv
import os

FILE_NAME = "students.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City", "Sub1", "Sub2", "Sub3"])


def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    city = input("Enter City: ")

    sub1 = int(input("Enter Subject 1 Marks: "))
    sub2 = int(input("Enter Subject 2 Marks: "))
    sub3 = int(input("Enter Subject 3 Marks: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, city, sub1, sub2, sub3])

    print("Student Added Successfully!")


def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            avg = (int(row[3]) + int(row[4]) + int(row[5])) / 3
            grade = calculate_grade(avg)

            print("\nName:", row[0])
            print("Age:", row[1])
            print("City:", row[2])
            print("Average:", round(avg, 2))
            print("Grade:", grade)


def search_student():
    name = input("Enter Student Name: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0].lower() == name.lower():
                print("\nStudent Found:")
                print(row)
                return

    print("Student Not Found!")


def delete_student():
    name = input("Enter Student Name to Delete: ")

    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0].lower() != name.lower():
                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Student Deleted Successfully!")


def statistics():
    topper = ""
    highest_avg = 0
    total_avg = 0
    count = 0
    pass_count = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            avg = (int(row[3]) + int(row[4]) + int(row[5])) / 3

            total_avg += avg
            count += 1

            if avg >= 40:
                pass_count += 1

            if avg > highest_avg:
                highest_avg = avg
                topper = row[0]

    if count > 0:
        print("\nTopper:", topper)
        print("Highest Average:", round(highest_avg, 2))
        print("Class Average:", round(total_avg / count, 2))
        print("Pass Rate:", round((pass_count / count) * 100, 2), "%")
    else:
        print("No Records Found!")


while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Statistics")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        statistics()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
