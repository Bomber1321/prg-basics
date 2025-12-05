# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]
sum=0
x=0
for prod_nr in product_prices:
    sum=sum+(prod_nr*product_quantities[x])
    x=x+1

print(f"Value of all the good in the shop:{round(sum,2)}")