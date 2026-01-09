def f(products,lamb):
    lista=map(lamb,products)
    return lista

prods = ["water","cheese","tomato"]
fnc1 = lambda x: "id:"+x[:2] 

print(f(prods,fnc1))
