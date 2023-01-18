def MinNumber(Brr):

    imax = Brr[0]    
    for i in range(0,len(Brr)):
        if imax > Brr[i]:
            imax = Brr[i]

    return imax


def main():

    print("Enter number of elements :")
    a = int(input())

    Arr = []
    print("Enter elements")

    for i in range(0,a):
        b = int(input())
        Arr.append(b)

    ret = MinNumber(Arr)
    print("Minimum number from the list is:",ret)


if __name__ =="__main__":
    main()