print("Demostration of Tuple ")

data = {11,21,51,101,11}

# Data : Hetrogeneous
# Ordered : No
# Mutable: Yes
# Indexed : No
#Dulicates : Yes

data1 ={11,90.2,"Hello",True} # hetrogeneous 

print("data is hetrogeneous :",data1)
print("data is ordered :",data1)
print("Length of data",len(data))

print("data with unique elements:",data)

print("set is mutable")
# insert element in set

data.add(211)
print("Data after insertion ",data)

# remove element

data.remove(211)
print("Data after removel ",data)

data.discard(201)
print("Data after discard",data)
