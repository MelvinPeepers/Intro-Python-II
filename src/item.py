# Create a file called item.py and add an Item class in there.

# The item should have name and description attributes.

# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.


class Item:
    def __init__(self, name, description, size, color, weight):
        self.name = name
        self.description = description
        self.size = size
        self.color = color
        self.weight = weight

    def __str__(self):
        output = f' You see a {self.description} {self.name}.'

        return output

    def pickup(self):
        return(f'???')


class Rock(Item):
    def __init__(self, name, size):
        super().__init__(name, "solid", size, "grey", "heavy")

    def pickup(self):
        return(f'You pickup {self.size} {self.name}.')


i = Item("Candlestick", "metal", "long", "gold", "heavy")
r = Rock("rock", "big")
print(r.pickup())
