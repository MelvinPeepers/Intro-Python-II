# Create a file called item.py and add an Item class in there.

# The item should have name and description attributes.

# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.description} {self.name}'

    def pickup(self):
        return(f'pickup {self.name}')


class Rock(Item):
    def __init__(self, name, description, size):
        super().__init__(name, description)  # a way to access Parent Product Class
        self.size = size

    def __str__(self):
        return super().__str__() + (f" that's {self.size}")

    def pickup(self):
        return super().pickup() + (f'.')


class Candlestick(Item):
    def __init__(self, name, description, make):
        super().__init__(name, description)  # a way to access Parent Product Class
        self.make = make

    def __str__(self):
        return super().__str__() + (f" that's {self.make}")


class SilverBullets(Item):
    def __init__(self, name, description, quantity):
        super().__init__(name, description)  # a way to access Parent Product Class
        self.quantity = quantity

    def __str__(self):
        return super().__str__() + (f" {self.quantity}")


class Revolver(Item):
    def __init__(self, name, description, caliber):
        super().__init__(name, description)  # a way to access Parent Product Class
        self.caliber = caliber

    def __str__(self):
        return super().__str__() + (f" {self.caliber}")


i = Item("Treasure box", "empty")
r = Rock("rock", "bloody", "big")
c = Candlestick("Candlestick", "deadly", "gold")
s = SilverBullets("Silver Bullets", "shiny", "6")
g = Revolver("Colt", "templated", ".45")
print(i)
print(r)
print(c)
print(s)
print(g)
print(i.pickup())
print(r.pickup())
print(c.pickup())
print(s.pickup())
print(g.pickup())
