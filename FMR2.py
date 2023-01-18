def ChkEven(no):
    return (no % 2 ==0)

def Mult(no):
    ans = no * 2
    return ans

def filterX(Helper_Function, Data):
    Result = []
    for no in Data:
        if(Helper_Function(no) == True):
            Result.append(no)
    return Result

def mapX(Helper_Function,Data):
    Result = []
    for no in Data:
        a = Helper_Function(no)
        Result.append(a)
    return Result 

def reduce(Data):
    sum = 0
    for i in Data:
        sum = sum + i
    return sum

def main():

    Data_Input = []
    print("Enter number of element :")
    a = int(input())

    print("Enter the data :")
    for i in range(0,a,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is :",Data_Input)

    Data_Filter = filterX(ChkEven ,Data_Input)
    print("Data after Filter",Data_Filter)

    Data_Map  = mapX(Mult , Data_Filter)
    print("Data after Maping",Data_Map)

    ret = reduce(Data_Map)
    print("Sumation is :",ret)


if __name__ =="__main__":
    main()