data = 11                       # 0 0 0 0 1 0 1 1
result = data >> 3              # 0 0 0 0 0 0 0 1 ----- 0 1 1
print('result:', result)        # 1

print('~~~~~~~~~~~~~~~~~')

data = -11
result = data >> 3
print('result:', result) 
"""

 11:  0 0 0 0 1 0 1 1
-11:  1 1 1 1 0 1 0 0  1s complement
                  + 1  2s complement

-11 >> 3

     1 1 1 1 0 1 0 0 >> 3
     _ _ _ 1 1 1 1 0 --- 1 0 0
     1 1 1 1 1 1 1 0 --- 1 0 0
     0 0 0 0 0 0 0 1
                   1
     0 0 0 0 0 0 1 0 -> -2
"""      

data = -13
result = data >> 2
print('result:', result) 
