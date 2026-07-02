'''def add_number(number1,number2):
def add_number(number1=10,number2=20):
def add_number(number1,number2=20):
def add_number(number1=10,number2):   # this will throw an error.
'''

def add_number(number1=10,number2=20):
    result=number1+number2
    print('Addition of',number1,'and',number2,'is:',result)

add_number()  # Uses default values
print(add_number) # return the hashcode in hexadecimal format.
print(hex(id(add_number)),type(add_number))


add_number(number1=100,number2=200)  # Uses the values provided by the user.
add_number(number2=200,number1=100)  
add_number(100)

#reference copy operation
add=add_number
print(add) # return the hashcode in hexadecimal format.
add(100,200)  


"""
You can delete the function also
del add
del add_numbers

add_numbers(10) # no function named add_numbers
"""

