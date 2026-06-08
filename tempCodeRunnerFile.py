class ExampleClass:
    counter = 0
    def __init__(self,val = 1):
        ExampleClass.counter += 1
        if val % 2 != 0:
            self.a = val
        else:
            self.b = val

example_object = ExampleClass(1)
print(example_object.a)
# print(example_object.b)


#Exception Handling

try:
    print("b = ", example_object.b)
except AttributeError:
    pass