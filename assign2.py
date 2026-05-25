#There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
# Your task is to:
# write a line of code that prints the length of the existing list (Step 1).
# write a line of code that removes the last element from the list (Step 2)
# write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 3)

hat_list=[1,2,3,4,5]
print(len(hat_list))

del hat_list[-1]
print(hat_list)

middle = len(hat_list) // 2
hat_list[middle] = int(input("Enter a number: "))
print(hat_list)


# The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
# The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
# Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.

beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")


for member in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(member)
print(beatles)


del beatles[-1]
del beatles[-1]

beatles.insert(0, "Ringo Starr")
print(beatles)




# Write a program that counts the number of digits in a string. For example, if the string is "Mindcoders password2 is : 1234", the output should be 5.
string="Mindcoders password2 is : 1234"
count=0
for ch in string:
    if ch.isdigit():
        count += 1
print("Number of digits in the string: ", count)



string = "U r a a n S 0 f t s k i l l 1 s 1234"

count = 0

for ch in string:
    if ch.isdigit():
        count += 1

print("Total number of Digits =", count)




string = "MindCoders"

count = 0

for ch in string:
    if ch == 's' or ch == 'S':
        count += 1

print(count)




string = "UraanSoftskills"
checked = ""

for ch in string:
    if ch not in checked:
        print(ch, "=", string.count(ch))
        checked += ch




for i in range(1,11):
    print(i)


for i in range(1,11):
    if i%2 == 0:
        print(i)


sum=0
for i in range(1,11):
    sum += i
print("The sum is: ",sum)



sum=0
for i in range(1,16):
    if i%2 != 0:
        sum += i
print("The sum is: ",sum)



for i in range(1,11):
    print("15 x",i,"=",15*i)


numbers = [1, 2, 4, 6, 88, 125]

for i in numbers:
    print(i)



number = 129475
count = len(str(number))
print(count)




string = "madam"

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")




word = input("Enter a word: ")

print(word[::-1])




number = 153

sum = 0
temp = number

while temp > 0:

    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10

if sum == number:
    print("Armstrong Number")
else:
    print("Not Armstrong")