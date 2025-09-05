"""
TASK: Create a Library class.

Requirements:
1. The class should track available books (list).
2. Provide a method to add new books to the library.
3. Provide a method for users to borrow books.
   - Remove the borrowed book from available list.
   - Store borrowed books with user info.
4. Provide a method for returning borrowed books.
5. Provide a method to show all available books.

Example Usage:
    lib = Library()
    lib.add_book("Python 101")
    lib.add_book("Data Science Handbook")
    lib.borrow_book("Alice", "Python 101")
    print(lib.show_available_books())  # ["Data Science Handbook"]
    lib.return_book("Alice")
    print(lib.show_available_books())  # ["Data Science Handbook", "Python 101"]
"""
class Library:
    def __init__(self):
        self.available_books = []
        self.borrowed_books = {}

    def add_book(self, book_title):
        """Add a new book to the library."""
        self.available_books.append(book_title)

    def borrow_book(self, user, book_title):
        """Allow a user to borrow a book if available."""
        if book_title in self.available_books:
            self.available_books.remove(book_title)
            self.borrowed_books[user] = book_title
            print(f"{user} borrowed '{book_title}'.")
        else:
            print(f"Sorry, '{book_title}' is not available.")

    def return_book(self, user):
        """Allow a user to return a borrowed book."""
        if user in self.borrowed_books:
            book_title = self.borrowed_books[user]
            self.available_books.append(book_title)
            del self.borrowed_books[user]
            print(f"{user} returned '{book_title}'.")
        else:
            print(f"{user} has no borrowed books.")

    def show_available_books(self):
        """Return a list of available books."""
        return self.available_books



lib = Library()
lib.add_book("Python 101")
lib.add_book("Data Science Handbook")

lib.borrow_book("Alice", "Python 101")
print(lib.show_available_books()) 

lib.return_book("Alice")
print(lib.show_available_books())  
