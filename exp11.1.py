import re

# Custom exception for invalid ISBN
class InvalidISBNError(Exception):
    """Exception raised for invalid ISBN format."""
    pass

# Base class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title       # Title of the book
        self.author = author     # Author of the book
        self.isbn = self.validate_isbn(isbn)  # Validate ISBN

    def validate_isbn(self, isbn):
        """Validate the ISBN format (10 or 13 digits)."""
        if not re.match(r'^(?:ISBN(?:-1[03])?: )?(?=[0-9]{10}|[0-9]{13}$)[0-9\-]*$', isbn):
            raise InvalidISBNError(f"Invalid ISBN format: {isbn}")
        return isbn

    def display_info(self):
        """Display information about the book."""
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}"

# Subclass for EBooks
class EBook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)  # Call to the base class constructor
        self.file_size = file_size  # File size of the eBook in MB

    def display_info(self):
        """Display information about the eBook."""
        base_info = super().display_info()  # Get base class info
        return f"{base_info}\nFile Size: {self.file_size} MB"

# Subclass for Printed Books
class PrintedBook(Book):
    def __init__(self, title, author, isbn, shelf_location):
        super().__init__(title, author, isbn)  # Call to the base class constructor
        self.shelf_location = shelf_location  # Shelf location of the printed book

    def display_info(self):
        """Display information about the printed book."""
        base_info = super().display_info()  # Get base class info
        return f"{base_info}\nShelf Location: {self.shelf_location}"

# Main function to demonstrate the classes
def main():
    # Create instances of EBook and PrintedBook
    try:
        ebook = EBook("Python", "Chintu Tyagi", "123456", 2.5)
        printed_book = PrintedBook("Java", "Mustafa", "65329", "B7")
    
        # Display information about each book
        print("EBook Information:")
        print(ebook.display_info())
        print("\nPrinted Book Information:")
        print(printed_book.display_info())
    except InvalidISBNError as e:
        print(e)

if __name__ == "__main__":
    main()
