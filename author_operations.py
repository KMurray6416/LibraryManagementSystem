
class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for biography
    def get_biography(self):
        return self.__biography

    # Setter for biography
    def set_biography(self, biography):
        self.__biography = biography

    def display_info(self):
        return f"Name: {self.__name}, Biography: {self.__biography}"
