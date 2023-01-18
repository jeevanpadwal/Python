def Frequency(Brr,No):

    isum =0  
    for i in range(0,len(Brr)):
        if Brr[i] == No:
            isum = isum + 1
            

    return isum


def main():

    print("Enter number of elements :")
    a = int(input())

    Arr = []
    print("Enter elements")

    for i in range(0,a):
        b = int(input())
        Arr.append(b)

    print("Enter number to find frequence :")
    c = int(input())

    ret = Frequency(Arr,c)
    print("Frequency of the number is :",ret)


if __name__ =="__main__":
    main()