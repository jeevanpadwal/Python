import os

def Display_Data(Fname):
    fd = open(Fname,"r")
    print(fd.read())

def main():
    print("Enter the file name :")
    fname = input()

    Display_Data(fname)

if __name__ =="__main__":
    main()