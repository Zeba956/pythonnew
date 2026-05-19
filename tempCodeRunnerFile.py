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