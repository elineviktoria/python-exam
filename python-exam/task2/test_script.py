# --- Test Script ---
from book import Book
from library import Library

if __name__ == "__main__":
    print("--- Starting Library Management System Test ---")

    # 1. create a library instance
    my_library = Library()
    print(f"\n1. Library instance created.")
    my_library.display_all_books() # should be empty

    # 2. add multiple books to the library
    print("\n2. Adding books to the library...")
    book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1200)
    book2 = Book("Pride and Prejudice", "Jane Austen", 400)
    book3 = Book("1984", "George Orwell", 328)
    book4 = Book("To Kill a Mockingbird", "Harper Lee", 281)

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.add_book(book4)
    my_library.add_book(Book("1984", "George Orwell", 328)) # attempt to add duplicate

    my_library.display_all_books()

    # 3. attempt to check out a book
    print("\n3. Attempting to check out books...")
    my_library.check_out("Pride and Prejudice") # successful checkout
    my_library.check_out("The Lord of the Rings") # successful checkout
    my_library.check_out("Pride and Prejudice") # already checked out
    my_library.check_out("NonExistent Book") # book not found

    my_library.display_all_books() # verify status change

    # 4. attempt to return a book
    print("\n4. Attempting to return (check in) books...")
    my_library.check_in("Pride and Prejudice") # successful check-in
    my_library.check_in("Pride and Prejudice") # already checked in (available)
    my_library.check_in("NonExistent Book") # book not found
    my_library.check_in("1984") # was never checked out

    my_library.display_all_books() # verify status change

    # 5. remove a book from the library
    print("\n5. Removing book...")
    my_library.remove_book("To Kill a Mockingbird") # remove existing book
    my_library.remove_book("To Kill a Mockingbird") # remove alredy removed book    
    my_library.remove_book("Another NonExistent Book") # remove nonexisting book

    my_library.display_all_books() # verify status change    

    # 6. print the list of books to verify the results
    print("\n6. Final list of books in the library: ")
    my_library.display_all_books()

    print("\n--- Library Management System Test Finished ---")