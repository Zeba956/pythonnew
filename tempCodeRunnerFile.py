class Student:
    def __init__(self,name,age,gender,grade):
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade

    def printdetails(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Grade:",self.grade)

Zeba = Student("Zeba Siddique", 20, "Female","10th")
print(Zeba)

# Zeba.name = "Zeba Siddique"
# Zeba.age = 20
# Zeba.gender = "Female"
# Zeba.grade = "10th"

Zeba.printdetails()

# print(Zeba.name)
# print(Zeba.age)
# print(Zeba.gender)
# print(Zeba.grade)