def compute_taxes(amount):
    # final_amount = amount + 0.18 * amount + 0.05*amount+1
    # return final_amount
    return amount + 0.18 * amount + 0.05*amount+1

taxes = lambda amount: amount + 0.18 * amount + 0.05*amount+1

amount = 100
# print(compute_taxes(amount))

print(compute_taxes, type(compute_taxes))
print(taxes, type(taxes))

print(taxes(amount))

add = lambda a,b: a + b
print(add(10,20))

square = lambda num: num*num

print(square(10))