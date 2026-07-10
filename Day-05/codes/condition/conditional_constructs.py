# Conditional Constructs
# if else
# if elif else
# nested if else



email = 'admin@example.com'
password = 'admin123'

user_email = input('Enter Email to Login: ')
user_password = input('Enter Password to Login: ')

# regular/simple if/else

if user_email == email and user_password == password:
    print('Login is Successful')
else:
    print('Invalid Credentials. Either email or password is incorrect')


# nested if/else
"""
if user_email == email:
    if user_password == password:
        print('Login Success')
    else:
        print('Login Failed: Invalid Password')
else:
    print('Login Failed: Invalid Email')
"""