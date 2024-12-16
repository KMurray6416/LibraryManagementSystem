from library import Library
from validation import Validate 

valid = Validate

class UserInterface:
    def __init__(self):
        self.library = Library()

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
                    title = input("Please enter the book title: ")
                    author = input(" Please enter the author: ")
                    genre = input("Enter genre: ")  # Assuming free input for genre
                    pub_date = input("Enter publication date (e.g., YYYY): ")  # Add further validation if needed
                    self.library.add_book(title, author, genre, pub_date)
                elif choice == 2:
                    library_id = input(" Please enter library ID: ")
                    title = input("Please enter the book title: ")
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
                    library_id = input(" Please enter library ID:")
                    title = input("Please enter the book title: ")
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
                    title = input("Please enter the book title: ")
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
                    name = input("Enter your name: ")
                    library_id =input("Enter library ID: ")
                    if self.library.find_user(library_id):
                        print("A user with this ID already exists.")
                    else:
                        self.library.add_user(name, library_id)
                        print(f"User '{name}' added successfully.")
                elif choice == 2:
                    library_id =input("Enter library ID: ")
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
                    name = input("Enter the author's name: ")
                    biography = input("Enter biography: ")  
                    if self.library.find_author(name):
                        print("An author with this name already exists.")
                    else:
                        self.library.add_author(name, biography)
                        print(f"Author '{name}' added successfully.")
                elif choice == 2:
                    name = input("Enter the author's name: ")
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


