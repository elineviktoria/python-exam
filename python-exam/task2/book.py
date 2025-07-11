# --- Book Class Implementation ---
class Book:
    """
    Representa an individual book in the library
    - attributes: title, author, num_pages, is_checked_out
    """

    def __init__(self, title, author, num_pages):
        # constructor for the Book class  - initializes the book's attributes
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.is_checked_out = False # a new book is initially available

    def __str__(self):
        # returns a user-friendly string representation of the book
        status = "Checked out" if self.is_checked_out else "Available"
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.num_pages}, Status: {status}"
    
    # a __repr__ method (can also be useful for developers)
    def __repr__(self):
        # returns an unambiguous string representation of the book object - useful for debugging
        return f"Book(title='{self.title}', author='{self.author}', pages='{self.num_pages}', is_checked_out='{self.is_checked_out}')"