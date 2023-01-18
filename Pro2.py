class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name =""
        self.Amount = 0
        self.Accept()
    
    def Accept(self):
        print("Etner name of Account Holder")
        self.Name = input()

        print("Etner Initial Amount")
        self.Amount = int(input())

    def Display(self):
        print("Name :",self.Name)
        print("Amount ",self.Amount)

    def Deposite(self):

        print("Enter amount to be deposite :")
        a = int(input())

        self.Amount = self.Amount + a

    def Withdraw(self):

        print("Enter amount for withdraw :")
        a = int(input())

        self.Amount = self.Amount - a

    def CalculateIntreast(self):

        Intrest = (self.Amount * BankAccount.ROI * 1) / 100

        print("------------------------------------------------------------")
        print("Intrest for 1 Year on Your Current Amount is :",Intrest)
        print("Your amount after adding intrest will be :",self.Amount + Intrest)
        print("-------------------------------------------------------------")



def main():

    obj1 = BankAccount()

    obj1.Deposite()
    obj1.Withdraw()
    obj1.CalculateIntreast()
    obj1.Display()

if __name__ == "__main__":
    main()