

from library_database_connect import Database


def db_add_user(name, library_id):
    conn = Database.connect_database()
    if conn is not None:  
        with conn.cursor() as cursor:  
            try:  

                query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"  
                
                cursor.execute(query, (name, library_id))  

                conn.commit()  
                print("User added successfully!")

            except Exception as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()

def view_user_details(library_id):
    conn = Database.connect_database()
    if conn is not None:  
        with conn.cursor() as cursor:  
            try:  

                query = "SELECT * FROM users WHERE library_id = %s"  
                
                cursor.execute(query, (library_id,))  

                user = cursor.fetchone()

                if user:  
                    print(f"Name: {user[1]}, Library ID: {user[2]}")  
                else:  
                    print("User not found!")  

            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close() 

def display_users():
    conn = Database.connect_database()
    if conn is not None:  
        with conn.cursor() as cursor:  
            try:  
    
                query = "SELECT * FROM users"  
                cursor.execute(query)  
                users = cursor.fetchall()  

                for user in users:  
                   print(f"Name: {user[1]}, Library ID: {user[2]}")  

            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close() 