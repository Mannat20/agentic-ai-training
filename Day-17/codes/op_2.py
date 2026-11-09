numbers = list(range(10,101,10))

numbers.append(99)
numbers.append(77)
numbers.append(101)

numbers.insert(3,33)

print('numbers:',numbers)

print('sum of numbers:',sum(numbers))
print('min of numbers:',min(numbers))
print('max of numbers:',max(numbers))
print('avg of numbers:',sum(numbers)/len(numbers))
print('len of numbers:',len(numbers))

# data = tuple(numbers)
# data = set(numbers)
# data = str(numbers)
# data = dict(numbers) : error
# print('data:',data,type(data))

reverse_numbers = list(reversed(numbers))
print('reverse numbers:',reverse_numbers)
print('reverse numbers:',numbers[::-1])

numbers.sort()
print("Sorted Numbers:",numbers)

numbers.sort(reverse=True)
print("Reverse Sorted Numbers:",numbers)

index = numbers.index(101)
print('Index of 101:',index)

numbers.remove(99)
del numbers[6]
numbers.clear()
# del numbers

data = [10,20,30,40,50]
print('before data:',data)
data.pop()
print('after data:',data)

# Assignment: Explore queue implementation on list