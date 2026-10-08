import pandas as pd
import sqlite3

class Sqlite_DB:
    def __init__(self):
        self.db_name = "./Model/consistency.db"
        self.conn = sqlite3.connect(self.db_name)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Habits (
                habit_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                start_date TEXT NOT NULL,
                complete_colour TEXT NOT NULL,
                incomplete_colour TEXT NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS IncompleteDates (
                date_id INTEGER PRIMARY KEY AUTOINCREMENT,
                habit_id INTEGER NOT NULL,
                date TEXT NOT NULL,                

                FOREIGN KEY (habit_id)
                    REFERENCES Habits(habit_id)
            );
        """)


        self.conn.commit()
        print("Database and table created successfully")

    def add_habit(self, habit_dict):
        self.cursor.execute("""
            INSERT INTO Habits (title, description, start_date, complete_colour, incomplete_colour)
            VALUES (?, ?, ?, ?, ?)
        """, (habit_dict["title"], habit_dict["description"], habit_dict["start_date"], habit_dict["complete_colour"], habit_dict["incomplete_colour"]))
        self.conn.commit()

    def add_habit_return_habit_id(self, habit_dict):
        self.add_habit(habit_dict)
        return self.cursor.lastrowid

    def update_habit(self, habit):
        query = """UPDATE Habits SET title = ?, description = ?, start_date = ?, complete_colour = ?, incomplete_colour = ? WHERE habit_id = ?;"""
        self.cursor.execute(query, (habit["title"], habit["description"], habit["start_date"], habit["complete_colour"], habit["incomplete_colour"], habit["habit_id"]))
        self.conn.commit()

    def remove_dates(self, habit_id):
        self.cursor.execute("""DELETE FROM IncompleteDates WHERE habit_id = ?;""", (habit_id,))
        self.conn.commit()

    def remove_habit(self, habit_id):
        self.remove_dates(habit_id)
        self.cursor.execute("""DELETE FROM Habits WHERE habit_id = ?;""", (habit_id,))
        self.conn.commit()


    def add_dates(self, habit_id, dates):
        if(len(dates) == 0):
            return

        for date in dates:
            self.cursor.execute("""INSERT INTO IncompleteDates (habit_id, date) VALUES (?, ?)""", (habit_id, date))
        self.conn.commit()
        

        

    def get_habits_dict(self):
        query = """SELECT * FROM Habits"""
        habits_df = pd.read_sql_query(query, self.conn)
        habits_df["start_date"] = pd.to_datetime(habits_df["start_date"]).dt.date
        habits_dict = habits_df.set_index("habit_id").to_dict("index")
        
        query = """SELECT * FROM IncompleteDates"""
        dates_df = pd.read_sql_query(query, self.conn)
        dates_df["date"] = pd.to_datetime(dates_df["date"]).dt.date

        for habit_id in habits_dict:
            completed_dates_df = dates_df[dates_df["habit_id"] == habit_id]
            habits_dict[habit_id]["dates_incomplete"] = completed_dates_df["date"].to_list()
        
        return habits_dict
