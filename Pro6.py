def Display(No):
  

    if(No <= 0):
        return 0
    
    else:
        return (No * Display(No - 1))

ret = Display(4)
print("Result :",ret)
