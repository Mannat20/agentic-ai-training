#single value container
a=10
b=10
print("a: ",a," hashcode of a: ",id(a),type(a))
print("b: ",b," hashcode of b: ",id(b),type(b))

#Multi value container
data=[10,20,30,40,50]
number=[10,20,30,40,50]
print("data: ",data," hashcode of data: ",id(data),type(data))
print("number: ",number," hashcode of number: ",id(number),type(number))
#this will print the hashcode of "a" because it store 10 as a value 
print("data[0]: ",data[0]," hashcode of data[0]: ",id(data[0]),type(data[0]))
print("number[0]: ",number[0]," hashcode of number[0]: ",id(number[0]),type(number[0]))
#print("data[1]: ",data[1]," hashcode of data[1]: ",id(data[1]),type(data[1]))
#print("number[1]: ",number[1]," hashcode of number[1]: ",id(number[1]),type(number[1]))
data[0]=100
print("After updating value of data[0]: ")
print("data[0]: ",data[0]," hashcode of data[0]: ",id(data[0]),type(data[0]))
#number[0] will still have the same value as before because it is not updated
print("number[0]: ",number[0]," hashcode of number[0]: ",id(number[0]),type(number[0]))
