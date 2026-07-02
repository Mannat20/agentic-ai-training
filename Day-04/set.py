number={10,20,30,40,50}
print("Number: ",number,id(number),type(number))
num=[10,20,30,40,50,10,20]

data=set(num) # A new hashcode will be generated whenever we are using set().
print("Data: ",data,id(data),type(data))

# This will throw an error because set elements can't be accessed by index.
print("data[0]: ",data[0],id(data[0]),type(data[0])) 


