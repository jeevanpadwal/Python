data = (11,21,51,101)

print("Output using for -----------")

for i in data:
    print(i,end =" ")
print()


print("Output using for with index")

for i in range(0,len(data)):
    print(data[i],end =" ")
print()



print("Output using for while with index")

i=0
while(i < len(data)):

    print(data[i],end =" ")
    i+=1
print()