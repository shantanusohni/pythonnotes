"""
This is a convention that whenver u create a module
you should provide the documentation, generally as help
page of a module
"""

def add(a, b):
    """
    This is a documentation of add function
    which accept a and b return sum of a and b
    ex:
    add(10, 20) --> 30
    """
    return a + b

def mul(a, b):
    """
    This is a documentation of mul function
    which accept a and b return multiplication of a and b
    ex:
    mul(10, 20) --> 200
    """
    return a * b

if __name__ == '__main__':
    print('Lets call an add function: ', add(10, 30))
    print('Lets call an mul function: ', mul(10, 30))
