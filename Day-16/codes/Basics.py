# orders = ['Pizza','Burger','Pasta','Noodles','Coke']
# orders = {'Pizza','Burger','Pasta','Noodles','Coke'}
# orders = ('Pizza','Burger','Pasta','Noodles','Coke')
# orders = "'Pizza','Burger','Pasta','Noodles','Coke'"
orders = {
    'o1':'Pizza',
    'o2':'Burger',
    'o3':'Pasta',
    'o4':'Noodles',
    'o5':'Coke'
}
# for order in orders:
#     print(order)

orders_iterator = iter(orders)
print(orders_iterator,type(orders_iterator))

print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))