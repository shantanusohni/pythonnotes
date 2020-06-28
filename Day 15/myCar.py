

class Car(object):  # object - python builtin class - which contains default actions
    no_of_tyres = 5
    steering_type = 'Manual'

    __enginetype__ = 'ford' # python2 - such variable are not directly accessible by instance

audi = Car() # How we create an instance/object of Car class
merc = Car()

print(audi.__enginetype__)

"""
Car.no_of_tyres = 7
merc.no_of_tyres = 6 # instance attribute

# name = 'Jatin' # creating a string object
# name = str() # creating a string object
# numbers = list() # creating a list object

print(audi.no_of_tyres) # 5
print(audi.steering_type) # manual

print(merc.no_of_tyres)  # 6
print(merc.steering_type)  # manual

print(Car.no_of_tyres) # class attribute
print(Car().no_of_tyres) # accessing again which an object but on the fly attribute
"""


