# Explore Set
numbers = list(range(10,101,10))
print('numbers:',numbers)

data = set(numbers)
print('data:',data)
data.add(77)
data.add(99)
data.add(121)

data.remove(50)
data.clear()
print('data:',data)

john_followers = {'fionna','sia','harry','kim','leo'}
fionna_followers = {'jack','sia','kim','joe'}
george_followers = {'harry','kim'}

mutual_followers = john_followers.intersection(fionna_followers)
print('mutual_followers:',mutual_followers)

print(george_followers.issubset(john_followers))
print(john_followers.issuperset(george_followers))

A = {1,2,3,4,5}
B = {4,5,6,7,8}

C = A.union(B)
print(C)

D = A-B
print(D)

E = A^B
print(E)

F = A|B
print(F)