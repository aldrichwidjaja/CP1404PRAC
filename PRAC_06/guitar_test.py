from guitar import Guitar

CURRENT_YEAR = 2018

def guitartest():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1911
    cost = 20000

    guitar = Guitar(name, year, cost)
    another = Guitar("Another Guitar", 2000, 6400)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 107,guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another.name, 18,another.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,True,guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another.name,False,another.is_vintage()))

guitartest()