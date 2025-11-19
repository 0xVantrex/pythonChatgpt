class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Member:
    def __init__(self, name, memberid):
        self.name = name
        self.memberid = memberid
        self.borrowedbooks = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowedbooks.append(book)
            return f"{self.name} borrowed {book.title}"
        else:
            return f"{book.title} is not available."

    def return_book(self, book):
        if book in self.borrowedbooks:
            book.available = True
            self.borrowedbooks.remove(book)
            return f"{self.name} returned {book.title}"
        else:
            return f"{self.name} does not have that book."


class Librarian(Member):
    def add_book(self, book, catalog):
        catalog.append(book)
        return f"Added {book.title} to catalog."

    def remove_book(self, book, catalog):
        if book in catalog:
            catalog.remove(book)
            return f"Removed {book.title} from catalog."
        return "Book not in catalog."


class Library:
    def __init__(self):
        self.catalog = []

    def searchbytitle(self, title):
        return [book for book in self.catalog if title.lower() in book.title.lower()]

    def display_books(self):
        for book in self.catalog:
            status = "Available" if book.available else "Borrowed"
            print(f"{book} - {status}")

# ---- TESTING ----

# Create a library
lib = Library()

# Create books
b1 = Book("Harry Potter", "J.K. Rowling", "12345")
b2 = Book("The Hobbit", "Tolkien", "67890")

# Add books to the library
librarian = Librarian("Alice", "L001")
print(librarian.add_book(b1, lib.catalog))
print(librarian.add_book(b2, lib.catalog))

# Display books
lib.display_books()

# Create a member
m = Member("John", "M001")

# Borrow a book
print(m.borrow_book(b1))

# Try borrowing the same book again
print(m.borrow_book(b1))

# Return the book
print(m.return_book(b1))

# Display books again
lib.display_books()
