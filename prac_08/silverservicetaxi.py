from taxi import Taxi

class silverservice(Taxi):
    first_fare = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name,fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} with first fare of ${:.2f}".format(super().__str__(), self.first_fare)

    def get_price(self):
        test = float(self.first_fare + super().get_fare())
        return test
