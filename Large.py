def Largest(no1, no2):

    if no1 > no2:
        return no1

    else:
        return no2
    

def main():
     print("Enter First no:")
     no1 = int(input())

     print("Enter Second number:")
     no2 = int(input())

     ret = Largest(int(no1),int(no2))
     print("Largest number is :",ret)



if __name__ == "__main__":
    main()
   


