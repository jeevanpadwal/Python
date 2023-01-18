import threading

def ChkEven(No):
         
    for i in range(1,No):
        if(i % 2 != 0):
            print("Even number : ",i)

    
            
def ChkOdd(No):
     for i in range(1,No):
        if(i % 2 == 0) and i < 11:
            print("Odd number : ",i)
            
   
    

def main():

    Number = 10

    p1= threading.Thread(target=ChkEven ,args = (Number ,))
    p2= threading.Thread(target= ChkOdd  ,args = (Number ,))

    p1.start()
    p2.start()
    




if __name__ == "__main__":
    main()