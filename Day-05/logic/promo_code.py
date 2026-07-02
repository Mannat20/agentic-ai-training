promo_codes={
    'BINGO': {
        'minimum_amount': 200,
        'discount': 0.50,
        'discount_upto':200
    },
    'JUMBO': {
        'minimum_amount': 500,
        'discount': 0.30,
        'discount_upto': 0
    },
}

promo_code=input('Enter Promo Code: ')
amount_in_cart=int(input('Enter Amount in Cart: '))
print('~~~~~~~~~~~~~~~~~~~~')
print('Promo Code:', promo_code)
print('Amount in Cart:', amount_in_cart)
print('~~~~~~~~~~~~~~~~~~~~')

if promo_code in promo_codes:
    promo_code_rules=promo_codes[promo_code]
    print('Promo Code Rules:', promo_code_rules,type(promo_code_rules))
    print('_______________________')
    if amount_in_cart>promo_code_rules['minimum_amount']:
        discount_cal=promo_code_rules['discount']*amount_in_cart
        if promo_code_rules['discount_upto']!=0:
            if discount_cal>promo_code_rules['discount_upto']:
                amount_to_pay=amount_in_cart-promo_code_rules['discount_upto']
        else:
            amount_to_pay=amount_in_cart-discount_cal
        print('promo code applied successfully')
        print('Amount to Pay:', amount_to_pay)
    else:
        print('add more items worthy',promo_code_rules['minimum_amount']-amount_in_cart +1,'to avail promo code')
else:
    print('Invalid Promo Code')