

#CSV
import csv
records = [
    ['Name','Marks','City','Grade'],
    ['Rahul',85,'Bhopal','B'],
    ['Priya',92,'Indore','A'],
    ['Amit',73,'Jabalpur','B']
]

with open('students.csv','w',newline='') as f:
    csv.writer(f).writerows(records)

name = input("Enter Student Name for Search: ")

with open('students.csv','r') as f:
    for row in csv.DictReader (f):
        if row["Name"] == name:
            print(f'Found{name}')
            print(f'{row["Name"]}:{row["Marks"]} marks ({row["City"]})')
            found = True
            break

if not found:
    print("Student Not Found!")