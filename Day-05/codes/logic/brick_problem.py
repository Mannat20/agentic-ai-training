"""
    Another Brick in the Wall

    customer - 13 bricks
    iteration 1     3
    john  1         
    jack  2
    iteration 2     6+3 = 9
    john  2
    jack  4
    iteration 3     9 + 3 + 1 => 13 
    john  3
    jack  6 -> 1


    Answer: Who placed the last brick and how many
    jack placed the last brick. qty: 1

"""

# CONTROLLER
# for/if/else/operators
brick=int(input('Enter Total Bricks: '))
i=1
total=0
while(total<brick):     # 1 +2 =3 ... 2+4=6  (9).. 3+6

    john=i
    jack=2*i
    for j in range(1,john+1):
        total+=1
        if(total==brick):
            print('John placed the last brick. Qty:',j)
            break
        
    for k in range(1,jack+1):
        total+=1
        if(total==brick):
            print('Jack placed the last brick. Qty:',k)
            break
        
    i+=1

