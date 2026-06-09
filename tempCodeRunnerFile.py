#09-06-2026
class Super:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "My name is " + self.name + "."
    
class Sub(Super):
    def __init__(self,name):
        pass
        Super.__init__(self,name)
    
obj = Sub("Andy")
print(obj)