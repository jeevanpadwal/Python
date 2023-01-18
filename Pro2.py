Multiplication = lambda ino ,ino2 : ino*ino2 

def main():
    print("Enter first number :")
    a = int(input())

    print("Enter second number :")
    b = int(input())

    ret  = Multiplication(a, b)
    print("Multiplication of number :",ret)


if __name__ == "__main__":
    main()