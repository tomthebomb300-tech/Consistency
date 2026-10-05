from View.window import Window
from Model.database import Sqlite_DB

class Controller:
    def __init__(self):
        self.window = Window("Consistency", 1080, 720, self)
        self.db = Sqlite_DB()

        self.display_main_page()
        self.window.run()

    def display_main_page(self):
        self.window.display_main_page()

    def add_habit(self, habit_dict):
        self.db.add_habit(habit_dict)