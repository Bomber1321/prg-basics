arr = ["Barbara", "Ann","Patrick","Thomas"]
x = sorted(arr, key=len)
print(x)


arr2= [2,3,5,7]

print(list(map(lambda x:x*10, arr2)))

print(list(filter(lambda x:x>4, arr2)))