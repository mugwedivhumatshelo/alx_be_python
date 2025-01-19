class Book:
    def __init__(self, title, author):
        """
        Initializes a Book instance.

        Args:
        title (str): The title of the book.
        author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """
        Marks the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as returned.
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Checks if the book is available.

        Returns:
        bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out

class Library:
    def __init__(self):
        """
        Initializes a Library instance.
        """
        self._books = []

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
        book (Book): The book to add.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book from the library.

        Args:
        title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"'{title}' is not available or does not exist in the library.")

    def return_book(self, title):
        """
        Returns a book to the library.

        Args:
        title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"'{title}' is not checked out or does not exist in the library.")

    def list_available_books(self):
        """
        Lists all available books in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are available.")
