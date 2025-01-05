from user_actions import UserInterface
import library_database_connect

ldc = library_database_connect
ldc.Database.connect_database()
ldc.Database.create_tables()



if __name__ == "__main__":
    ui = UserInterface()
    ui.display_main_menu()