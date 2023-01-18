# accept n number from user and return the addition of that number 

class Numbers:
    def __init__(self):
        self.size = 0
        self.Arr = list()
        self.Accept()

    def Accept(self):
        print("enter how many elemnets you want :")
        self.size = int(input())

        print("Enter the elements :")
        value = 0

        for i in range(0,self.size):
            value = int(input())
            self.Arr.append(value)

    

    def Display(self):

        print("Elements from list is :")

        for i in range(0,self.size):
            print(self.Arr[i])


    def Summation(self):
        sum =0 
        for i in range(0,self.size):
            sum = sum + self.Arr[i]

        return sum

    def Max(self):

        imax = 0
        for i in range(0,self.size):
            if imax < self.Arr[i]:
                imax = self.Arr[i]
        
        return imax

    def Min(self):

        imax = self.Arr[0]
        for i in range(0,self.size):
            if imax > self.Arr[i]:
                imax = self.Arr[i]
        
        return imax

def main():
    obj = Numbers()

    
    output = obj.Summation()
    obj.Display()
    print("Sumation of element is :",output)

    output = obj.Max()
    print("Maximum element is",output)

    output = obj.Min()
    print("Minimum element is",output)


if __name__ =="__main__":
    main()