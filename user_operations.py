
class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []  # Private attribute to track borrowed books

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_library_id(self):
        return self.__library_id

    def set_library_id(self, library_id):
        self.__library_id = library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(book_list, user):
        title = input("Enter the title of the book to borrow: ")

        for book in book_list:
            if book.get_title().lower() == title.lower():
                if book.is_available():
                    book.set_availability(False)  # Mark the book as borrowed
                    user.borrow_book(title)
                    print(f"You have borrowed '{book.get_title()}'.")
                else:
                    print("The book is currently not available.")
                return
        print("Book not found.")

    def return_book(book_list, user):
        title = input("Enter the title of the book to return: ")

        for book in book_list:
            if book.get_title().lower() == title.lower():
                if title in user.get_borrowed_books():
                    book.set_availability(True)  # Mark the book as available
                    user.return_book(title)
                    print(f"You have returned '{book.get_title()}'.")
                else:
                    print("You have not borrowed this book.")
                return
        print("Book not found.")


    def display_info(self):
        return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {self.__borrowed_books}"
