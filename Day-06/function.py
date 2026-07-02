data=[10,20,30,40,50]
score=[98,89,76,90,100]
price=[677,222,55,788,111,999]

'''
max=data[0]
for i in range(1,len(data)):
    if data[i]>max:
        max=data[i]
print('Maximum value in ',data,'is:',max)
max=score[0]
for i in range(1,len(score)):
    if score[i]>max:
        max=score[i]
print('Maximum value in ',score,'is:',max)
max=price[0]
for i in range(1,len(price)):
    if price[i]>max:
        max=price[i]
print('Maximum value in ',price,'is:',max)

'''


def max_value(number):
    max=number[0]
    for i in range(1, len(number)):
        if number[i] > max:
            max = number[i]
    return max

print('Maximum value in ',data,'is:',max_value(data)) # (number=data)
print('Maximum value in ',score,'is:',max_value(score))
print('Maximum value in ',price,'is:',max_value(price)) 
