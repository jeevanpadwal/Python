
import threading
import os

def SmallChar(SData):
    thread = threading.current_thread()
    print("id of small thread :{} name of thread : {}".format(os.getpid(),thread.name))
    cnt = 0
    for i in SData:
        if i.islower():
            cnt = cnt + 1
        
    print("Number of Small Characters ",cnt)

            
def CapitalChar(SData):
    thread = threading.current_thread()
    print("id of small thread :{} name of thread : {}".format(os.getpid(),thread.name))
    

    cnt = 0
    for i in SData:
        if i.isupper():
            cnt = cnt + 1
        
    print("Number of Upeer case Characters ",cnt)
   
def DigitCount(SData):
    print("id of digit thread :",os.getpid())

    cnt = 0
    for i in SData:
        if i.isdigit():
            cnt = cnt + 1
        
    print("Number of Digts ",cnt)

def main():

    print("Entr the string")
    str = input()

    small = threading.Thread(target= SmallChar ,args = (str ,))
    capital = threading.Thread(target= CapitalChar  ,args = (str ,))
    digit = threading.Thread(target= DigitCount , args = (str ,))
    
   
    

    small.start()
    capital.start()
    digit.start()

if __name__ == "__main__":
    main()
