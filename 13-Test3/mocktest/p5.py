import re
def f(numbers):
    count=0
    for number in numbers:
        if re.match("^[+-]?[1-7a-dA-D]+$",number):
            count=count+1
    return count




print(f(["A15","-31","7abC","+D1","-g4"]))
print(f(["A05","-3+1","7ab8C","+Bb7","-22c55"]))