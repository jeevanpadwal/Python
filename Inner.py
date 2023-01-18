def Demo():
        print("Inside demo")

def Fun():
    print("Inside fun")

def Hello(FPTR):
    print("Inside hello")
    FPTR()   

Hello(Demo)
Hello(Fun)
