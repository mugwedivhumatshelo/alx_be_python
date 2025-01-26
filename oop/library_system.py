class Book:
    def __init__(self, title, author):
        """
        Initializes a Book instance with title and author.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the book.
        
        Returns:
            str: A string representation of the book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Initializes an EBook instance with title, author, and file size.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            file_size (int): The file size of the eBook in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the eBook.
        
        Returns:
            str: A string representation of the eBook.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook instance with title, author, and page count.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            page_count (int): The page count of the print book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the print book.
        
        Returns:
            str: A string representation of the print book.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """
        Initializes a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library's collection.
        
        Args:
            book (Book): The book to be added.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of each book in the library's collection.
        """
        for book in self.books:
            print(book)
