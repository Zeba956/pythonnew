with open ('students.txt', 'w') as f:
    f.write('Rahul Sharma,85,Bhopal\n')
    f.write('Priya Verma,92,Indore\n')
    f.write('Amit Kumar,73,Jabalpur\n')

with open('students.txt','a') as f:
    f.write('Sneha Joshi,88,Bhopal\n')

with open('students.txt','r') as f:
    content = f.read()
print(content)

with open('students.txt','r') as f:
    for line in f:
        name,marks,city = line.strip().split(',')
        print(f'{name:<15} | {marks:>5} | {city}')
        print("--------------")