
from book_operations import Book
from user_operations import User
from author_operations import Author

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.authors = {}

    def add_book(self, title, author, genre, publication_date):
        new_book = Book(title, author, genre, publication_date)
        self.books[title] = new_book
        if author in self.authors:
            self.authors[author].add_book(title)
        return new_book

    def add_user(self, name, library_id):
        new_user = User(name, library_id)
        self.users[library_id] = new_user
        return new_user

    def add_author(self, name, biography):
        author = Author(name, biography)
        self.authors[name] = author
        return author

    def find_book(self, title):
        return self.books.get(title) #---\
                                     #    \
    def find_user(self, library_id): #     \___Getters
        return self.users.get(library_id)# /
                                     #    /
    def find_author(self, name):     #   /
        return self.authors.get(name)#__/

    def list_books(self):
        return [book.display_info() for book in self.books.values()] #-------\
                                                                     #        \
    def list_users(self):                                            #         \___Setters
        return [user.display_info() for user in self.users.values()] #         /
                                                                     #        /
    def list_authors(self):                                          #       /
        return [author.display_info() for author in self.authors.values()]#_/
