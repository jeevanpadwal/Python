def Display(iNo):

    for i in range(1,iNo+1):
        for j in range(1,iNo+1):
            if i >= j:
                print(j, end =" ")
        print(' ')
        
        


def main():
    print("Enter number")
    a = int(input())

    Display(a)

if __name__ == "__main__":
    main()