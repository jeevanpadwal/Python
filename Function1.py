# Function which accept nothing 

def Demo():
    print("Inside Demo1")

# Function accept one parameter and returns nothing 

def Demo2(No):
    print("Inside Demo2 with argument :",No)

def Demo3(No):
    print("Inside Demo 3",No)
    return No+2

def Demo4(no1,no2):
    print("Inside demo 4")
    ans = no1 + no2
    return ans

# Function accept two parameter and return two parameter
def Demo5(No1,No2):
    Add = No1 + No2
    Sub = No1 - No2
    return Add,Sub

def main():
    Demo()
    Demo2('Hello')

    ans=Demo3(10)
    print("Return value of Demo 3",ans)
    
    Ans1,Ans2 = Demo5(11,10)
    print("First return value",Ans1)
    print("Second retur value",Ans2)


if __name__ == "__main__":
    main()