import myModule13
import pdb

pdb.set_trace()
print('Program started')

var = 10

def func(a, b):
    print('Inside function')
    return a + b

var2 = 20
for i in range(2):
    print('Inside loop')
    print(i)

c = func(var, var2)
d = myModule13.add(var, var2)

print(c, d)
print('program completed')
