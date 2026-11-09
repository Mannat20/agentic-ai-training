import re
text='Python is easy to learn'

result=re.search('easy',text)
if result:
    print('Found.')
else:
    print('not found')


text='Order id 101 costs 2500 inr'
result=re.findall(r'\d+',text) # r denotes raw string
print(result)

text = """
this is awesome
john@example.com we are learning regular expressions in python
admin@finlo.in
hello@gmail.com
"""
result=re.findall(r'\S+@\S+',text)
print(result)

phone = '9876512345' # exactly a 10 digit phone number
phone_check=re.fullmatch(r'\d{10}',phone)
if phone_check:
    print('Valid phone number')
else:
    print('Invalid Phone Number.')

pan = 'BBVPK2144K'
pan_validation=re.fullmatch(r'[A-Z]{5}[0-9]{4}[A-Z]{1}',pan)
if pan_validation:
    print('Valid pan number')
else:
    print('Invalid pan Number.')


vehicle_number = 'PB10AL2937'
validation=re.fullmatch(r'[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}',vehicle_number)
if validation:
    print('Valid vehicle_number ')
else:
    print('Invalid vehicle_number .')


text = 'Learning #python and #agenticai with #auribises'
hastags=re.findall(r'#\w+',text)
print(hastags)

text = 'Visit the site https://finlo.in to read about parking ticketing'
urls = re.findall(r'https?://\S+', text)
print('urls:', urls)

text = """
i want to place a call to +919876512345 and send an email to john@example.com
as my vehicle PB10AL2937 is having a flat tyre. I need help immediately
"""
# With Regular Expression, filter 3 things -> Phone, email and Vehicle Number

result=re.findall(r'[0-9]{12}| \S+@\S+| [A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4} ',text)
print(result)
#  | [A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}