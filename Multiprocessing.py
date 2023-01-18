import time

def DisplayEven(No):

    for i in range(No):
        if(i % 2 == 0):
            print("Even number :",i)

def DisplayOdd(No):
     for i in range(No):
        if(i % 2 != 0):
            print("Odd number :",i)

def main():

    print("Demostration of serial programming")
    DisplayEven(2000)
    DisplayOdd(2000)


if __name__=="__main__":
    start_time = time.process_time()
    main()

    end_time = time.process_time()

    print("Execution time is :",end_time - start_time)