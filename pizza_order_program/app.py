print('Thankyou for choosing Pizza deliveries')
size = input('Choose the size of pizaa; S or M or L: ')
add_pepperino = input('do yo want pepperino? Y OR N: ')
extra_cheese = input('Do you want extra cheese? Y OR N: ')
bill = 0
if (size == 'S'):
    bill += 15
elif (size == 'M'):
    bill += 20
else:
    bill += 25
if (add_pepperino == 'Y'):
    if (size == 'Y'):
        bill += 2
    else:
        bill += 3
if (extra_cheese == 'Y'):
    bill += 1
print(f'your final bill is {bill}')


# if (size == 'small'):
#     price += 15
#     print(f'small pizza is ${price}')
#     pepperoni = input('add perperoni for small pizza; y or n?: ')
#     if (pepperoni == 'y'):
#         peperoni_price = 2
#         total_price = peperoni_price + price
#         print(f'total price for small pizza with pepperoni is ${total_price}')
#     else:
#         print(f'total price for a plain small pizza  is ${price}')
#         cheese = input('add cheese? y or n')
# elif (size == 'medium'):
#     price += 20
#     print(f'medium pizza is ${price}')
#     pepperoni = input('add perperoni for medium pizza; y or n?: ')
#     if (pepperoni == 'y'):
#         peperoni_price = 3
#         total_price = peperoni_price + price
#         print(f'total price for medium pizza with pepperoni is ${total_price}')
#     else:
#         print(f'total price for a plain medium pizza  is ${price}')
# elif (size == 'large'):
#     price += 25
#     print(f'large pizza is ${price}')
#     pepperoni = input('add perperoni for large pizza; y or n?: ')
#     if (pepperoni == 'y'):
#         peperoni_price = 3
#         total_price = peperoni_price + price
#         print(f'total price for large pizza with pepperoni is ${total_price}')
#     else:
#         print(f'total price for a plain large pizza  is ${price}')
