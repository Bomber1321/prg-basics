###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
inta = int(a)
b = input('b=')
intb = int(b)
c = input('c=')
intc = int(c)
volume = inta*intb*intc   
surface_area = 2*(inta*intb+intb*intc+intc*inta)
print(f'surface area is:{surface_area}')
print(f'volume is {volume}')