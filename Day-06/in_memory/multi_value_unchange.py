def square_of_numbers(numbers):
    num=[]
    for index in range(len(numbers)):
        num.append(numbers[index])
    print('~~~~~~~~~~~~~~~~~~~')
    print('[start] square_of_numbers function')  # Loggings (tells about the status of the function)
    print('num:', num,' hashcode of num is:',id(num))
    for index in range(len(num)):
        num[index] *= num[index]    
    print('Squared num:', num,' hashcode of num is:',id(num))
    print('[end] square_of_numbers function')
    print('~~~~~~~~~~~~~~~~~~~')

def main():
    print('----------------------------')
    print('[start] main function')
    data=[10,20,30,40,50]
    print('Data is:', data,' hashcode of data is:',id(data))
    square_of_numbers(data)
    print('Data is:', data,' hashcode of data is:',id(data))  # value will not be updated.
    print('[end] main function')
    print('---------------------------')
    

if __name__=='__main__':
    main()