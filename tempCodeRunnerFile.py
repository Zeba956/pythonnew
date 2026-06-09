
class MyZeroDivisionError(ZeroDivisionError):
    pass

def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("Some worse news")
    else:
        raise ZeroDivisionError("Some bad news")
    
do_the_division(False)