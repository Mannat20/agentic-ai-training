def square_of_number(number):
    print('~~~~~~~~~~~~~~~~~~~')
    print('[start] square_of_number function')  # Loggings (tells about the status of the function)
    print('Number is:', number,' hashcode of number is:',id(number))
    number *=number
    print('Square of number is:', number,' hashcode of number is:',id(number)) # its hashcode will change.
    print('[end] square_of_number function')
    print('~~~~~~~~~~~~~~~~~~~')
    return number


def main():
    print('[start] main function')
    print('---------------------------')
    data=10
    print('Data is:', data,' hashcode of data is:',id(data))
    square_of_number(data)
    print('Data is:', data,' hashcode of data is:',id(data)) # its hashcode will not change.
    print('[end] main function')
    print('---------------------------')
    
if __name__=='__main__':
    main()
    