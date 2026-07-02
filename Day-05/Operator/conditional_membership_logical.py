# Conditional Operators -> will always return either true or false
# >, <, >=, <=, ==, !=

# Membership Operators 
# is, in, not in, is not

# Logical Operators
# and or not

wallet_amount = 300
cab_fare = 300

print('can i book the cab?', (wallet_amount >= cab_fare))

# Boolean : True/False
# internt = True
# 'is' checks the identity/hashcode
print(cab_fare is  wallet_amount)
# print(cab_fare is not wallet_amount)

print(cab_fare == wallet_amount) # "==" checks the object| data
'''
print(cab_fare != wallet_amount)



data = [10, 20, 30]
print(10 in data)
print(100 not in data)

internet = True
gps = False

print('can i navigate?', internet and gps)

email = 'admin@example.com'
password = 'admin123'

user_email = input('Enter Email to Login: ')
user_password = input('Enter Password to Login: ')

print('Login Success?', user_email == email and user_password == password)
'''