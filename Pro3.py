from sys import *

def Copy_Content(Fname):
    fd = open(Fname,"r")

    fd_New = open("Demo.txt","w")

    for data in fd:
        fd_New.write(data)

    fd.close()
    fd_New.close()



def main():

    Copy_Content(argv[1])

if __name__ == "__main__":
    main()