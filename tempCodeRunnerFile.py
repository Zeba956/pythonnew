

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