# Instance Variable : Name, Amount, Address,Account Number
# Instancr Method : CreateAccount()

# Class Variable : ROI, Bank Name
# Class Method : Display Bank information 

# Static Method : Display KYC Info

class Bank_Account:

    Bank_Name = "HDFC Bank Pvt Ltd"
    ROI_On_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Ammount = 0
        self.Address = ""
        self.AccountNo = 0


    def CreatAccount(self):
        print("Enter your name")
        self.Name = input()

        print("Enter your initial amount")
        self.Amount = int(input())

        print("Enter your Address")
        self.Address = input()

        print("Enter your Account Number")
        self.AccountNo = int(input())


    def DisplayAccountInfo(self):
        print("____________Your Account Information is as below___________")
        print("Name :",self.Name)
        print("Account Amount :",self.Amount)
        print("Address :",self.Address)
        print("Account Number :",self.AccountNo)

    def Deposit(self,Value):
        self.Amount = self.Amount + Value

    def Withdraw(self,Value):
        self.Amount = self.Amount - Value



    @classmethod
    def DisplayBankInformation(cls):
        print("Welcom to banking console",)
        print("Name of our bank is :",cls.Bank_Name)
        print("Rate of intrest we offer on fixed deposite is :",cls.ROI_On_FD)


    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC information ")
        print("According to rules of Gov. Of india you have to submit below documents ")
        print("1 :Clear and recent passport size photo")
        print("2 : Photo of addher card ")
        print("3 : Photo of PAN card")

def main():
   
    Bank_Account.DisplayKYCInfo()

    Bank_Account.DisplayBankInformation()

    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating First Account")
    User1.CreatAccount()

    print("Creating Second Account")
    User2.CreatAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

    User1.Deposit(500)
    User2.Deposit(500)

    print("Amount of {} user1 after deposite {}:".format(User1.Name,User1.Amount))
    print("Amount of {} user2 after deposite {}:".format(User2.Name,User2.Amount))

    User1.Withdraw(10)
    User2.Withdraw(50)

    print("Amount of user1 after witdraw :",User1.Amount)
    print("Amount of user2 after deposite :",User2.Amount)



if __name__ =="__main__":
    main()