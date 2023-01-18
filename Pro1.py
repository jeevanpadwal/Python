Power = lambda ino : ino**2 

def main():
    print("Enter number :")
    a = int(input())

    ret  = Power(a)
    print("power of number :",ret)


if __name__ == "__main__":
    main()