
import threading

def EvenFactor(LData):
    Sum = 0
    for i in LData:
        if i % 2 == 0:
            Sum = Sum + i

    print("Addition of Even Numbers from list :",Sum)

            
def OddFactor(LData):
    Sum = 0 
    for i in LData:
        if i % 2 != 0:
            Sum = Sum + i
    
    print(" Addition of Odd Numbers from list : ",Sum)
   
    

def main():

    print("How many element you want to add")
    a = int(input())

    List = []

    print("enter the elements ")
    for i in range(1,a + 1):
        b= int(input())
        List.append(b)



    evenList = threading.Thread(target= EvenFactor ,args = (List ,))
    OddList = threading.Thread(target= OddFactor  ,args = (List ,))

    evenList.start()
    OddList.start()
    
    evenList.join()
    OddList.join()

    print("Exit from main")




if __name__ == "__main__":
    main()
