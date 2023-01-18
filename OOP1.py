

class Arithmatic:
    
    def __init__(self,A,B):
        print("Inside init mathod")
        self.No1 = A
        self.No2 = B
    
    def Add(self):
        ans = self.No1 + self.No2
        return ans

    def Sub(self):
        ans = self.No1 - self.No2
        return ans




def main():
    print("Inside main method")

    obj = Arithmatic(11,10)

    ret = obj.Add()
    print("Addition is :",ret)

    
    ret = obj.Sub()
    print("Substraction is :",ret)

    



if __name__ == "__main__":
    print("Inside starter")
    main()