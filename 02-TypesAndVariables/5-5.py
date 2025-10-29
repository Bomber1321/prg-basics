price= float(input('Price: '))
discount = float(input('Discout %: '))
dcprice= price*(1-(discount/100))
reduction= price-dcprice
print(f'Price: {round(price,2)}')
print(f'Discount: {round(discount,2)}')
print(f'DC price: {round(dcprice,2)}')
print(f'Reduction: {round(reduction,2)}')
