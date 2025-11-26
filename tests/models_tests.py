# models_tests.py

import os
import unittest
from src.models import Book, Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Set up a fresh library before each test."""
        self.library = Library()

    def test_add_book_adds_book_to_dictionary_with_correct_id_as_key(self):
        """
        Ensures:
        - Books get unique, auto-incremented IDs
        - Each key leads to the correct book with the corresponding id
        """

        # Add first book
        b1 = Book("Test Book 1", "Author A", 2001)
        self.library.add_book(b1)

        # Get the only key of the books dict which must equals 1
        actual_keys = self.library.books.keys()
        self.assertIn(1, actual_keys)

        # Add second book
        b2 = Book("Test Book 2", "Author B", 2002)
        self.library.add_book(b2)

        # The books dict should now have 2 key-values pairs and the second key=2
        actual_keys = self.library.books.keys()
        self.assertEqual(len(actual_keys), 2)
        self.assertIn(2, actual_keys)

        # The key=2 should lead to Test Book 2
        second_book = self.library.books[2]
        self.assertEqual(second_book.book_id, 2)
        self.assertEqual(second_book.title, "Test Book 2")
        self.assertEqual(second_book.author, "Author B")
        self.assertEqual(second_book.year, 2002)

    def test_add_and_save_load_preserves_unique_ids(self):
        """
        Ensures:
        - Books get unique, auto-incremented IDs
        - Saving to JSON and loading back recreates valid Book objects
        - Loading does NOT duplicate IDs or break availability flags
        """

        # Add initial books
        b1 = Book("Test Book 1", "Author A", 2001)
        b2 = Book("Test Book 2", "Author B", 2002)
        self.library.add_book(b1)
        self.library.add_book(b2)

        # Save to temp file
        filename = "test_books.json"
        self.library.save_doc(filename)

        # Load into a new library instance
        library = Library()
        library.load_doc(filename)

        # Check book count
        self.assertEqual(len(library.books), 2)

        # Ensure IDs are still unique and sequential
        loaded_ids = sorted(library.books.keys())
        self.assertEqual(loaded_ids, [1, 2])

        # Check attributes of a loaded book
        loaded_book = library.books[1]
        self.assertEqual(loaded_book.title, "Test Book 1")
        self.assertEqual(loaded_book.author, "Author A")
        self.assertTrue(loaded_book.is_available)

        # Cleanup
        os.remove(filename)


if __name__ == "__main__":
    unittest.main()
