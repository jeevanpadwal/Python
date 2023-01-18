def MaxNumber(Brr):

    imax = 0    
    for i in range(0,len(Brr)):
        if imax < Brr[i]:
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

    ret = MaxNumber(Arr)
    print("Maximum number from the list is:",ret)


if __name__ =="__main__":
    main()