class Car(object):

    def __init__(self, direction='straight'):
        self.direction = direction

    def __del__(self):
        print('Removing an object of Car class')


audi = Car('left')
bmw = Car()
merc = Car(direction='right')

print(audi.direction) # left
print(bmw.direction) # straight
print(merc.direction) # right