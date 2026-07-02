#LIST
data=[10,20,30,40,50]

# for each | enhanced loop : Use for read only purpose , it does not return the index
#for number in data:
#   print(number)

# Different ways for fetching index.
# In this data can also be updated as we are using index.
'''for index in range(0,5): # this return the index
    print(data[index])
for index in range(len(data))
for index in range(0,len(data),1)
'''

'''for index in range(len(data)):
    data[index]=data[index] * 2
    print(data[index])


# while loop -> traditional loop : When we want apps to continuously run till some action is taken.
idx = 0
while idx < 5:
    print(data[idx])
    idx += 1
# Indexing aonly works on list.
'''
# Dictionary
product = {
    'code': 101,
    'name': 'Ultraboost',
    'brand': 'Adidas',
    'price': 8000,
    'category': 'shoe'
}

for key in product:
    print(key,product[key])