# Assigment Operators: =, +=, -=, *=, /=, **=, %=
# ++, -- -> this is not available in python
number1 = 10
'''number1 += 20 # number1 = number1 + 20
number1 += 1
number1 -= 1

number1 *= 2
print("number1:", number1)
'''

# hashcode of number1 is assigned to number2 . 
# if number1 change a new container will be formed as it store single value.
# Number2 remain same . Concept: reference operator 
number2 = number1

number1 *= 2
print(number1,id(number1))
print(number2,id(number2))