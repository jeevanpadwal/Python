def Display(No):
    Ans = 0

    while(No > 0):
        Ans = Ans + No

        No = No -1

    return Ans

ret = Display(4)
print("Result :",ret)
