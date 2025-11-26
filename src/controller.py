# controller.py
import manager

MENU = {
    "1": manager.add_book_to_library,
    "2": manager.remove_book,
    "3": manager.list_all_available_books,
    "4": manager.search_books_by_title,
    "5": manager.borrow_book_from_library,
    "6": manager.return_book_to_library,
    "7": manager.save,
    "8": manager.load,
}


while True:
    choice = input(
        "Please choose one of the following (1 to 9):\n"
        "1 Add\n"
        "2 Remove\n"
        "3 List available\n"
        "4 Search\n"
        "5 Borrow\n"
        "6 Return\n"
        "7 Save\n"
        "8 Load\n"
        "9 Exit\n"
        ">"
    )

    if choice == "9":
        print("Program ended")
        break

    action = MENU.get(choice)
    if action:
        try:
            action()
        except Exception as e:
            print("Error:", e)
    else:
        print("Invalid.")
