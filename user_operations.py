
class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []  # Private attribute to track borrowed books
    

    def get_name(self):
        return self.__name

    def set_name(self):
        from validation import Validate
        valid = Validate
        self.__name = valid.validate_name()

    def get_library_id(self):
        return self.__library_id

    def set_library_id(self, library_id):
        from validation import Validate
        valid = Validate
        self.__library_id = valid.validate_id(library_id)

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, title):
        from library import Library
        library = Library 
        book = library.find_book(title) 
        if book:
            if book.get_availability(): 
                book.set_availability(False)  # Mark the book as borrowed
                self.__borrowed_books.append(book.get_title())  # Add to borrowed books
                print(f"You have borrowed '{book.get_title()}'.")
            else:
                print("The book is currently not available.")
        else:
            print("Book not found.")

    def return_book(self, title):
        from library import Library
        library = Library 
        book = library.find_book(title)  
        if book:
            if title in self.__borrowed_books:
                book.set_availability(True)  # Mark the book as available
                self.__borrowed_books.remove(title)  # Remove from borrowed books
                print(f"You have returned '{book.get_title()}'.")
            else:
                print("You have not borrowed this book.")
        else:
            print("Book not found.")

    def display_info(self):
        return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {', '.join(self.__borrowed_books)}"
