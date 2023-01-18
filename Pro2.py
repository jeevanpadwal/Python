
import threading

def EvenFactor(No):
    Sum = 0
    for i in range(1,No):
        if No % i == 0 and i % 2 == 0:
            Sum = Sum + i

    print("Addition of Even Factors :",Sum)

            
def OddFactor(No):
    Sum = 0 
    for i in range(1,No):
        if(No % i == 0)and(i % 2 != 0):
            Sum = Sum + i
    
    print(" Addition of Odd Factors : ",Sum)
   
    

def main():

    Number = 10

    p1= threading.Thread(target= EvenFactor ,args = (Number ,))
    p2= threading.Thread(target= OddFactor  ,args = (Number ,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

    print("Exit from main")




if __name__ == "__main__":
    main()