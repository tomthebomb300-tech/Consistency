from View.window import Window
from Model.database import Sqlite_DB

class Controller:
    def __init__(self):
        self.db = Sqlite_DB()
        self.window = Window("Consistency", 1080, 720, self)
        self.display_main_page()
        self.window.run()        

    def close_application(self):
        self.window.close()
        self.window.destroy()

    def display_main_page(self):
        self.window.display_main_page()

    def add_habit(self, habit_dict):
        self.db.add_habit(habit_dict)
        self.window.update_app()

    def get_habits_dict(self):
        return self.db.get_habits_dict()

    def remove_habit(self, habit):
        self.db.remove_habit(habit["habit_id"])

    def save_changes(self, habit, habit_changed, dates_changed):
        if(habit_changed):
            self.db.update_habit(habit)

        if(dates_changed):
            self.db.remove_dates(habit["habit_id"])
            self.db.add_dates(habit["habit_id"], habit["dates_incomplete"])