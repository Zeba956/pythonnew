
def my_function(n):
    if n==1:
        return
    print(n,end=" ")
    my_function(n-1)#recursive call
my_function(5)
