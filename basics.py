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



my_list.reverse()#reverse the list
print(my_list)

list_1=[1]
list_2=list_1[:]#create a copy of list_1
list_1[0]=2
print(list_2)
print(list_1)



my_list=[1,2,3,4,5]
new_list=my_list[1:3]
#new_list=my_list[-1:1]
#new_list=my_list[1:-1]
#new_list=my_list[-5:3]
#new_list=my_list[:3]
#new_list=my_list[2:]
print(new_list) 

del my_list[1:3] #delete elements from index 1 to 2
print(my_list)

#del my_list #delete the entire list

del my_list[:] #delete all elements in the list
print(my_list)



my_list=[0,3,12,8,2]
print(5 in my_list)
print(3 in my_list) 
print(5 not in my_list) 



#selection sort
my_list = [8, 10, 6, 2, 4]
n=len(my_list)
count=0
for i in range(n):
    min_index=i
    count += 1

    for j in range(i+1,n):
        if my_list[j]<my_list[min_index]:
            min_index=j

    my_list[i],my_list[min_index]=my_list[min_index],my_list[i]
print(my_list)
print(count)

#list comprehension

# row=[]
# for i in range(8):
#     row.append("WHITE_PAWN")
row=["WHITE_PAWN" for i in range(8)] 
print(row)

squares=[x**2 for x in range(10)]
print(squares)

squares=[index ** 2 for index in range(1,11)]
odds=[x for x in squares if x % 2!=0]
print(odds)


#two dimensional list
board=[]
for i in range(8):
    row=["EMPTY"for i in range(8)]
    board.append(row)
#print(board)

for index in board:
    print(index)
print(len(board))

board[0][0]= "Rook"
board[0][7]= "Rook"
board[7][0]= "Rook"
board[7][7]= "Rook"
board[0][1]= "Knight"
board[0][6]= "Knight"
board[7][1]= "Knight"
board[7][6]= "Knight"


for index in board:
    print(index)

#multidimensional list comprehension

temps=[[0.0 for h in range(24)] for d in range(31)]

temp1=19
temp2=32
count=0
for days in temps:
    if count == 0:
        days[11]=temp1
        count=1
    else:
        days[11]=temp2
        count=0

    
for element in temps:
    print (element)

total = 0.0
for day in temps:
    total += day[11]
average = total/31
print("Average temperature at noon: ",average)


highest = -100.0
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
print("Highest temperature: ", highest)


hot_days = 0
for days in temps:
    if day[11] > 20.0:
        hot_days +=1
print(hot_days, "days were hot days in the month.")

#question 2 3D list comprehension
rooms=[[[False for r in range(20)]for f in range(15)] for t in range(3)]
print(rooms)
rooms[1][9][13]=True
rooms[1][9][1]=True

vacancy = 0
for room_number in range(20):
    if not rooms[1][9][room_number]:
        vacancy += 1
print("vacancy in 3rd 15th floor of 3rd building: ", vacancy)


#left shift operator
var=1
while var<10:
    print("#")
    var = var << 1



a=1
b=0
c=a&b
d=a|b
e=a^b
print(c+d+e)





#function

def message():
    print("Enter the value: ")
print("Step 1")

message() #call the function
a=int(input())
print("Step 2")

message()
b=int(input())
print("Step 3")

message()
c=int(input())





def message():
    print("Enter the value: ")

#message=1
print("We start here.")
print(message)
message()
print("We end here.")


#function with return value
def message():
    print("Enter the value: ")
    temp=int(input())
    return temp

print("Step 1")
a=message() 

print("Step 2")
b=message()

print("Step 3")
c=message()

print("a: ",a )
print("b: ",b )
print("c: ",c )



def hello(n):#defining a function 
    print("Hello,", n)#body of the function

name = input("Enter your name: ")
hello(name)#call the function with argument name




def message(number):
    print("Enter a number:",number)

number=1234
message(1)
print(number)



def message(what, number):
    print("Enter", what, "number", number)

message("telephone",11)
message(11,"telephone")#this will not give error but it will print the arguments in the order they are passed in the function call.
message("price",5)
message("number","number")




def introduction(first_name,last_name):
    print("Hello, my name is" , first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse","Quick")
introduction("Clark","Kent")


introduction(last_name="Bond", first_name="James")#keyword arguments
introduction(first_name="Luke", last_name="Skywalker")



def adding(a,b,c):
    print(a,"+",b,"+",c,"=",a+b+c)

adding(1,2,3)
adding(c=1,b=2,a=3)
adding(3,c=1,b=2)
adding(3,a=1,b=2)#this will give error because positional argument a is passed after keyword argument c and b. positional arguments should be passed before keyword arguments.


def happy_new_year(wishes=True):
    print("Three..")
    print("Two..")
    print("One..")
    if not wishes:
        return
    print("Happy New Year!")

happy_new_year()#this will print the countdown and the message "Happy New Year!"
happy_new_year(wishes=False)#this will print the countdown but not the message "Happy New Year!" because the function will return before printing the message.



def boring_function():
    print(" 'Boredom Mode' ON")
    return 123
print("this lesson is interesting!")
boring_function()
print("This lesson is boring...")



def checkMyVar(variable):
    if(variable==10):
        print("variable is 10")
        return 2
    else:
        print("variable is not up to the mark")
        return

checkMyVar(10)
print()

print(checkMyVar(5))#it print false bcz function is print inside the function and it return None if the condition is not satisfied. so it will print None when we call the function with argument 5.



def list_sum(lst):
    s=0
    for element in lst:
        s += element    
    return s
print(list_sum([5,4,3]))



def strange_list_fun(n):
    strange_list=[]

    for i in range(0,n):
        #strange_list.insert(0,i+1)
        strange_list.append(i+1)

    return strange_list
print(strange_list_fun(5))



def scope_test():
    x=123
scope_test()
print(x)#x is not define so the output will be error


def my_function():
    print("Do I know that variable?",var)

var=1
my_function()
print(var)


#shadow variable

def mult(x):
    var=7
    return x * var

var=3
print(mult(7))



def my_function():
    global var
    var=2
    print("Do I Know That Variable?", var)

var=1
my_function()
print(var)


#global variable
var=2
print(var)#output:2

def return_var():
    global var
    var=5
    return var

print(return_var())#output:5
print(var)



def my_function(n):
    print("I got",n)
    n+=1
    print("I have",n)

var=1
my_function(var)
print(var)


#how function interacts with its arguments

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1=[0,1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2=[2,3]
my_function(my_list_2)
print("Print #5:", my_list_2)



def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]#this will delete the first element of the list my_list_1 and it will also affect the list my_list_2 because both my_list_1 and my_list_2 are pointing to the same list in memory.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2=[2,3]
my_function(my_list_2)
print("Print #5:", my_list_2)



def my_function(n):
    if n==0:
        return
    print(n,end=" ")
    my_function(n-1)#recursive call
my_function(5)


#recursive function to count down from a number to 0
def countDown(number):
    print(number)
    if number == 0:
        return
    else:
        print("Going in rec: ",number)
        countDown(number-1)
        print("Out of rec: ",number)
print("Starting Recursion")
countDown(5)
print("Recursion ended")



#factorial of a number using recursion
def factorial(n):
    if n == 1:      # base condition
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))


#Tuple

my_tuple=(1,10,100)

t1= my_tuple + (1000,10000)
t2= my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


tuple_1=(1,2,3)
for element in tuple_1:
    print(element)

tuple_2=(1,2,3,4)
print(5 in tuple_2)
print(5 not in tuple_2)

tuple_3=(1,2,3,4)
print(len(tuple_3))
print(5 not in tuple_3)

tuple_4=tuple_1+tuple_2
print(tuple_4)
tuple_5=tuple_3*2 #this will repeat the elements of tuple_3 two times and create a new tuple with the repeated elements.
print(tuple_5)




my_tuple=tuple((1,2,"String"))
print(my_tuple)
print(type(my_tuple))

my_list=[2,4,6]
print(my_list)
print(type(my_list))

tup=tuple(my_list)#this will convert the list my_list into a tuple and assign it to the variable tup.
print(tup)
print(type(tup))



var=123
t1=(1, )
t2=(2, )
t3=(3,var)

t1,t2,t3=t2,t3,t1
print(t1)
print(t2)
print(t3)
print(type(t1),type(t2),type(t3))


#Dictionary

dictionary = {
"cat":"chat",
"dog":"chien",
"horse":"cheval"        
}

phone_numbers={'boss':5551234567, 'Suzy':5559876543}
empty_dictionary={}

print(dictionary)
print(type(dictionary))
print(phone_numbers)
print(type(phone_numbers))
print(empty_dictionary)
print(type(empty_dictionary))


print(dictionary["cat"])
print(phone_numbers['boss'])

#print(phone_numbers['president'])#this will give error because president is not a key in the dictionary phone_numbers.KeyError: 'president'


words=['cat','lion','horse']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word,"is not in dictionary")


print(dictionary.keys())

for key in dictionary.keys():
    print(key,"->", dictionary[key])

print(dictionary.items())
for key , value in dictionary.items():#this will return a list of tuples where each tuple contains a key and its corresponding value in the dictionary.
    print(key,"->", value)


print(dictionary.values())
for value in dictionary.values():
    print(value)


#copying a dictionary
pol_eng_dictionary={
    "zamek":"castle",
    "woda":"water",
    "gleba":"soil",
}
print("Polish-English Dictionary: ", pol_eng_dictionary)
copy_dictionary=pol_eng_dictionary.copy()#this will create a copy of the dictionary pol_eng_dictionary and assign it to the variable copy_dictionary.

print("copy_dictionary: ",copy_dictionary)



#update the dictionary
pol_eng_dictionary["zamek"]="lock"
item=pol_eng_dictionary["zamek"]
print(item)



phonebook={}
print(phonebook)
phonebook["Adam"]=5551234567#create/add a key value pair 
print(phonebook)

del phonebook["Adam"]#this will delete the key "Adam" and its corresponding value from the dictionary phonebook.
print(phonebook)



#popitem method

pol_eng_dictionary={"kwist":"flower"}
pol_eng_dictionary.update(
    {
        "gleba":"soil"
    })
print(pol_eng_dictionary)

pol_eng_dictionary.popitem()#this will remove the last key value pair from the dictionary pol_eng_dictionary and return it as a tuple.
print(pol_eng_dictionary)


print(pol_eng_dictionary)
print(len(pol_eng_dictionary))

del pol_eng_dictionary["zamek"]
print(pol_eng_dictionary)
print(len(pol_eng_dictionary))

pol_eng_dictionary.clear()
print(pol_eng_dictionary)
print(len(pol_eng_dictionary))

del pol_eng_dictionary
print(pol_eng_dictionary)



sd={}

while True:
    name=input("Enter Student's Name: ")
    if name== " ":
        break
    score=int(input(f"Enter ${name}'s score: "))

    if score not in range(1,11):
        break
    if name in sd:
        sd[name] += (score, )
    else:
        sd[name] = (score, )

# for mark in sd:
#     print(mark)

print(sd)

for name,mark in sd.items():
    sum=0
    #print(name,"->")
    for m in mark:
        #print(m)
        sum += m
    print(name,"->",sum/len(mark))



