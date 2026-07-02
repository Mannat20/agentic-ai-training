'''# for outer_index in range(0,5,1):
for outer_index in range(5):            # O(n) O(n*n)
    print(outer_index)
    print('-------------------')

    for inner_index in range(3):
        print(inner_index, end=' ')

    print('\n-------------------')
'''
for i in range(0,8):
    for j in range(8):
        if(i+j)% 2 == 0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
    