def DisplayF(No):
  

    if(No <= 0):
        return 1
    
    else:
        return (No * DisplayF(No - 1))

ret = DisplayF(4)
print("Factorials :",ret)
