
import threading

def Display1_50(No):
    
    for i in range(1,No+1):
        print(i)
        
            
def Display50_1(No):
 
    for i in range(No,0,-1):
        print(i)

def main():

    Number = 50

    thread1 = threading.Thread(target= Display1_50 ,args = (Number ,))
    thread2 = threading.Thread(target= Display50_1  ,args = (Number ,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()




if __name__ == "__main__":
    main()