import math

x=40+3.14
print(x)

print(repr('spam'))
print(str('spam'))

a=1
b=2
c=3

print(a>b and b>c)
print(a>b>c)#this is quicker bc only evaluate b once

print(math.floor(2.5))
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))

print(eval('64'))
print(eval('0b1000000'))

print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))
print('%o, %x, %x, %X' % (64, 64, 255, 255))

print(math.pi, math.e)
print(math.sin(90),math.sqrt(4),pow(2,4),abs(-4.0))

from fractions import Fraction
x=Fraction(1,3)
print(x)
print(Fraction(.25))

z=set('abcde')
y=set('bdxyz')
print(z,y)

print(z-y)#union, difference, intersection, XOR, superset, subset all can be done

