def AdditionList(Brr):

    sum =0
    for i in range(0,len(Brr)):
        sum = sum + Brr[i]

    return sum


def main():

    print("Enter number of elements :")
    a = int(input())

    Arr = []
    print("Enter elements")

    for i in range(0,a):
        b = int(input())
        Arr.append(b)

    ret = AdditionList(Arr)
    print("Addition of list elements is:",ret)


if __name__ =="__main__":
    main()