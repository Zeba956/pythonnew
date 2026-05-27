
var=123
t1=(1, )
t2=(2, )
t3=(3,var)

t1,t2,t3=t2,t3,t1
print(t1)
print(t2)
print(t3)
print(type(t1),type(t2),type(t3))