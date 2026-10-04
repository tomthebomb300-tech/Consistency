import customtkinter as ctk
import tkinter as tk

from datetime import datetime


class HabitChart(ctk.CTkFrame):

    def __init__(self, parent, habit, **kwargs):
        super().__init__(parent, **kwargs)

        habit = {
            "title" : "Drink Water",
            "description" : "3L of water",
            "rules" : "",
            "start_date" : datetime.now(),
            "dates_incomplete" : None
        }

        self.create_heading(self, habit)
        self.create_graphic(self, habit)

    def create_heading(self, parent, habit):
        header = ctk.CTkFrame(parent)
        header.pack(fill = "x", padx = (22,0))

        title = ctk.CTkLabel(header,text=habit["title"],font=("Arial", 20),text_color="white")
        title.pack(side = "left")

        description = ctk.CTkLabel(header,text="   -   {0}".format(habit["description"]),font=("Arial", 16),text_color="white")
        description.pack(side = "left")

        percentage = ctk.CTkLabel(header,text="{0}%".format(89),font=("Arial", 16),text_color="white")
        percentage.pack(anchor = "e", padx = (20,0))
        

    def create_graphic(self, parent, habit):
        graphic_frame = ctk.CTkFrame(parent, fg_color="transparent")
        graphic_frame.pack()

        labels = ctk.CTkFrame(graphic_frame)
        labels.pack(side = "left", fill = "y")

        ctk.CTkLabel(labels,text="Mon",font=("Arial", 10),text_color="#aa9a9a", anchor = "n").pack(pady = (3,0))
        ctk.CTkLabel(labels,text="Thu",font=("Arial", 10),text_color="#aa9a9a").pack(pady = (10,0))
        ctk.CTkLabel(labels,text="Sun",font=("Arial", 10),text_color="#aa9a9a", anchor = "s").pack(pady = (10,0))
      

        
        rows = 7
        cols = 30
        max_cols = 40
        square_length = 10
        padding = 5

        canvas_width = max_cols * (padding + square_length) + padding
        canvas_height = rows * (padding + square_length) + padding

        canvas = tk.Canvas(graphic_frame, width = canvas_width, height = canvas_height, bg = "#000000", highlightthickness = 0)
        canvas.pack()

        for ri in range(rows):
            for ci in range(cols):
                x1 = padding + ci * (square_length + padding)
                y1 = padding + ri * (square_length + padding)

                x2 = x1 + square_length
                y2 = y1 + square_length

                canvas.create_rectangle(x1, y1, x2, y2, fill = "#12af0d", outline = "#000000", width = 1, tags = f"rect_{ri}_{ci}")