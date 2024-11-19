from validation import Validate

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.validator = Validate()  # Initialize an instance of Validate
        self.__title = None
        self.__author = None
        self.__genre = None
        self.__publication_date = None
        self.__is_available = True  # Default availability status
        
        self.set_title(title)  # Use setters to validate during initialization
        self.set_author(author)
        self.set_genre(genre)
        self.set_publication_date(publication_date)

    # Getter for title
    def get_title(self):
        return self.__title

    # Setter for title
    def set_title(self, title):
        try:
            validated_title = self.validator.validate_title(title)
            if validated_title:
                self.__title = title
        except ValueError as e:
            print(f"Error: {e}")

    # Getter for author
    def get_author(self):
        return self.__author

    # Setter for author
    def set_author(self, author):
        try:
            validated_author = self.validator.validate_name(author)
            if validated_author:
                self.__author = author
        except ValueError as e:
            print(f"Error: {e}")

    # Getter for genre
    def get_genre(self):
        return self.__genre

    # Setter for genre
    def set_genre(self, genre):
        try:
            validated_genre = self.validator.validate_name(genre)
            if validated_genre:
                self.__genre = genre
        except ValueError as e:
            print(f"Error: {e}")

    # Getter for publication date
    def get_publication_date(self):
        return self.__publication_date

    # Setter for publication date
    def set_publication_date(self, publication_date):
        try:
            validated_date = self.validator.validate_date(publication_date)
            if validated_date:
                self.__publication_date = publication_date
        except ValueError as e:
            print(f"Error: {e}")

    # Getter for availability
    def get_availability(self):
        return self.__is_available

    # Setter for availability
    def set_availability(self, availability_status):
        self.__is_available = availability_status

    def display_info(self):
        availability = "Yes" if self.__is_available else "No"
        return (f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, "
                f"Publication Date: {self.__publication_date}, Available: {availability}")
