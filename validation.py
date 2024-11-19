import re

class Validate:
    def __init__(self):
        pass

    def validate_name(self, name):
        if not re.match(r"^[A-Za-z\s]+$", name):
            raise ValueError("Invalid input. Only letters and spaces are allowed.")
        return name

    def validate_id(self, library_id):
        if not re.match(r"^[A-Za-z]{2}-\d{5}$", library_id):
            raise ValueError("Invalid ID input. ID must be formatted as Ab-12345.")
        return library_id

    def validate_title(self, title):
        if not re.match(r"^[A-Za-z0-9\s\-,.']+$", title):
            raise ValueError("Invalid title. Only letters, numbers, spaces, and punctuation are allowed.")
        return title

    def validate_date(self, date):
        if not re.match(r"^\d{2}-\d{2}-\d{4}$", date):
            raise ValueError("Invalid date. Use the format MM-DD-YYYY.")
        return date
