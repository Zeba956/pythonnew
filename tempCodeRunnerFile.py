
import csv

records = [
    ['Name','Marks','City','Grade'],
    [' ' ,'Rahul','#85','BhopalCity','B*'],
    ['Priya','#92','IndoreDist','@A'],
    ['Amit','#73','JabalpurCity','B']
]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(records)

print("Unclean data created successfully!")