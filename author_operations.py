from validation import Validate

class Author:
    def __init__(self, name, biography):
        self.validator = Validate()  # Create an instance of the validation class
        self.__name = self.validator.validate_name(name)
        self.__biography = biography

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        try:
            self.__name = self.validator.validate_name(name)
        except ValueError as e:
            print(f"Error setting name: {e}")

    # Getter for biography
    def get_biography(self):
        return self.__biography

    # Setter for biography
    def set_biography(self, biography):
        self.__biography = biography

    def display_info(self):
        return f"Name: {self.__name}, Biography: {self.__biography}"
