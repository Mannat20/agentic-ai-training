# my_data = [10,20,30,40,50]
# print(my_data[0])
# print(my_data[-1])
# print(my_data[-5])
# # CRASH -> wherever error occurs , the next part of program will not be executed
# # Handling Run Time Errors
# try:
#     print(my_data[7]) # Error at Run Time
# except:
#     print('Something Went Wrong')
# print('Last Statement')

# # 2D List
# numbers = [
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ]

# print('len(numbers):',len(numbers))
# print('len(numbers[0]):',len(numbers[0]))

# print(numbers[0][2])
# print(numbers[-1][-2])

# # 3D List
# large_data = [
#     [
#         [10,20,30],
#         [40,50,60],
#         [70,80,90]
#     ],
#     [
#         [11,22,33],
#         [44,55,66],
#         [77,88,99]
#     ],
# ]

# print('len(large_data):',len(large_data))
# print('len(large_data[0]):',len(large_data[0]))
# print(large_data[0][2])
# print(large_data[-1])
# print(large_data[-1][-2])
# print(large_data[-2][-2][-2])

data = list(range(10,101,10))
print(data)

print('data[2 : 5]:',data[2:5])
print('data[:5]:',data[:5])
print('data[5:]:',data[5:])
print('data[:-5]:',data[:-5])
print('data[-5:-2]:',data[-5:-2]) 

data1 = [10,20,30]
data2 = [40,50,60]

data3 = data1+data2
print('data3:',data3)

data4 = [10,20,30]
data5 = data4 * 3
print('data5:',data5)

print(10 in data4)
print(100 in data4)
print(100 not in data4)

data6 = {10,20,30}
print(10 in data6)

product = {
    'code':101,
    'name':'Adidas Ultraboost',
    'price':8000 
}
print('price' in product) # works on key
print(8000 in product) # will not work for value