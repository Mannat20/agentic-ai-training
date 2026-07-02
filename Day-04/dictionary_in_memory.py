product = {
    'code': 101,
    'name': 'Ultraboost',
    'brand': 'Adidas',
    'price': 8000,
    'category': 'shoe'
}
print(product,id(product),type(product))
print(product['code'],id(product['code']),type(product['code']))
print(product['name'],id(product['name']),type(product['name']))
print(product['brand'],id(product['brand']),type(product['brand']))
shoe_brand='adidas' # this will be stored in different space in memory as python is case sensitive.
# a new hashcode will be generated.
print(shoe_brand,id(shoe_brand),type(shoe_brand))
print(product['price'],id(product['price']),type(product['price']))

product['price'] = 7000
print("after updating price:")
# this show that a new container is made . and the old value is not updated in place in memory.
print(product['price'],id(product['price']),type(product['price']))

for key in product:
    print(key, product[key])