#accept two number and perform addition and substraction in it 
# object oriented programing python 
# class = Data + Functions 

class Arithmatic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Add(self):
        return self.No1+self.No2

    def Sub(self):
        return self.No1 - self.No2

def main():
    print("Enter first")
    a = int(input())

    print("Enter second")
    b = int(input())

    obj = Arithmatic(a,b)

    Ans = obj.Add()
    print("Addition is",Ans)

    Ans = obj.Sub()
    print("Subsrtaction is",Ans)


if __name__ =="__main__":
    main()
    