#Positional argumets/keyword arguments
def Add1(No1,No2):
    print("value of no1 :",No1)
    print("value of no1 :",No2)

    return No1 + No2

def Sub1(No1,No2):
    print("value of no1 :",No1)
    print("value of no1 :",No2)

    return No1 - No2


def main():

    Ans= Add1(10,11)
    print("Addtion of Add1 is",Ans)

    Ans= Sub1(No2 = 10,No1 = 11)
    print("Sub  of Sub1 by Keyword argument is",Ans)

if __name__ == "__main__":
    main()