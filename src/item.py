class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        output = f' You see a {self.description} {self.name}.'

        return output


i = Item("rock", "big")
print(i)
