def f(word:str):
    temp=""
    for i in range(0,len(word)):
        temp=word.replace(word[i],word[i].upper())
        result.append(temp)
    result="-".join(map(str,result))
    return result
       

print(f("water"))
