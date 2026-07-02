def square_of_numbers(numbers):
    print('~~~~~~~~~~~~~~~~~~~')
    print('[start] square_of_numbers function')  # Loggings (tells about the status of the function)
    print('numbers:', numbers,' hashcode of numbers is:',id(numbers))
    for index in range(len(numbers)):
        numbers[index] *= numbers[index]    
    print('Squared numbers:', numbers,' hashcode of numbers is:',id(numbers))
    print('[end] square_of_numbers function')
    print('~~~~~~~~~~~~~~~~~~~')

def main():
    print('----------------------------')
    print('[start] main function')
    data=[10,20,30,40,50]
    print('Data is:', data,' hashcode of data is:',id(data))
    square_of_numbers(data)
    print('Data is:', data,' hashcode of data is:',id(data))  # value will be updated as both are pointing to same hashcode of list.
    print('[end] main function')
    print('---------------------------')
    

if __name__=='__main__':
    main()