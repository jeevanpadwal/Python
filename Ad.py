
from sys import *


def Add(a,b):
    c= a+b
    print(c)


def main():

    if argv[1] == "--U":
        print("Use of code for addition of number ")
        print("python name_of_application no1_no2")

    if len(argv) != 3:
        print("Invalid Number of Arguments")
        exit()

    Add(int(argv[1]),int(argv[2]))
   
   
    

if __name__ == "__main__":
    main()
