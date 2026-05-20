name = "Zeba"
profession  = "Software Engineer"
experience = 5
print("hello, I am", name, "and I am a", profession, "with", experience, "years of experience.")

x=5
print(type(x))

x=["apple", "banana", "cherry"]
print(x)

x=("apple", "banana", "cherry")
print(x)

x=20
print(x)

x=20.5
print(x)

x=1j
print(x)

x={"name": "Zeba", "age": 30}
print(x)

x=None
print(x)
print(type(x))

x=True
print(x)
print(type(x))

x=b"Hello"
print(x)
print(type(x))

x=memoryview(bytes(5))
print(x)

x=bytearray(5)
print(x)

x=100
y=34
print(x//y)

x=2
y=3
print(x**y)

print(5>>2)

x=1
print(x==1)
print(x==2)

print(x !=1)
print(x !=2)

x=4
print(x<5 and x<10)
print(x>5 or x>10)
print(not(x<5 and x<10))


x=10
y=10
print(x is y)
print(type(x))


x=["Maruti","BMW"]
y=["Maruti","BMW"]
z=x
print(x is z)
print(x is y)

x=["apple", "banana", "cherry"]
y="apple"
print(y in x)

x=input("enter first value: ")
y=input("enter second value: ")
print("the sum is: ", int(x) + int(y))

print("+----------+")
print("|          |")
print("|          |")
print("|          |")
print("|          |")
print("+----------+")

print("+"+"-"*10+"+")
print(("|"+" "*10+"|\n")*5,end="")
print("+"+"-"*10+"+")

number1 = int(input("enter the first number:"))
number2 = int(input("enter the second number:"))

if number1>number2:
    larger_number = number1
else:
    larger_number = number2

print("The Larger number is:", larger_number)


number1 = int(input("enter the first number:"))
number2 = int(input("enter the second number:"))
number3 = int(input("enter the third number:")) 

larger_number = max(number1, number2, number3)  
lowest_number = min(number1, number2, number3)  

# if number2 > larger_number:
#     larger_number = number2 
# if number3 > larger_number:
#     larger_number = number3 

print("The Larger number is:", larger_number)       
print("The Lowest number is:", lowest_number)       



plant = input("Enter plant name: ")

if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")

elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")

else:
    print("Spathiphyllum! Not", plant)


# while True:
#     print("i'm stuck inside a loop.")

i=1
while i<=50:
    print(i)
    i+=1


number=int(input("Enter the number: "))
count = 1
even = 0
odd = 0
while count<=number:
    if count % 2 == 0:
        even += 1
    else:
        odd += 1
    count += 1

print("Even numbers is:", even)
print(" Odd numbers is:", odd)        

#logical expresion
var=10
print(var>0)
print (not(var<=0))

var=6
print(var != 0)
print(not(var == 0))

i=1
j= not not i
print(j)


#list
number=[1,2,3,4,5]
print(number)
print(type(number))

print("first element: ", number[0])

#update especific element
number[0]=111
print("number[0]: ",number[0])
print(number)

number[1]=number[4]
print(number)

del number[3] #delete element at index 3
print(number) 
print(len(number)) #length of list


number=[2,4,6,8,10]
print (number[-1]) #last element
print (number[-2])
print (number[-6]) #index error


#practice question

numbers=[1,2,3,4,5]
print(len(numbers))

del numbers[-1]
print(numbers)

numbers[int(len(numbers)//2)]=80 #update middle element
print(numbers)

list=[1,2,3,4,5]
print(list)
list.append(6) #add element at the end of the list
print(list)

list.insert(0,10) 
print(list)


#module 3

my_list=[1,2,3,4,5,6,7,8,9,10]
for iterator in range(len(my_list)):
    print(my_list[iterator])

#dry run of the above code
'''
iterator   0  1  2  3
output     1  2  3  4

'''

list=[]
for i in range(1,11):
    list.append(i)
print(list)


#update the list by adding 1 to each element
my_list=[10,20,30,40,50,60,70,80,90,100]

for i in range(len(my_list)):
    my_list[i] += 1   #my_list[i] = my_list[i] + 1
print(my_list)



#calculate the sum of all elements in the list
my_list=[10,20,30,40,50,60,70,80,90,100]

sum=0
for i in my_list:
    sum=sum+i
print("The sum is: ",sum)


variable1 = 1
variable2 = 2
print("variable1: ",variable1)
print("variable2: ",variable2)

#swap the values

variable1 = 1
variable2 = 2
variable1,variable2 = variable2,variable1
print("variable1: ",variable1)
print("variable2: ",variable2)


list=[10,20,30,40,50,60,70,80,90,100]
list[4],list[1]=list[1],list[4]
print(list)




lst=[1,2,3,4,5]
lst_2=[]
add=0
for number in lst:
    add += number
    lst_2.append(add)
print(lst_2)
print(lst)


print("Testing commit changes")



#bubble sort

my_list=[8,10,6,2,4]
swapped = True
count = 0
index=0
while swapped:
    swapped = False
    for i in range(len(my_list)-1-index):
        index = i
        count += 1
        if my_list[i] > my_list[i+1]:
            swapped = True
            my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
print(my_list)
print(count)


#built in sort function
my_list=[8,10,6,2,4]
my_list.sort()
print(my_list)