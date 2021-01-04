#lists and dictionairies
###Lists
##basic operations
print(3 in [1,2,3])
a=list(c*4 for c in 'SPAM')
print(a)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])

matrix[0]='dog'
print(matrix)

matrix[1:]='cat','fish'
print(matrix)

matrix.append('bunny')
matrix.sort(reverse=True)
print(matrix)

matrix.extend(['seal','tiger'])
print(matrix)

print(matrix.pop())#LIFO
print(matrix)

###Dictionaries
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(D)
print(len(D))
print(list(D.keys()))

D['ham'] = ['grill', 'bake', 'fry']
del D['eggs']
D['brunch'] = 'Bacon'
print(D)

D2 = {'toast':4, 'muffin':5}
D.update(D2)
print(D)

print(D.pop('muffin'))

Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
X = 2
Y = 3
Z = 4
print(Matrix[(X,Y,Z)])
print(Matrix)

