
def Increase(ino):
    return ino + 10

def Greater(ino):
    return ino >= 70 and ino <= 90
        
def filterX(Function_Name,Data):

    Result =[]

    for i in Data:
        if(Function_Name(i) == True):
            Result.append(i)
    
    return Result

def mapX(Function_Name, Data):
    Result = []

    for i in Data:
        value = Function_Name(i)
        Result.append(value)
    
    return Result

def reduceX(Data):

    iMult = 1 

    for i in Data:
        iMult = i*iMult
    

    return iMult



def main():

    print("Enter number of elements for list :")
    a = int(input())

    Input = []

    print("Etner elements :")
    
    for i in range(0,a,1):
        b = int(input())
        Input.append(b)

    print(Input)

    Filter_Data = filterX(Greater ,Input)

    print("Data after filter ",Filter_Data)

    Map_Data = mapX(Increase , Filter_Data)

    print("Data after maping ",Map_Data)

    ret = reduceX(Map_Data)

    print("Multiplication of maped data",ret)



if __name__ == "__main__":
    main()