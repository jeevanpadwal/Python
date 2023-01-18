def ChkPrime(Brr):

    
    isum = 0
    prime = []
    for i in Brr:
        iCnt = 0

        for j in range(1,i):
            if (i % j) == 0:
                iCnt = iCnt +1
            
        if (iCnt == 1):
            
            isum = isum + i
            
            
    return isum 
               
        


