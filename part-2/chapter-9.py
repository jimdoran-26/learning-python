#tuples, files, else
###Tuples
print((1, 2) + (3, 4),(1,2)*4)

y = (40,)#comma after signifies this is a tuple
T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)
tmp.sort()
T = tuple(tmp)
print(tmp,T,sorted(tmp))

#named tuples
bob = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print(bob)
print(bob['name'])

from collections import namedtuple
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])
print(bob)

###Files
myfile = open('myfile.txt', 'w') # Open for text output: create/empty
myfile.write('hello text file\n')
myfile.write('goodbye text file\n')
myfile.close()
myfile = open('myfile.txt')
myfile.readline()

for line in open('myfile.txt'):
    print(line,end='')

