import os


def Delete_File(FileName):
    if(os.path.exists(FileName)):

        os.remove(FileName)
        print("File Deleted susessfully...")
    else:
        print("File is not existing")
        return

def main():
    print("Enter the file name to delete")
    Name = input()

    Delete_File(Name)


if __name__ =="__main__":
    main()