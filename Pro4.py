from sys import *
import os
import filecmp

def Compare_Data(Fname1,Fname2):
    ret = filecmp.cmp(Fname1,Fname2, shallow = False)

    if ret == True:
        print("Success")

    else:
        print("Failure")

def main():

    Compare_Data(argv[1],argv[2])

if __name__ == "__main__":
    main()