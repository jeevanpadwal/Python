import os
from sys import *
import shutil

def CopyDirectoryData(Old_Dirname,New_Dirname):

    for files in os.listdir(Old_Dirname):

        try:

            os.path.join(Old_Dirname,files)
            shutil.copytree(Old_Dirname,New_Dirname)
        except:
            pass
def main():

    if(len(argv) != 3):
        print("Enter -h for help and -u for usage of script")
        print("Error : Insuuficent Argument")
        exit()
    
    if argv[1] == "-h" or argv[1] == "-H":
        print("This script use to copy all files from one file to other directory")

        exit()

    if(argv[1]=="-u" or argv[1] =="-U"):
        print("Usage : Application_Name Directory_Name Dirctory_Name_which_want_to_create")
        exit()

    else:
    
        CopyDirectoryData(argv[1],argv[2])

if __name__ == "__main__":
    main()