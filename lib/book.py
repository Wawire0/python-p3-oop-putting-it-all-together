class Book:
    def __init__(self, title, page_count):
        """
        Initialize a Book object.

        Parameters:
        - title (str): The title of the book.
        - page_count (int): The page count of the book.
        """
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        """Simulate turning a page."""
        print("Flipping the page...wow, you read fast!")

    @property
    def title(self):
        """Get the title of the book."""
        return self._title

    @title.setter
    def title(self, value):
        """Set the title of the book."""
        self._title = value

    @property
    def page_count(self):
        """Get the page count of the book."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Set the page count of the book with validation."""
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value
