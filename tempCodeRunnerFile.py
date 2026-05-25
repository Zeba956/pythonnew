def strange_list_fun(n):
    strange_list=[]

    for i in range(0,n):
        #strange_list.insert(0,i+1)
        strange_list.append(i+1)

    return strange_list
print(strange_list_fun(5))