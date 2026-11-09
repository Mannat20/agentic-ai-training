
discount_generator = lambda discount : (lambda price: price - (price*discount/100))

monthly_subscription = discount_generator(10)
half_yearly_subscription = discount_generator(20)
yearly_subscription = discount_generator(30)
 
print(monthly_subscription(1000))
print(half_yearly_subscription(1000))
print(yearly_subscription(1000))