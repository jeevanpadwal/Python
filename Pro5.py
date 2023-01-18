import MarvellousNum       

def main():

    print("Enter number of elements :")
    a = int(input())

    Arr = []
    print("Enter elements")

    for i in range(0,a):
        b = int(input())
        Arr.append(b)
     
    ret =MarvellousNum.ChkPrime(Arr)
    print("Prime numbers Addition is:",ret)


if __name__ =="__main__":
    main()