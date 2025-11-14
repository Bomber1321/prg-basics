###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s=(a+b+c)/2
    wynik=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f'The area of ​​a triangle with sides {a}, {b}, {c} is {wynik}')
    return wynik


triangle_area(3,4,5)
triangle_area(5,12,13)
triangle_area(7,24,25)
