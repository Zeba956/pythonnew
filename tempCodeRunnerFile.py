def reciprocal(n):
    try:
        n= 1/n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went well")
        return n
    
print("---------")
print("reciprocal(2):", reciprocal(2))
print("---------")
print("reciprocal(0):", reciprocal(0))
print("---------")