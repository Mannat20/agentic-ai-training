my_data = {
    101: 'John',
    201: 'Jennie',
    301: 'Jim',
    401: 'Jack',
    251: 'Joe',
    95: 'Fionna',
}
# my_data = {
#     'rn101': 'Sia',
#     'ec101': 'Fionna',
# }

print('len(my_data):',len(my_data))
print('min(my_data):',min(my_data))
print('max(my_data):',max(my_data))
print('sum(my_data):',sum(my_data))

print(my_data[101])
print(my_data.get(101))

my_data[666] = 'Leo'
my_data[123] = 'Ben'

del my_data[301]
my_data.pop(401)

print(my_data)

keys = my_data.keys()
print(keys)

for key in keys:
    print(key,my_data[key])
    
items = my_data.items()

print(items)

for item in items:
    print(item)
    print(item[0],item[1])  