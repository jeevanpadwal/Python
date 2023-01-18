def Add(*Values):
    print(type(Values))
    print("Number of arguments ",len(Values))

    a = 0
    for i in Values:
        a = a + i

    return a

def AddX(*Values):
    print(type(Values))
    print("Number of arguments ",len(Values))

    a = 0
    for i in range(0,len(Values),1):
        a = a + Values[i]

    return a

    

def main():
    ans = Add(4,5,6,1,2,3,65)
    print("Addition is ",ans)

    ans1 = AddX(4,5,6,1,2,3,65)
    print("Addition is ",ans1)


if __name__ == "__main__":
    main()