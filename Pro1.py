def Display(No):
    
    if (No > 0):
        print("*",end ="    ")
    
        Display(No - 1)


def main():
    
    a = int(input("Enter number :"))

    Display(a)


if __name__ == "__main__":
    main()