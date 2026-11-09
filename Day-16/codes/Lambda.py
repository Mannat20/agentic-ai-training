from functools import reduce
product_prices = [100,300,450,120,900]
discounted_prices = []

discount = lambda price,percentage: price*percentage

for price in product_prices:
    discounted_prices.append(discount(price,0.5))
    
print('Product prices:',product_prices)
print('Discounted prices:',discounted_prices)

new_prices = list(map(lambda price: price*0.5, product_prices))
print('New prices:',new_prices)

filtered_prices = list(filter(lambda price: price>200, product_prices))
print('Filtered prices:',filtered_prices)

total = reduce(lambda x,y: x+y, product_prices)
print('Total:',total)

# Assignment: list of flights dictionary
# lambdas -> map,filter and reduce