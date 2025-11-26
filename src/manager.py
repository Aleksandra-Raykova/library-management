# manager.py
from models import Book, Library

library = Library()


def validate_positive_integer(msg):
    while True:
        value = input(msg)
        if value.isdecimal():
            return int(value)
        print("Enter a positive integer.")


def add_book_to_library():
    book_title = input("Book title: ").strip()
    book_author = input("Book author: ").strip()
    book_year = validate_positive_integer("Book year: ")
    book = Book(title=book_title, author=book_author, year=book_year)
    library.add_book(book)
    print(f"Book {book} is added to Library")


def remove_book():
    book_id = validate_positive_integer("Book ID: ")
    removed_book = library.remove_book(book_id)
    print(f"Book {removed_book} is removed from Library")


def list_all_available_books():
    all_available_books = library.list_available_books()
    if all_available_books:
        print("\n".join([str(b) for b in all_available_books]))
    else:
        print("No books available")


def search_books_by_title():
    search_input = input("Search book by title: ")
    all_filtered_books = library.find_by_title(search_input)
    if not all_filtered_books:
        print("No books found with the given search")
    else:
        print("All found books:")
        print("\n".join([str(b) for b in all_filtered_books]))


def borrow_book_from_library():
    book_id = validate_positive_integer("Book ID: ")
    book_object = library.get_book(book_id)
    book_object.borrow()
    print(f"Book {book_object} is borrowed from Library")


def return_book_to_library():
    book_id = validate_positive_integer("Book ID: ")
    book_object = library.get_book(book_id)
    book_object.return_back()
    print(f"Book {book_object} is returned to Library")


def save():
    file_name = input("Add file name: ")
    library.save_doc(file_name)
    print("Saved.")


def load():
    file_name = input("Add file name: ")
    library.load_doc(file_name)
    print("Loaded.")
