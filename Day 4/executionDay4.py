Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> employee1 = ['Jatin', 35, 'Pune']
>>> print(employee1)
['Jatin', 35, 'Pune']
>>> print(type(employee1))
<class 'list'>
>>> employee1[0]
'Jatin'
>>> employee1[-1]
'Pune'
>>> employee1[0] = 'Yatin' # mutuable object
>>> employee1
['Yatin', 35, 'Pune']
>>> employee1[2] = 'Mohan' #???
>>> employee1
['Yatin', 35, 'Mohan']
>>> employee1[3] = 'Pune' #??
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    employee1[3] = 'Pune' #??
IndexError: list assignment index out of range
>>> 
>>> numbers = range(10) #
>>> list(numbers)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> numbers
range(0, 10)
>>> 
>>> 
>>> numbers = list(range(10))
>>> print(numbers)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> numbers = list(range(1, 10))
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> len(numbers)
9
>>> numbers = list(range(1, 10, 2))
>>> print(numbers)
[1, 3, 5, 7, 9]
>>> 
>>> sum(range(1, 101))
5050
>>> sum(range(1, 101, 2))
2500
>>> sum(range(2, 101, 2))
2550
>>> sum(range(1, 101)) / len(range(1, 101))
50.5
>>> sum(range(1, 101, 2)) / len(range(1, 101, 2))
50.0
>>> sum(range(2, 101, 2)) / len(range(2, 101, 2))
51.0
>>> 
>>> employee1
['Yatin', 35, 'Mohan']
>>> employee2 = ['Rahul', 25, 'Pune']
>>> 
>>> employee1
['Yatin', 35, 'Mohan']
>>> employee2
['Rahul', 25, 'Pune']
>>> 
>>> # Opr
>>> 10 + 10
20
>>> 'Jatin ' + ' Miglani' # Contatenation
'Jatin  Miglani'
>>> 
>>> 
>>> # Number + addition , string + concatenation
>>> 
>>> 
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> name = 'Jatin'
>>> name.__len__()
5
>>> len(name)
5
>>> a = 10
>>> b = 20
>>> a.__add__(b)
30
>>> name.__add__(' Miglani')
'Jatin Miglani'
>>> 
>>> 
>>> employee1
['Yatin', 35, 'Mohan']
>>> employee2
['Rahul', 25, 'Pune']
>>> employee1 + employee2
['Yatin', 35, 'Mohan', 'Rahul', 25, 'Pune']
>>> employee1 * 2
['Yatin', 35, 'Mohan', 'Yatin', 35, 'Mohan']
>>> 
>>> 
>>> employee1
['Yatin', 35, 'Mohan']
>>> employee2
['Rahul', 25, 'Pune']
>>> employee1 == employee2
False
>>> employee1 > employee2 # what it compares?
True
>>> 
>>> employee2 = ['YAtin']
>>> employee1 > employee2
True
>>> employee2 = ['Yatin', 20]
>>> employee1 > employee2
True
>>> employee1
['Yatin', 35, 'Mohan']
>>> employee2 = ['Yating']
>>> employee1 > employee2
False
>>> 
>>> employee1
['Yatin', 35, 'Mohan']
>>> employee2 = ['Yatin', 35, 'Mohan']
>>> 
>>> 
>>> employee1
['Yatin', 35, 'Mohan']
>>> employee2
['Yatin', 35, 'Mohan']
>>> employee1 is employee2
False
>>> 
>>> name = 'Jatin'
>>> lastname = 'Jatin'
>>> 
>>> name is lastname
True
>>> 
>>> employee1
['Yatin', 35, 'Mohan']
>>> employee2
['Yatin', 35, 'Mohan']
>>> 
>>> employee3 = employee1
>>> employee1 is employee3
True
>>> employee1
['Yatin', 35, 'Mohan']
>>> ,employee2
['Yatin', 35, 'Mohan']
>>> employee3
['Yatin', 35, 'Mohan']
>>> 
>>> employee1[0] = 'Aakash'
>>> employee3
['Aakash', 35, 'Mohan']
>>> employee2
['Yatin', 35, 'Mohan']
>>> help(list.copy)
Help on method_descriptor:

copy(...)
    L.copy() -> list -- a shallow copy of L

>>> del employee1
>>> employee3
['Aakash', 35, 'Mohan']
>>> 
>>> 
>>> 
>>> 
>>> employee3
['Aakash', 35, 'Mohan']
>>> 'Aakash' in employee3
True
>>> 25 in range(1, 100)
True
>>> 
>>> 
>>> 'ai' in 'Jatin'  # true or false
False
>>> numbers = range(100)
>>> numbers = list(range(100))
>>> 
>>> 
>>> numbers[:3]
[0, 1, 2]
>>> numbers[-3:3]
[]
>>> numbers[-3:]
[97, 98, 99]
>>> 
>>> 
>>> employee1
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    employee1
NameError: name 'employee1' is not defined
>>> employee2
['Yatin', 35, 'Mohan']
>>> employee3
['Aakash', 35, 'Mohan']
>>> 
>>> 
>>> employees = [employee2, employee3]
>>> employees
[['Yatin', 35, 'Mohan'], ['Aakash', 35, 'Mohan']]
>>> len(employees)
2
>>> employees[0]
['Yatin', 35, 'Mohan']
>>> employees[0][0]
'Yatin'
>>> employees[1][2]
'Mohan'
>>> employees = [['Jatin', 35, 'Pune', ['Mohan', 'Aakash']], ['Rahul', 32, 'Pune', ['Vijay', 'Aakash', 'Rohan']]]
>>> 
>>> 
>>> employees
[['Jatin', 35, 'Pune', ['Mohan', 'Aakash']], ['Rahul', 32, 'Pune', ['Vijay', 'Aakash', 'Rohan']]]
>>> employees[1]
['Rahul', 32, 'Pune', ['Vijay', 'Aakash', 'Rohan']]
>>> employees[1][3]
['Vijay', 'Aakash', 'Rohan']
>>> employees[1][3][2]
'Rohan'
>>> employees[0][2][0] = 'Aditi'
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    employees[0][2][0] = 'Aditi'
TypeError: 'str' object does not support item assignment
>>> employees[0][3][0] = 'Aditi'
>>> employees
[['Jatin', 35, 'Pune', ['Aditi', 'Aakash']], ['Rahul', 32, 'Pune', ['Vijay', 'Aakash', 'Rohan']]]
>>> 
>>> 
>>> 
>>> 
>>> del employees[2][3][0]
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    del employees[2][3][0]
IndexError: list index out of range
>>> del employees[1][3][0]
>>> employees
[['Jatin', 35, 'Pune', ['Aditi', 'Aakash']], ['Rahul', 32, 'Pune', ['Aakash', 'Rohan']]]
>>> 
>>> 
>>> employee1 = ('Jatin', 35, 'Pune')
>>> employee1 + employee1
('Jatin', 35, 'Pune', 'Jatin', 35, 'Pune')
>>> employee1 * 2
('Jatin', 35, 'Pune', 'Jatin', 35, 'Pune')
>>> employee1[0] = 'Yatin'
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    employee1[0] = 'Yatin'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> employee1 = ('Jatin')
>>> type(employee)
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    type(employee)
NameError: name 'employee' is not defined
>>> type(employee1)
<class 'str'>
>>> employee1 = ('Jatin',)
>>> type(employee1)
<class 'tuple'>
>>> 
>>> 
>>> empty_list = list()
>>> empty_tuple = tuple()
>>> empty_list = []
>>> empty_tuple = ()
>>> 
>>> tot = (('Jatin', 35, 'Pune'), ('Aakash', 25, 'Bangalore')) # Tuple of Tuple
>>> tot[0]
('Jatin', 35, 'Pune')
>>> tot[0][-1]
'Pune'
>>> tot[0][-1] = 'U cant modify the same'
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    tot[0][-1] = 'U cant modify the same'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> 
>>> employee = {'name':'Jatin', 'age':35, 'location':'Pune'}
>>> 
>>> 
>>> # employee = {[1,2,3]:'Jatin'}
>>> # employee = {(1,2,3):'Jatin'}
>>> 
>>> print(employee)
{'name': 'Jatin', 'age': 35, 'location': 'Pune'}
>>> 
>>> employee = {'name':'Jatin', 'age':35, 'location':'Pune', 'name':'Rahul'}
>>> employee
{'name': 'Rahul', 'age': 35, 'location': 'Pune'}
>>> 
>>> employee['name'] # we have to provide a key not index
'Rahul'
>>> employee['location'] = 'Bangalore'
>>> employee
{'name': 'Rahul', 'age': 35, 'location': 'Bangalore'}
>>> del employee['age']
>>> employee['ManagerName'] = 'Aakash'
>>> employee
{'name': 'Rahul', 'location': 'Bangalore', 'ManagerName': 'Aakash'}
>>> 
>>> employee + employee
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    employee + employee
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> # is, in
>>> 
>>> employee2 = employee
>>> employee
{'name': 'Rahul', 'location': 'Bangalore', 'ManagerName': 'Aakash'}
>>> employee2
{'name': 'Rahul', 'location': 'Bangalore', 'ManagerName': 'Aakash'}
>>> employee2['age'] = 35
>>> employee
{'name': 'Rahul', 'location': 'Bangalore', 'ManagerName': 'Aakash', 'age': 35}
>>> 
>>> 'name' in employee
True
>>> 'Rahul' in employee
False
>>> # dictionary of dictionary
>>> # dictionary of list
>>> # dictionary of tuple
>>> # tuple of dict
>>> # list of dict
>>> 
>>> 
>>> empployees = {1: {'name':'Jatin', 'age':35}, 2:{'name':'Vikas', 'age':25}}
>>> employees = {1: {'name':'Jatin', 'age':35}, 2:{'name':'Vikas', 'age':25}}
>>> 
>>> 
>>> employees = {1: {'name':'Jatin', 'age':35}, 2:{'name':'Vikas', 'age':25}}
>>> employees[2]['name']
'Vikas'
>>> employees = {1: ['Jatin', 35], 2:['Vikas', 25]}
>>> employees[2][0]
'Vikas'
>>> employees = {1: ('Jatin', 35), 2:('Vikas', 25)}
>>> employees[2][0]
'Vikas'
>>> # tuple of dict
>>> employees = ({'name': 'Jatin','age': 35}, {'name':'Vikas', 'age':25})
>>> employees[1]['name']
'Vikas'
>>> employees = [{'name': 'Jatin','age': 35}, {'name':'Vikas', 'age':25}]
>>> employees[1]['name']
'Vikas'
>>> 
>>> 
>>> names = {'Jatin', 'Aakash', 'Mohan', 'Vijay'}
>>> type(names)
<class 'set'>
>>> # Unique
>>> names = {'Jatin', 'Aakash', 'Mohan', 'Vijay', 'Jatin'}
>>> names
{'Jatin', 'Aakash', 'Mohan', 'Vijay'}
>>> # immutiable
>>> names = {'Jatin', 'Aakash', 'Mohan', 'Vijay', ['Jatin', 'Vijay']}
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    names = {'Jatin', 'Aakash', 'Mohan', 'Vijay', ['Jatin', 'Vijay']}
TypeError: unhashable type: 'list'
>>> names[0]
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    names[0]
TypeError: 'set' object does not support indexing
>>> 
>>> 
>>> print(names)
{'Jatin', 'Aakash', 'Mohan', 'Vijay'}
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> names
{'Jatin', 'Aakash', 'Mohan', 'Vijay'}
>>> lastnames = {'Jatin', 'Mohan', 'Aditi', 'Ayushi'}
>>> 
>>> names
{'Jatin', 'Aakash', 'Mohan', 'Vijay'}
>>> lastnames
{'Jatin', 'Aditi', 'Mohan', 'Ayushi'}
>>> names - lastname
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    names - lastname
TypeError: unsupported operand type(s) for -: 'set' and 'str'
>>> names - lastnames
{'Vijay', 'Aakash'}
>>> lastnames - names
{'Aditi', 'Ayushi'}
>>> names & lastnames
{'Jatin', 'Mohan'}
>>> names | lastnames
{'Jatin', 'Ayushi', 'Aakash', 'Vijay', 'Mohan', 'Aditi'}
>>> names ^ lastnames
{'Ayushi', 'Aakash', 'Vijay', 'Aditi'}
>>> 
>>> 
>>> na = None
>>> yes = True
>>> no = False
>>> type(yes)
<class 'bool'>
>>> type(na)
<class 'NoneType'>
>>> 
