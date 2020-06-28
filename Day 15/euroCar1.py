
class Car(object):

    def moveCar(self, direction):
        self.direction = direction
        print('Car is moving towards {} direction'.format(direction))

    def get_direction(self):
        return self.direction

class EuroCar(Car):
    pass

class AmericanCar(EuroCar):

    def moveCar(self, direction):
        self.direction = direction
        print('AmericanCar is moving towards {} direction'.format(direction))
        super(AmericanCar, self).moveCar(direction=direction)


audi = AmericanCar()
audi.moveCar('left')