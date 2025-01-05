
import datetime
from library_database_connect import Database


class Books:
    def add_book_to_db(title, author, genre, publication_date):    
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
    
                        genre_id = None
    
                   # Check if genre already exists in database  
                        query = "SELECT id FROM genres WHERE name = %s"  
                        
                        cursor.execute(query, (genre,))  
                        genre_data = cursor.fetchone()  
    
                        if genre_data is not None:  
                       # If the genre exists, retrieve its id  
                            genre_id = genre_data[0]  
                        else:  
                           # If the genre doesn't exist, add it to the database  
                           query = "INSERT INTO genres (name) VALUES (%s)"  
                           cursor.execute(query, (genre,))  
                           conn.commit()  
                           genre_id = cursor.lastrowid  
    
    
                   # Insert book into books table  
                        query = "INSERT INTO books (title, author, genre_id, publication_date) VALUES (%s, %s, %s, %s)"  
                        
                        cursor.execute(query, (title, author, genre_id, publication_date))  
                        conn.commit()  
                        print(f"New book: {title} by {author} has been successfully added to the library database")
    
                except Exception as e:
                    print(f"Error: {e}")
    
                finally:
                    cursor.close()
                    conn.close()
    
    def remove_book_from_db():
        conn = Database.connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                title = input("Enter the title of the book to delete: ")
    
                query = "DELETE FROM books WHERE title = %s"
                cursor.execute(query, (title,))
                conn.commit()
                print(f"{title} has successfully been removed from database")
    
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
    
    def lookup_book():
        conn = Database.connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
    
                title = input("Enter the book title: ")
    
                query = "SELECT * FROM books WHERE title = %s" 
    
                cursor.execute(query, (title,)) 
                book = cursor.fetchone()
    
                if book:  
                    print(f"Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, ISBN: {book[4]}, Publication Date: {book[5]}")  
                else:  
                    print("Book not found!")  
    
            except Exception as e:
                print(f"Error: {e}")
            
            finally:
                cursor.close()
                conn.close()
    
    def list_books():  
    
        conn = Database.connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
    
                query = "SELECT * FROM books"  
                cursor.execute(query)  
                books = cursor.fetchall()  
    
                for book in books:  
                   print(f"Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, ISBN: {book[4]}, Publication Date: {book[5]}")  
    
            except Exception as e:
                print(f"Error: {e}")
            
            finally:
                cursor.close()
                conn.close()