print("Application to demonstrate Industrial PRograming")

import G1module

def main():
    print("Vale of __name__ from main is:",__name__)
   
    print("Enter first number: ")
    no1 = int(input())

    print("Enter second number :")
    no2 = int(input()) 
    
    ans= G1module.Addition(no1,no2)
    print("Addition is :",ans)

if __name__ == "__main__":
    main()

