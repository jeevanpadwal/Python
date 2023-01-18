# filter map reduce 

def CheakEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No + 2

def filterX(Arr,Function_Name):
    Result = []
    for no in Arr:
        if(Function_Name(no)):
            Result.append(no)
    return Result

def mapX(Arr,Function_Name):
    Result = []
    for no in Arr:
        value = Function_Name(no)
        Result.append(value)
    return Result

def reduceX(Arr):
    sum =0
    for no in Arr:
        sum = sum + no

    return sum




def main():
    Data = [2,3,1,6,4,5]
    print("Orignal data",Data)
    Data_Filter = list(filterX(Data,CheakEven))
    Data_map = list(mapX(Data_Filter,Increment))
    Data_Reduce = reduceX(Data_map)

    print("Data after filter :",Data_Filter)
    print("Data after increment",Data_map)
    print("Data after increment",Data_Reduce)


if __name__ =="__main__":
    main()