class Shoe:
    def __init__(self, brand, size):
        """
        Initialize a Shoe object.

        Parameters:
        - brand (str): The brand of the shoe.
        - size (int): The size of the shoe.
        """
        self.brand = brand
        self.size = size
        self.condition = "Used"

    def cobble(self):
        """Simulate cobbling, repairing the shoe."""
        print("Your shoe is as good as new!")
        self.condition = "New"

    @property
    def brand(self):
        """Get the brand of the shoe."""
        return self._brand

    @brand.setter
    def brand(self, value):
        """Set the brand of the shoe."""
        self._brand = value

    @property
    def size(self):
        """Get the size of the shoe."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the shoe with validation."""
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
