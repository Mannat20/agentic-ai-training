def deliver_orders():
    yield {'o1': 'Pizza'}
    yield ('Burger','Munchurian')
    yield ['Noodles']
    yield {'Coke'}
    
orders = deliver_orders()
print(orders,type(orders))

print(next(orders)['o1'])
print(next(orders)[1])
print(next(orders)[0])
print(next(orders).pop())