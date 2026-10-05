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
            CREATE TABLE IF NOT EXISTS CompleteDates (
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