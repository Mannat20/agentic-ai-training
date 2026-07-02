''' Different way to store data.
john_math=70
john_sci=75 
john_eng=80
john_marks=[70,75,80]
a_marks=[60,45,90]
# list of list
class_record =[
    [70,75,80],
    [60,45,90]
]
'''
#              0.  1.  2.  3.   4.   5. 
john_marks = [70, 80, 85, 'B', 'A', 'A']
print(john_marks, id(john_marks), type(john_marks))

print(len(john_marks))

# Output
print(john_marks[0], id(john_marks[0]), type(john_marks[0]))
print(john_marks[1], id(john_marks[1]), type(john_marks[1]))
print(john_marks[2], id(john_marks[2]), type(john_marks[2]))
print(john_marks[3], id(john_marks[3]), type(john_marks[3]))
print(john_marks[4], id(john_marks[4]), type(john_marks[4]))
print(john_marks[5], id(john_marks[5]), type(john_marks[5]))

john_marks[1] = 'B'
print(john_marks[1], id(john_marks[1]), type(john_marks[1]))

# a_marks = 70, 80, 85
a_marks = (70, 80, 85)
print(a_marks, id(a_marks), type(a_marks))
a_marks[0]=90;


class_record =[
    [70,75,80],
    [60,45,90]
]
print(class_record, id(class_record), type(class_record))

print(class_record[0], id(class_record[0]), type(class_record[0]))
print(class_record[1], id(class_record[1]), type(class_record[1]))
print(class_record[0][0], id(class_record[0][0]), type(class_record[0][0]))
print(class_record[0][1], id(class_record[0][1]), type(class_record[0][1]))
print(class_record[0][2], id(class_record[0][2]), type(class_record[0][2]))
print(class_record[1][0], id(class_record[1][0]), type(class_record[1][0]))
print(class_record[1][1], id(class_record[1][1]), type(class_record[1][1]))
print(class_record[1][2], id(class_record[1][2]), type(class_record[1][2]))
class_record[0][0] = 90
print("after changing the value of class_record[0][0] to 90")
print(class_record[0][0], id(class_record[0][0]), type(class_record[0][0]))