from View.window import Window
from Model.database import Sqlite_DB

class Controller:
    def __init__(self):
        self.db = Sqlite_DB()
        self.window = Window("Consistency", 1080, 720, self)
        self.display_main_page()
        self.window.run()        

    def close_application(self):
        print("Ending")
        self.window.destroy()

    def display_main_page(self):
        self.window.display_main_page()

    def add_habit(self, habit_dict):
        self.db.add_habit(habit_dict)

    def get_habits_dict(self):
        return self.db.get_habits_dict()