print("Demonstration of dictonary ")



Batches = {"PPA":18000,"LB":16700,"Python":16500,"Angular":15000}



print("Data of dictionary :",Batches)

print("Data traversal using for loop")

for x in Batches:
    print(x)

print("data travell --------")
for x in Batches:
    print(x,Batches[x])

print("data travell --------")
for x in Batches:
    print(x,Batches.get(x))


keyBatches =Batches.keys()
print(type(keyBatches))
print(keyBatches)

valueBatches = Batches.values()
print(valueBatches)

for i in range(0, len(Batches)):
    print("Batches name is :",keyBatches,end =" ")
    print("Fees are",valueBatches)