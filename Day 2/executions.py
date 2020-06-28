Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> global = 10
SyntaxError: invalid syntax
>>> 9var = 10
SyntaxError: invalid syntax
>>> var9 = 10
>>> print(Var9)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(Var9)
NameError: name 'Var9' is not defined
>>> 10 + 'jatin'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    10 + 'jatin'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> $var = 10
SyntaxError: invalid syntax
>>> __var = 10
>>> __var__ = 10
>>> 
>>> 
>>> print(__var)
10
>>> print(__var__)
10
>>> 
>>> _global = 10
>>> print(_global)
10
>>> sum = 10 # ??
>>> 
>>> sum([1,2,3])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sum([1,2,3])
TypeError: 'int' object is not callable
>>> 
=============================== RESTART: Shell ===============================
>>> print(var9)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(var9)
NameError: name 'var9' is not defined
>>> print(_global)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(_global)
NameError: name '_global' is not defined
>>> sum([1,2,3])
6
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> help(sum)
Help on built-in function sum in module builtins:

sum(iterable, start=0, /)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.

>>> help('global')
The "global" statement
**********************

   global_stmt ::= "global" identifier ("," identifier)*

The "global" statement is a declaration which holds for the entire
current code block.  It means that the listed identifiers are to be
interpreted as globals.  It would be impossible to assign to a global
variable without "global", although free variables may refer to
globals without being declared global.

Names listed in a "global" statement must not be used in the same code
block textually preceding that "global" statement.

Names listed in a "global" statement must not be defined as formal
parameters or in a "for" loop control target, "class" definition,
function definition, "import" statement, or variable annotation.

**CPython implementation detail:** The current implementation does not
enforce some of these restrictions, but programs should not abuse this
freedom, as future implementations may enforce them or silently change
the meaning of the program.

**Programmer's note:** "global" is a directive to the parser.  It
applies only to code parsed at the same time as the "global"
statement. In particular, a "global" statement contained in a string
or code object supplied to the built-in "exec()" function does not
affect the code block *containing* the function call, and code
contained in such a string is unaffected by "global" statements in the
code containing the function call.  The same applies to the "eval()"
and "compile()" functions.

Related help topics: nonlocal, NAMESPACES

>>> help(str.replace)
Help on method_descriptor:

replace(...)
    S.replace(old, new[, count]) -> str
    
    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.

>>> help(str.encoding)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    help(str.encoding)
AttributeError: type object 'str' has no attribute 'encoding'
>>> help(str.encode)
Help on method_descriptor:

encode(...)
    S.encode(encoding='utf-8', errors='strict') -> bytes
    
    Encode S using the codec registered for encoding. Default encoding
    is 'utf-8'. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
    'xmlcharrefreplace' as well as any other name registered with
    codecs.register_error that can handle UnicodeEncodeErrors.

>>> 
>>> 
>>> var = 10
>>> type(var) # class type of an object
<class 'int'>
>>> var2 = 10.1
>>> type(var2) # class type of an object
<class 'float'>
>>> var3 = 3 + 4j
>>> type(var3) # class type of an object
<class 'complex'>
>>> 
>>> # Operator - Arithmetic Opr
>>> # +, -, *, /, %, **, // (floor Division)
>>> 10 + 3
13
>>> 10 - 3
7
>>> 10 * 3
30
>>> 10 / 3 # both are intergers here
3.3333333333333335
>>> # In python2 - Integer
>>> # In Python3 - Interger divide by interger may return float value as well
>>> 10 * 2 / 3
6.666666666666667
>>> 
>>> 10 ** 2 * 3 / 2 + 10 - 2
158.0
>>> 10 ** (2 * (3 / 2)) + 10 - 2
1008.0
>>> 11 % 3
2
>>> 11 // 3
3
>>> import math
>>> math.ceil(11/3)
4
>>> import math
>>> 10 ** (2 * (3 / 2)) + 10 - 2
1008.0
>>> # True, False
>>> 
>>> var = True
>>> var = true
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    var = true
NameError: name 'true' is not defined
>>> type(var)
<class 'bool'>
>>> var2 = False
>>> type(var2)
<class 'bool'>
>>> 
>>> # Comparison  - ==, !=, >, <, >=, <=
>>> 
>>> 10 == 10.0 #  Implicit - done by programing, excilit - by the user
True
>>> 10.1 > 10
True
>>> int(10.1) > 10
False
>>> int(10.1) > float(10)
False
>>> int(10.1) >= float(10)
True
>>> int(10.1) =< float(10)
SyntaxError: invalid syntax
>>> int(10.1) <= float(10)
True
>>> # <> behave same !=
>>> 
>>> # is, is not - Identity
>>> 
>>> var = 10
>>> var2 = var # what is the meaning of this statement?
>>> 
>>> var is var2
True
>>> var == var2
True
>>> 
>>> a = 1000
SyntaxError: unexpected indent
>>> a = 1000
>>> b = 100
>>> b = 1000
>>> 
>>> a
1000
>>> b
1000
>>> a == b
True
>>> a is b
False
>>> id(a)
4611956048
>>> id(b)
4611956656
>>> id(var)
4304849568
>>> id(var2)
4304849568
>>> 
>>> 
>>> 
>>> 
>>> 
>>> var = 200
>>> var2 = 200
>>> 
>>> var is var2 #??
True
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> var = 200
>>> var2 = 200
>>> var is var2 #??
True
>>> var3 = 300
>>> var4 = 300
>>> var3 is var4 #??
False
>>> id(var)
4304855648
>>> id(var2)
4304855648
>>> id(var3)
4611949264
>>> id(var4)
4611949552
>>> 
>>> # Assignment Opr
>>> var = 10
>>> id(var)
4304849568
>>> var += 20 # var = var + 20
>>> id(var)
4304850208
>>> var *= 20 # ++var
>>> var
600
>>> 
>>> var5 = 10
>>> id(var5)
4304849568
>>> 
