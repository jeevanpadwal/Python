import os
from sys import *
import shutil

def CopyDirectoryData(Old_Dirname,New_Dirname,Extention):

    for files in os.listdir(Old_Dirname):
        os.mkdir(New_Dirname)
        src = New_Dirname + files


        try:

            os.path.join(Old_Dirname,files)
            if files.endswith(Extention):
                
                print("After making directory")
                print("Extention :",Extention)
                print("Old Directoy",Old_Dirname)
                
                print("New Directory",New_Dirname)
                shutil.copy(Old_Dirname,src)
                print("Copyed")
        except:
            pass
def main():

    if(len(argv) != 4):
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
    
        CopyDirectoryData(argv[1],argv[2],argv[3])

if __name__ == "__main__":
    main()