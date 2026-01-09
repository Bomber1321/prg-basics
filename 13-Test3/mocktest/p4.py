res = [95,90,20,50,70]
fnc1 = lambda x: x>50 
def f(fnc1,res):
    filtered=list(filter(fnc1,res))
    return (max(filtered)-min(filtered))

print(f(fnc1,res))

fnc2 = lambda x: x>30 and x<90
print(f(fnc2,res))