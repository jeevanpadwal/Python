print("Application to demonstrate Industrial PRograming")

def Addition(Value1,Value2):
    ans = Value1 + Value2
    return ans


def main():
   
    print("Enter first number: ")
    no1 = int(input())

    print("Enter second number :")
    no2 = int(input()) 
    
    ans= Addition(no1,no2)
    print("Addition is :",ans)

if __name__ == "__main__":
    main()

