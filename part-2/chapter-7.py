#String Fundamentals

a='one'
b="one"
print(a,b)

s='a\nb\tc'
print(s)
print(len(s))

#indexing and slicing
#string conversion
s='spammy'
s=s[:3]+'xx'+s[5:]
print(s)

print(s.replace('xx','mm'))

print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})

import sys
g='My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})
print(g)