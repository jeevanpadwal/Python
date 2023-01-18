def Factor(iNo):
    
    print("Factors Are :")
    for i in range(1,int(iNo/2)+1):
        if iNo % i == 0:
           print(i)

        
def FactorWhile(iNo):
    i = 1
    while( i <= int(iNo/2)):
        if((iNo % i) == 0):
            print(i)
        i = i + 1
