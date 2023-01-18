# accetp no and tell perfect or not 

class Value:
    def __init__(self,Data):
        self.No = Data

    def SumFactor(self):
        sum = 0
      

        for i in range(1,self.No):
            if(self.No % i == 0):
                sum = sum + i
              

        return sum 


    def ChkPerfect(self):
        Ans = self.SumFactor()

        if(self.No == Ans):
            return True
        
        else:
            return False


    def ChkPrime(self):
        i = 0

        Flage = True

        for i in range(2, int(self.No /2)+1):
            if(self.No % 1 == 0):
                Flage = False
                
            
        return Flage
        
   

def main():

    print("please enter number")
    A = int(input())

    obj = Value(A)

    ret = obj.ChkPerfect()

    if(ret == True):
        print("Perfect Number")

    else:
        print("Not Perfect ")


    ret = obj.ChkPrime()

    if(ret == True):
        print("Prime Number")

    else:
        print("Not Prime")




if __name__ =="__main__":
    main()