# models.py
import json
from itertools import count
from dataclasses import dataclass, field, asdict
from typing import Dict, List


@dataclass
class Book:
    book_id: int = field(init=False)
    title: str
    author: str
    year: int
    is_available: bool = field(default=True)

    _counter = count(1)

    def __post_init__(self):
        if self.year <= 0:
            raise ValueError("Year must be positive integer")

        self.book_id = next(Book._counter)

    def borrow(self):
        if not self.is_available:
            raise ValueError("Book already borrowed.")
        self.is_available = False

    def return_back(self):
        if self.is_available:
            raise ValueError("Book is not borrowed.")
        self.is_available = True

    def __str__(self):
        status = "available" if self.is_available else "borrowed"
        return f"[{self.book_id}] {self.title} — {self.author} ({self.year}) |{status}|"


class Library:
    def __init__(self):
        self.books: Dict[int, Book] = {}

    def add_book(self, book: Book):
        self.books[book.book_id] = book

    def remove_book(self, book_id) -> Book:
        try:
            return self.books.pop(book_id)
        except KeyError:
            raise ValueError("No book with such ID.")

    def get_book(self, book_id) -> Book:
        book = self.books.get(book_id)
        if book:
            return book
        else:
            raise ValueError("No book with such ID.")

    def find_by_title(self, text: str) -> List[Book]:
        text = text.lower().strip()
        return [b for b in self.books.values() if text in b.title.lower()]

    def list_available_books(self):
        return [b for b in self.books.values() if b.is_available]

    def save_doc(self, filename: str):
        books_info = [asdict(b) for b in self.books.values()]
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(books_info, fp=f, indent=4)

    def load_doc(self, filename: str):
        with open(filename, "r", encoding='utf-8') as f:
            books_info = json.load(f)

        self.books.clear()
        for data in books_info:
            book = Book(title=data["title"], author=data["author"], year=data["year"])
            book.book_id = data["book_id"]
            self.add_book(book)

        # update counter
        max_id = max(self.books.keys(), default=0)
        Book._counter = count(max_id + 1)
