def my_function():
    global var
    var=2
    print("Do I Know That Variable?", var)

var=1
my_function()
print(var)