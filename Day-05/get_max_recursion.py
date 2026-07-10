def get_max(numbers,length):
    if length==1:
        return numbers[0]
    previous=get_max(numbers,length-1)
    current=numbers[length-1]
    if current>previous:
        return current
    else:
        return previous


data=[10,40,20,30,50]
result=get_max(data,len(data))
print('Max value out of ',data,' is ',result)