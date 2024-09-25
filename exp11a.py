# Base class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title       # Title of the book
        self.author = author     # Author of the book
        self.isbn = isbn         # ISBN number of the book

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
    ebook = EBook("Python Programming", "John Doe", "123456789", 2.5)
    printed_book = PrintedBook("Learn Python the Hard Way", "Zed A. Shaw", "987654321", "A3")

    # Display information about each book
    print("EBook Information:")
    print(ebook.display_info())
    print("\nPrinted Book Information:")
    print(printed_book.display_info())

if __name__ == "__main__":
    main()
