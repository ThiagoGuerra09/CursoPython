"""
Trocar valores entre variaveis
"""

x=10
y=5
z=0

z = x
x = y
y = z

print(x,y)
#esse processo gasta linha atoa, pode ser feito assim:

x, y = y, x
print(x,y)
