import math as m
def circle(r):
    return m.pi * pow(r, 2)
r = float(input('r='))
area = circle(r)
print(f'Area={area}')
