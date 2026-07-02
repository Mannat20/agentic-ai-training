def add_numbers(number1=10, number2=20):
    result = number1 + number2
    print('result is:', result)

print('add_numbers before:', add_numbers)

# ReDefine the Function
# Wheneveer we redefine the function,
# old defintion will be deleted and new will be created

add = add_numbers # reference copy of hashcode of add_numbers function

def add_numbers(number1=10, number2=20, number3=30):   # new hashcode
    result = number1+number2+number3
    print('result is:', result)


print('add_numbers after:', add_numbers)
print('add: ',add)
add_numbers()
add()