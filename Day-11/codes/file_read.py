#  
# data=file.read()
# print(data)
# print(type(data),len(data))

# lines=file.readlines()
# for line in lines:
#     print(line)
# file.close()
# print(type(lines),len(lines))

with open('tollPlaza.py') as file:
    lines=file.readlines()
    for line in lines:
        print(line)
    file.close()  
    print('program finished')   