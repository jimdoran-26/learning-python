#integer addition
print(123+222)
#floating point
print(1.5*4)
#exponent
print(2**100)

import math
print(math.pi)
print(math.sqrt(85))

s='spam'
x=len(s)
print(x)
print(s[0])
print(s[-1])

print(s.find('pa'))
print(s.find('ap'))

print(s.replace('pa','xyz'))
print(s)


line = 'aaa,bbb,ccccccc,dd'
print(line.split(','))

print(s.isalpha())

print(line.rstrip().split(','))

L=[[1,2,3],[4,5,6],[7,8,9]]
[row[1] for row in L if row[1] % 2 == 0]
