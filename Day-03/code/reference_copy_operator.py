a=10
b=a
print("a: ",a," hashcode of a: ",id(a),type(a))
print("b: ",b," hashcode of b: ",id(b),type(b))

data=[10,20,30,40,50]
number=data
print("data: ",data," hashcode of data: ",id(data),type(data))
print("number: ",number," hashcode of number: ",id(number),type(number))

number[2]=300
print("After updating value of number[2]: ")
print("data[2]: ",data[2]," hashcode of data: ",id(data[2]),type(data[2]))
print("number[2]: ",number[2]," hashcode of number: ",id(number[2]),type(number[2]))