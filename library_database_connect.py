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

                query = '''
                CREATE TABLE IF NOT EXISTS genres (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
                );
                '''

                cursor.execute(query)

                query = """  
                CREATE TABLE IF NOT EXISTS authors (  
                id INT AUTO_INCREMENT PRIMARY KEY,  
                name VARCHAR(255) NOT NULL,  
                email VARCHAR(255)  
                );  
                """  
               
                cursor.execute(query)

                query = """ALTER TABLE authors MODIFY email VARCHAR(255) NULL;"""
                
                cursor.execute(query)

                query = '''
                CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author_id INT,
                publication_date DATE,
                genre_id INT,
                availability BOOLEAN DEFAULT 1,
                FOREIGN KEY (author_id) REFERENCES authors(id),
                FOREIGN KEY (genre_id) REFERENCES genres(id)
                );''' 

                cursor.execute(query)

                query = '''
                CREATE TABLE IF NOT EXISTS book_copies (
                id INT AUTO_INCREMENT PRIMARY KEY,
                book_id INT,
                copy_number INT,
                FOREIGN KEY (book_id) REFERENCES books(id)
                );'''

                cursor.execute(query)

                query = '''
                CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                library_id VARCHAR(10) NOT NULL UNIQUE
                );'''

                cursor.execute(query)

                query =  '''
                CREATE TABLE IF NOT EXISTS borrowed_books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                book_id INT,
                borrow_date DATE NOT NULL,
                return_date DATE,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (book_id) REFERENCES books(id)
                );'''

                cursor.execute(query)
                conn.commit()
                print("Tables successfully created for database")

            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close()
