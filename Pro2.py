from sys import *
from os import *

def DirectoryFileSearch(Fname,AlreadyExten,ChangeExten):

    for files in listdir(Fname):
        Apath = path.join(Fname,files)  

        oldname = path.splitext(files)

        newname = Apath.replace(AlreadyExten,ChangeExten)

        output = rename(Apath,newname)

    print("All the file extentions of "+AlreadyExten+" replace with "+ChangeExten)


def main():
    
    if(len(argv) != 4):
        print("Use -h for help and use -u for usage of the script ")
        print("Error :Insufficient argument")
        exit()

    if argv[1] == "-h" or argv[1] == "-H":
        print("This script use to change extention with given extention")
        exit()

    if(argv[1]=="-u" or argv[1] =="-U"):
        print("Usage : Application_Name Directory_Name Extention")
        exit()

    else:
    
        DirectoryFileSearch(argv[1],argv[2],argv[3])

if __name__ =="__main__":
    main()