
class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True  # Private attribute to track availability status

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def get_availability(self):
        return self.__is_available

    def set_availability(self, availability_status):
        self.__is_available = availability_status

    def display_info(self):
        return (f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, "
                f"Publication Date: {self.__publication_date}, Available: {self.__is_available}")
