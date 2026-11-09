# def place_order():
#     print(' [LOG] Order Processing Started...')
#     print('Order Placed Successfully...')
#     print(' [LOG] Order Processing Finished...')
    
# place_order()

# Decorator takes func as input argument
# It has a Nested Function
# It returns a Nested Function

def logger(func):
    
    # Nested Function has to be returned
    def wrapper():
        print(' [LOG] Order Processing Started...')
        func()
        print(' [LOG] Order Processing Finished...')
    return wrapper

@logger
def place_order():
    print('Order Placed Successfully...')
    
place_order()