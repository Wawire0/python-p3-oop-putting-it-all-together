class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("Size must be an integer")
        elif value <= 0:
            print("Size must be a positive integer")
        else:
            self._size = value
