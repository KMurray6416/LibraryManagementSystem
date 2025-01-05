
from library_database_connect import Database

def db_add_author(name, email):
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