# list: Indexing
# It can store duplicates value.
#       0  1  2  3  4
list1=[10,20,30,40,50,10,20]
print("list1: ",list1," hashcode of list1: ",id(list1),type(list1))
print(list1[0],list1[len(list1)-2])

#Set : Hashing (due to which we get unordered data)
# It store Unique Values.
set1={10,20,30,40,50,10,20}
print("set1: ",set1," hashcode of set1: ",id(set1),type(set1))
