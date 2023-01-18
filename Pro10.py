def Length(iNo):

    Add =0

    while (iNo != 0):

        Add = Add +(iNo %10) 
        iNo = iNo//10

    return Add

    

def main():
    print("Enter number :")
    a= int(input())

    b= Length(a)
    print("Addition of Digit is :",b)

if __name__ == "__main__":
    main()