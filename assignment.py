# This program performs various arithmetic operations on two numbers input by the user.

a=int(input("enter the number: "))
b=int(input("enter the number: "))
sum=a+b
difference=a-b
multiplication=a*b
division=a/b
floor_division=a//b
modulus=a%b
power=a**b

print("The sum is : ",sum)
print("The difference is : ",difference)
print("The multiplication is : ",multiplication)
print("The division is : ",division)
print("The floor division is : ",floor_division)
print("The modulus is : ",modulus)
print("the power is: ",power)



# This program demonstrates the use of various operators in Python.

for i in range(1,51):
    print(i,end=" ")


for i in range(1,51):
    if i % 2 == 0:
        print("t",end=" ")
    else:
        print(i,end=" ")


for i in range(1,51):
    if i % 3 == 0:
        print("t",end=" ")
    else:
        print(i,end=" ")


for i in range(1,51):
    if i%3==0 and i%5==0:
        print("fizbuz",end=" ")
    elif i%3==0:
        print("fiz",end=" ")
    elif i%5==0:
        print("buz",end=" ")
    else:
        print(i,end=" ")


# This program calculates the tax based on the income input by the user.

income = float(input("Enter income: "))

if income <= 85528:
    tax = (income * 0.18) - 556.02

    if tax < 0:
        tax = 0

else:
    tax = 14839.02 + (income - 85528) * 0.32

print("The tax is:",tax, "thalers")




# This program determines whether a given year is a leap year or not.

year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")

elif year % 4 != 0:
    print("Common year")

elif year % 100 != 0:
    print("Leap year")

elif year % 400 != 0:
    print("Common year")

else:
    print("Leap year")



for i in range(1,6):
    print(i,"mississipppi")

print("Ready or not,here i come!")



# This program removes vowels from a word input by the user.
user_word=input("Enter the word: ")
user_word=user_word.upper()
word_without_vowels = " "

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter

print("The word without vowels is: ",word_without_vowels) 


for i in range(1,7):
    for j in range(i):
        print(i,end=" ")
    print()

for temp in range(1,7):
    print(str(temp)*temp)