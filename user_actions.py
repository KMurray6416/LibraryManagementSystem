from library import Library
from validation import Validate 
valid = Validate

class UserInterface:
    def __init__(self):
        self.library = Library()

    def get_valid_input(self, prompt, validation_func, error_message):
        """Prompt user and validate input using a validation function."""
        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            print(error_message)

    def display_main_menu(self):
        print("\nWelcome to the Library Management System!")
        while True:
            try:
                print("\nMain Menu:")
                print("1. Book Operations")
                print("2. User Operations")
                print("3. Author Operations")
                print("4. Quit")
                choice = input("Choose an option: ")
                if not choice.isdigit() or int(choice) not in range(1, 5):
                    print("Invalid choice. Please enter a number between 1 and 4.")
                    continue

                choice = int(choice)
                if choice == 1:
                    self.book_ops_menu()
                elif choice == 2:
                    self.user_ops_menu()
                elif choice == 3:
                    self.author_ops_menu()
                elif choice == 4:
                    print("Exiting the system.")
                    break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def book_ops_menu(self):
        while True:
            try:
                print("\nBook Operations:")
                print("1. Add a new book")
                print("2. Borrow a book")
                print("3. Return a book")
                print("4. Search for a book")
                print("5. Display all books")
                print("6. Back to main menu")
                choice = input("Choose an option: ")
                if not choice.isdigit() or int(choice) not in range(1, 7):
                    print("Invalid choice. Please enter a number between 1 and 6.")
                    continue

                choice = int(choice)
                if choice == 1:
                    title = self.get_valid_input(
                        "Enter book title: ", valid.validate_title, "Invalid title format."
                    )
                    author = self.get_valid_input(
                        "Enter author: ", valid.validate_name, "Invalid name format."
                    )
                    genre = input("Enter genre: ")  # Assuming free input for genre
                    pub_date = input("Enter publication date (e.g., YYYY): ")  # Add further validation if needed
                    self.library.add_book(title, author, genre, pub_date)
                elif choice == 2:
                    library_id = self.get_valid_input(
                        "Enter your library ID (e.g., AB-12345): ",
                        valid.validate_id,
                        "Invalid library ID format.",
                    )
                    title = self.get_valid_input(
                        "Enter the book title: ", valid.validate_title, "Invalid title format."
                    )
                    user = self.library.find_user(library_id)
                    book = self.library.find_book(title)
                    if user and book:
                        if book.borrow_book():
                            user.borrow_book(title)
                            print("Book borrowed successfully.")
                        else:
                            print("Book is not available.")
                    else:
                        print("User or Book not found.")
                elif choice == 3:
                    library_id = self.get_valid_input(
                        "Enter your library ID (e.g., AB-12345): ",
                        valid.validate_id,
                        "Invalid library ID format.",
                    )
                    title = self.get_valid_input(
                        "Enter the book title: ", valid.validate_title, "Invalid title format."
                    )
                    user = self.library.find_user(library_id)
                    book = self.library.find_book(title)
                    if user and book:
                        if user.return_book(title):
                            book.return_book()
                            print("Book returned successfully.")
                        else:
                            print("This user did not borrow the book.")
                    else:
                        print("User or Book not found.")
                elif choice == 4:
                    title = self.get_valid_input(
                        "Enter the book title to search: ", valid.validate_title, "Invalid title format."
                    )
                    book = self.library.find_book(title)
                    if book:
                        print(book.display_info())
                    else:
                        print("Book not found.")
                elif choice == 5:
                    books = self.library.list_books()
                    if books:
                        for book in books:
                            print(book)
                    else:
                        print("No books available.")
                elif choice == 6:
                    break
            except Exception as e:
                print(f"An error occurred: {e}")

    def user_ops_menu(self):
        while True:
            try:
                print("\nUser Operations:")
                print("1. Add a new user")
                print("2. View user details")
                print("3. Display all users")
                print("4. Back to main menu")
                choice = input("Choose an option: ")

                if not choice.isdigit() or int(choice) not in range(1, 5):
                    print("Invalid choice. Please enter a number between 1 and 4.")
                    continue

                choice = int(choice)
                if choice == 1:
                    name = self.get_valid_input(
                        "Enter user's name: ", valid.validate_name, "Invalid name format."
                    )
                    library_id = self.get_valid_input(
                        "Enter library ID (e.g., AB-12345): ",
                        valid.validate_id,
                        "Invalid library ID format.",
                    )
                    if self.library.find_user(library_id):
                        print("A user with this ID already exists.")
                    else:
                        self.library.add_user(name, library_id)
                        print(f"User '{name}' added successfully.")
                elif choice == 2:
                    library_id = self.get_valid_input(
                        "Enter the library ID of the user: ",
                        valid.validate_id,
                        "Invalid library ID format.",
                    )
                    user = self.library.find_user(library_id)
                    if user:
                        print(user.display_info())
                    else:
                        print("User not found.")
                elif choice == 3:
                    users = self.library.list_users()
                    if users:
                        for user_info in users:
                            print(user_info)
                    else:
                        print("No users in the system.")
                elif choice == 4:
                    break
            except Exception as e:
                print(f"An error occurred: {e}")

    def author_ops_menu(self):
        while True:
            try:
                print("\nAuthor Operations:")
                print("1. Add a new author")
                print("2. View author details")
                print("3. Display all authors")
                print("4. Back to main menu")
                choice = input("Choose an option: ")

                if not choice.isdigit() or int(choice) not in range(1, 5):
                    print("Invalid choice. Please enter a number between 1 and 4.")
                    continue

                choice = int(choice)
                if choice == 1:
                    name = self.get_valid_input(
                        "Enter author's name: ", valid.validate_name, "Invalid name format."
                    )
                    biography = input("Enter biography: ")  
                    if self.library.find_author(name):
                        print("An author with this name already exists.")
                    else:
                        self.library.add_author(name, biography)
                        print(f"Author '{name}' added successfully.")
                elif choice == 2:
                    name = self.get_valid_input(
                        "Enter the author's name: ", valid.validate_name, "Invalid name format."
                    )
                    author = self.library.find_author(name)
                    if author:
                        print(author.display_info())
                    else:
                        print("Author not found.")
                elif choice == 3:
                    authors = self.library.list_authors()
                    if authors:
                        for author_info in authors:
                            print(author_info)
                    else:
                        print("No authors in the system.")
                elif choice == 4:
                    break
            except Exception as e:
                print(f"An error occurred: {e}")

    
