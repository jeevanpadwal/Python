# even in lambda

def Even(no1):
    if(no1 % 2 == 0):
        return True
    else:
        return False


EvenL = lambda a : a % 2 == 0

ret = Even(10)
ret1 = EvenL(10)

if(ret1 == True):
    print("Even number")
else:
    print("Its odd")


