import mysql.connector
from mysql.connector import Error

def connect_database():
    """Connect to the MySQL database and return the connection object"""

    db_name ="library_management_system"
    user = "root"
    password = "Yourmom21892!"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        print("Connected to MySQL database successfully")
        return conn
    
    except Error as e:
        print(f"Error: {e}")
        return None
    
def create_tables():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            books_query = '''CREATE TABLE books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author_id INT,
            isbn VARCHAR(13) NOT NULL,
            publication_date DATE,
            availability BOOLEAN DEFAULT 1,
            FOREIGN KEY (author_id) REFERENCES authors(id),
            );'''
            cursor.execute(books_query)
            authors_query = '''CREATE TABLE authors (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            biography TEXT
            );'''
            cursor.execute(authors_query)
            users_query = '''CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            library_id VARCHAR(10) NOT NULL UNIQUE
            );'''
            cursor.execute(users_query)
            borrowed_books_query =  '''CREATE TABLE borrowed_books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            book_id INT,
            borrow_date DATE NOT NULL,
            return_date DATE,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (book_id) REFERENCES books(id)
            );'''
            cursor.execute(borrowed_books_query)
            conn.commit()
            print("Tables successfully created for database")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()