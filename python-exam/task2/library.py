# --- Library Class Implementation ---
from book import Book # import book object (file)

class Library: 
    """
    Represents the library, responsible for managing a collection of Book objects
    - attributes: books (a list of book objects)
    """

    def __init__(self):
        # Constructor for the Library class - initializes an empty list to store books
        self.books = []

    def _find_book(self, title):
        # Helper method to find a book in the library by its title (internal method)

        # loop through the list of books
        for book_in_library in self.books:
            if book_in_library.title.lower() == title.lower():
                return book_in_library
        return None # book not found
    
    def add_book(self, book_object):
        # Adds a Book object to the Library
        if self._find_book(book_object.title):
            print(f"Info: A book with the title {book_object.title} already exists in the library. Not adding duplicate.")
        else:
            self.books.append(book_object) 
            print(f"Book added: {book_object.title} by {book_object.author}")

    def remove_book(self, title):
        # Removed a book from the library based on its title
        book_to_remove = self._find_book(title)
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Book removed: {title}.")

    def check_out(self, title):
        # Allows a library visitor to borrow a book
        book_to_checkout = self._find_book(title)
        if book_to_checkout:
            if not book_to_checkout.is_checked_out: # check current status
                book_to_checkout.is_checked_out = True
                print(f"Book checked out: '{title}'.")
            else:
                print(f"Info: Book '{title}' is already checked out.")
        else:
            print(f"Error: Book with title '{title}' not found. Cannot check out.")

    def check_in(self, title):
        # Allows a library visitor to return a book
        book_to_checkin = self._find_book(title)
        if book_to_checkin:
            if book_to_checkin.is_checked_out: # check current status
                book_to_checkin.is_checked_out = False
                print(f"Book checked in: '{title}'")
            else:
                print(f"Info: Book '{title}' was not checked out (already available).")
        else:
            print(f"Error: Book with title '{title}' not found. Cannot check in.")

    def display_all_books(self):
        # Displays details of all books currently in the library
        if not self.books:
            print("\nThe library is currently empty.")
            return
        
        print("\n--- Library Book Inventory ---")
        for book_in_library in self.books:
            print(book_in_library)
        print("-" * 40) 