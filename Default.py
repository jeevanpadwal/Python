
def Area(Radius,PI = 3.14):
    Result = PI *Radius*Radius
    return Result

def main():
    Rvalue = 10.5
    PIvalue = 3.14
    ans = Area(Rvalue,PI =7.10) # default and key word argument 
    print("Area of circle is :",ans)

if __name__ == "__main__":
    main()