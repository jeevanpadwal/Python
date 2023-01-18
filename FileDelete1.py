import os


def Delete_File(FileName):
    if(os.path.exists(FileName)):
        size = os.path.getsize(FileName)

        if(size == 0):
            os.remove(FileName)
            print("File Deleted susessfully...")

        else:
            print("Are you sure to delete the file ? Y/N")
            option = input()
            if(option == "Y" or option == "y"):
                os.remove(FileName)
                print("File Deleted susessfully...")
            else:
                print("There is no such file")
    else:
        print("File is not existing")
        return

def main():
    print("Enter the file name to delete")
    Name = input()

    Delete_File(Name)


if __name__ =="__main__":
    main()