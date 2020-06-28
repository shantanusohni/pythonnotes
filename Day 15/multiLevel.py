class Car(object):

    def moveCar(self, direction):
        self.direction = direction
        print('Car is moving towards {} direction'.format(direction))

    def get_direction(self):
        return self.direction

class EuroCar(Car):
    def moveCar(self, direction):
        self.direction = direction
        print('EuroCar is moving towards {} direction'.format(direction))
        super(EuroCar, self).moveCar(direction=direction)

class AmericanCar(Car):

    def moveCar(self, direction):
        self.direction = direction
        print('AmericanCar is moving towards {} direction'.format(direction))
        super(AmericanCar, self).moveCar(direction=direction)

class IndianCar(AmericanCar, EuroCar):

    def moveCar(self, direction):
        self.direction = direction
        print('IndianCar is moving towards {} direction'.format(direction))
        super(IndianCar, self).moveCar(direction=direction)

audi = IndianCar()
audi.moveCar('left')