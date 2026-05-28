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