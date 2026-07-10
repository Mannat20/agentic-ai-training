"""
    BINGO: Flat 100 off, min amount 200
    GET500: Flat 500 off, min amount 100
    JUMBO: Flat 300 off, min amount 500

"""

amount_in_cart = int(input('Enter Amount: '))
promo_code = input('Enter Promo Code: ')

if promo_code == 'BINGO':
    if amount_in_cart >= 200:
        amount_to_pay = amount_in_cart - 100
        print('Promo Code Applied Successfully')
        print('Amount to Pay:', amount_to_pay)
    else:
        print('Add more items worth', 200 - amount_in_cart + 1, 'to avail promo code')
elif promo_code == 'GET500':
    if amount_in_cart >= 100:
        amount_to_pay = amount_in_cart - 500
        print('Promo Code Applied Successfully')
        print('Amount to Pay:', amount_to_pay)
    else:
        print('Add more items worth', 100 - amount_in_cart + 1, 'to avail promo code')
elif promo_code == 'JUMBO':
    if amount_in_cart >= 500:
        amount_to_pay = amount_in_cart - 300
        print('Promo Code Applied Successfully')
        print('Amount to Pay:', amount_to_pay)
    else:
        print('Add more items worth', 500 - amount_in_cart + 1, 'to avail promo code')
else:
    print('Invalid Promo Code')