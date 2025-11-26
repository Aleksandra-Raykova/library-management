# Library Console App

A small practice project with basic Python OOP, object modeling, simple data structures, and a console-based interface.
The application lets you add, remove, search, borrow, and return books, as well as save and load the library state from a JSON file.

This project isn’t meant to be a full system — just a straightforward exercise.

---

## Features

- Create books with unique, auto-incremented IDs
- Manage books through a `Library` class
- Search books by title
- List available books
- Borrow and return functionality
- Save and load library data using a JSON file
- Basic console menu (text UI)

---

## Project Structure

```
project/
│
├── src/
│ ├── models.py # Book and Library classes (core logic)
│ ├── manager.py # Console interaction functions
│ └── controller.py # Menu loop and program entry point
│
├── tests/
│ └── models_tests.py # Basic unit tests
│
└── example.json # Example book data for loading
```

---

## Tests

A few unit tests are included, covering:

- Adding books and verifying ID generation
- Saving and loading data while preserving identifiers

The tests don’t cover every feature, but they reflect the scope of this small practice project.

---

## How to Run

```bash
python src/controller.py
```

---

## Example Data

An example.json file is included.
It can be loaded using the "9 Load" functionality to quickly populate the library with sample books. Then, write "example.json" as input.
