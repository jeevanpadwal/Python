class Numbers:

    def __init__(self,A):
        self.Value = A

    def ChkPrime(self):
        Flage = False
        if(self.Value % 2 == 0):
            return False

        for i in range(2,self.Value):
            if (self.Value % i == 0):
                Flage = False

            else:
                Flage = True

        return Flage
                
    def ChkPerfect(self):
        sum =0
        
        for i in range(1,self.Value):
            if(self.Value % i == 0 ):
                sum = sum + i
        

        if(sum == self.Value):
            return True
        else:
            return False

    def SumFactors(self):
        sum =0
        
        for i in range(1,self.Value):
            if(self.Value % i == 0 ):
                sum = sum + i

        return sum
        
    def Factors(self):
        
        print("-------------------Factors-------------------")
        for i in range(1,self.Value):
            if(self.Value % i == 0 ):
                print(i)
                
        

        return sum



def main():

    print("Enter Number")
    a = int(input())

    obj1 = Numbers(a)
    ret = obj1.ChkPrime()
    print("Prime number Cheak :",ret)

    ret = obj1.ChkPerfect()
    print("Perfect number Cheak :",ret)

    ret = obj1.SumFactors()
    print("Sum of Factors:",ret)

    obj1.Factors()


if __name__ == "__main__":
    main()