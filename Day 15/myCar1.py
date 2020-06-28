class Car(object):

    def moveCar(self, direction):
        self.direction = direction
        print('Car is moving towards {} direction'.format(direction))

    def get_direction(self):
        return self.direction

if __name__ == '__main__':
    audi = Car()
    merc = Car()
    audi.moveCar('Straight')
    merc.moveCar('straight')
    print(audi.get_direction())
