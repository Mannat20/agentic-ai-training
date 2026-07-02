# Creation Statement | Model
user_name="Mannat20" # reference variable store the hashcode of the value stored in the variable.
# this will give the hashcode(related to heap) of the variable and type ( classification) of the variable.  
print('Hashcode of user_name: ',id(user_name),type(user_name)) # Output Statement | VIEW
age=20
print('Hashcode of age: ',id(age),type(age)) 
john_age=20 # Data in Right hand Side : Literal 
print('Hashcode of john_age: ',id(john_age),type(john_age))
# Age and john_age will have same hashcode because both are pointing to the same value in the heap.
user_name="Mannat_Kaur" 
print('Hashcode of user_name: ',id(user_name),type(user_name))
# a new hascode is assigned to the variable user_name because it is now pointing to a new value in the heap.
# the old value is now unreferenced and will be garbage collected.

del john_age;
del age;
#print('Hashcode of age: ',id(age),type(age))


# creation statement + Input(view)
age2=input ("Enter your age:")
# output(view)
print('Hashcode of age2: ',id(age2),type(age2))