from car import Car
from random import randint

class carreliable(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self,distance):
        randomnumber = randint(0,100)
        if randomnumber >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven