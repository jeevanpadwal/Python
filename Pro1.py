from sys import *
from os import *

def DirectoryFileSearch(Fname,Extention):
    
    list_of_file = []

    for files in listdir(Fname):
        if files.endswith(Extention):
            list_of_file.append(files)

    print("List of file is :",list_of_file)



def main():
    
    if(len(argv) != 3):
        print("Use -h for help and use -u for usage of the script ")
        print("Error :Insufficient argument")
        exit()

    if argv[1] == "-h" or argv[1] == "-H":
        print("This script use to display all file of given extentio")
        exit()

    if(argv[1]=="-u" or argv[1] =="-U"):
        print("Usage : Application_Name Directory_Name Extention")
        exit()

    else:
    
        DirectoryFileSearch(argv[1],argv[2])

if __name__ =="__main__":
    main()