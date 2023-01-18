# normal functions / named functions

def Add(no1,no2):
    return no1 + no2

# lambda functions / unnamed functions 
# lambda parameters : body 

addfun = lambda a,b : a+b

ans1 = Add(10,11)
ans2 = addfun(10,11)

print("Addition is using normal function",ans1)
print("Addition is using lambda function",ans2)

print("type of lambda function ",type(addfun))