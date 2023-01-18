import os
from sys import *

def Chk_Str(Fname ,Str1):

    fd = open(Fname,"r")

    string = fd.read()

    Cnt = string.count(Str1)
    
    print("Number of occurance of string is :",Cnt)



def main():
    print("Enter file Name :")
    fname = input()

    print("Enter string :")
    str = input()

    Chk_Str(fname,str)

if __name__ == "__main__":
    main()