values = [10,20,30,40]
print(values)
print(type(values))
print(len(values))
print(values[0])
print(values[1])
print(values[2])
print(values[3])          

values.append(50)
values.append(50)

values.insert(2, 11)
print("Data after insert :",values)

values.insert(41, 41)
print("Data after insert :",values)


values.remove(20)
print(values)

print(type(values[0]))

values.append(90.30)
print(values)


