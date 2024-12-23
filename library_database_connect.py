import mysql.connector
import datetime
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection - None

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
    
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS library_management_system")
            cursor.execute("USE library_management_system")
    
    
            print("Connected to MySQL database successfully")
            return conn
        
        except Error as e:
            print(f"Error: {e}")
            return None
        
    def create_tables():
        conn = Database.connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()

                genres_query = '''CREATE TABLE IF NOT EXISTS genres (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
                );'''

                cursor.execute(genres_query)

                books_query = '''CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author_id INT,
                isbn VARCHAR(13) NOT NULL,
                publication_date DATE,
                genre_id INT,
                availability BOOLEAN DEFAULT 1,
                FOREIGN KEY (author_id) REFERENCES authors(id),
                FOREIGN KEY (genre_id) REFERENCES genres(id)
                );''' 

                cursor.execute(books_query)

                book_copies_query = '''CREATE TABLE IF NOT EXISTS book_copies (
                id INT AUTO_INCREMENT PRIMARY KEY,
                book_id INT,
                copy_number INT,
                FOREIGN KEY (book_id) REFERENCES books(id)
                );'''

                cursor.execute(book_copies_query)

                authors_query = '''CREATE TABLE IF NOT EXISTS authors (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL UNIQUE,
                biography TEXT
                );'''

                cursor.execute(authors_query)

                users_query = '''CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                library_id VARCHAR(10) NOT NULL UNIQUE
                );'''

                cursor.execute(users_query)

                borrowed_books_query =  '''CREATE TABLE IF NOT EXISTS borrowed_books (
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

def add_book_to_db(title, author, isbn, genre, publication_date):    
    conn = Database.connect_database()
    if conn is not None:  
        with conn.cursor() as cursor:  
            try:  
               # Check if author already exists in database  
               query = "SELECT id FROM authors WHERE name = %s"  
               
               cursor.execute(query, (author,))  
               author_id = cursor.fetchone()  

               if author_id is None:  
                  # Author does not exist, insert into authors table  
                    query = "INSERT INTO authors (name) VALUES (%s)"  
                    
                    cursor.execute(query, (author,))  
                    author_id = cursor.lastrowid  
               else:  
                  # Author already exists, use existing ID  
                    author_id = author_id[0]  

               # Check if genre already exists in database  
                    query = "SELECT id FROM genres WHERE name = %s"  
                    
                    cursor.execute(query, (genre,))  
                    genre_id = cursor.fetchone()  

               if genre_id is None:  
                  # Genre does not exist, insert into genres table  
                    query = "INSERT INTO genres (name) VALUES (%s)"  
                    cursor.execute(query, (genre,))  
                    genre_id = cursor.lastrowid  
               else:  
                  # Genre already exists, use existing ID  
                    genre_id = genre_id[0]  

               # Insert book into books table  
                    query = '''INSERT INTO books (title, author_id, isbn, genre_id, publication_date) VALUES (%s, %s, %s, %s, %s)'''  
                    
                    cursor.execute(query, (title, author_id, isbn, genre_id, publication_date))  
                    conn.commit()  
                    print(f"New book: {title} by {author} has been successfully added to the library database")

            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close()

def borrow_book(user_id, book_title):
    conn = Database.connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            # Find the book id by using the book title
            query = "SELECT id FROM books WHERE title = %s"  
            
            cursor.execute(query, (book_title,))  
            book_id = cursor.fetchone()  
            
            if book_id is None:  
                print("Book not found.")  
                return False  
            
            book_id = book_id[0]  
            # Check if the book is available  
            query = "SELECT availability FROM books WHERE id = %s"  
            
            cursor.execute(query, (book_id,))  
            availability = cursor.fetchone()[0]  
            
            if availability == 0:  
               print("Book is not available")  
               return False
            
            # Check if the user has already borrowed the book  
            query = "SELECT * FROM borrowed_books WHERE user_id = %s AND book_id = %s"  
            
            cursor.execute(query, (user_id, book_id))  
            
            if cursor.fetchone():  
                print("User has already borrowed this book")  
                return 
            # Insert a new borrowed book record  
            query = "INSERT INTO borrowed_books (user_id, book_id , borrow_date) VALUES (%s, %s, %s)"  
            
            borrow_date = datetime.date.today()  
            cursor.execute(query, (user_id, book_id, borrow_date)) 
            
            # Update the book's availability  
            query = "UPDATE books SET availability = 0 WHERE id = %s"  
            
            cursor.execute(query, (book_id,))  
            conn.commit()    
            print("Book borrowed successfully")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def return_borrowed_book(user_id, book_title):
    conn = Database.connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Find the book ID using the book title  
            query = "SELECT id FROM books WHERE title = %s"  
            
            cursor.execute(query, (book_title,))  
            book_id = cursor.fetchone()  
            
            if book_id is None:  
              print("Book not found.")  
              return False  
            
            book_id = book_id[0]  

            # Check if the book is borrowed by the user  
            query = "SELECT * FROM borrowed_books WHERE user_id = %s AND book_id = %s"  
            
            cursor.execute(query, (user_id, book_id))  
            borrowed_book = cursor.fetchone()  
            
            if borrowed_book is None:  
                print("Book is not borrowed by the user.")  
                return False  
            
            # Update the book's availability  
            query = "UPDATE books SET availability = 1 WHERE id = %s"  
            
            cursor.execute(query, (book_id,))  
            conn.commit()  

            # Update the user's borrowed books record  
            return_date = datetime.date.today()  
            query = "UPDATE borrowed_books SET return_date = %s, status = 'Returned' WHERE user_id = %s AND book_id = %s"  
            cursor.execute(query, (return_date, user_id, book_id))  
            conn.commit()  

            print("Book returned successfully!")  
            return True  

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

