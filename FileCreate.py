def CreatFile(FileName):
    fd = open(FileName,"w")

def main():
    print("Enter the file name to create")
    Name = input()

    CreatFile(Name)


if __name__ =="__main__":
    main()