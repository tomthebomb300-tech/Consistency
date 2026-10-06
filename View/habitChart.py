import customtkinter as ctk
import tkinter as tk
import math

import datetime


class HabitChart(ctk.CTkFrame):

    def __init__(self, parent, habit, **kwargs):
        super().__init__(parent, **kwargs)

        print(habit)

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
        max_cols = 40
        square_length = 10
        padding = 5

        canvas_width = max_cols * (padding + square_length) + padding
        canvas_height = rows * (padding + square_length) + padding

        canvas = tk.Canvas(graphic_frame, width = canvas_width, height = canvas_height, bg = "#000000", highlightthickness = 0)
        canvas.pack()

        canvas.bind("<Button-1>", lambda event: self.on_canvas_click(event, square_length, padding, habit, canvas))

        date_index = habit["start_date"]
        ri = habit["start_date"].weekday()
        ci = 0

        while(ci < max_cols):
            if(ci > 0):
                ri = 0
            while(ri < rows):
                x1 = padding + ci * (square_length + padding)
                y1 = padding + ri * (square_length + padding)

                x2 = x1 + square_length
                y2 = y1 + square_length

                colour = habit["incomplete_colour"]
                if(date_index in habit["dates_complete"]):
                    colour = habit["complete_colour"]

                canvas.create_rectangle(x1, y1, x2, y2, fill = colour, outline = "#000000", width = 1, tags = f"rect_{ri}_{ci}")

                date_index = date_index + datetime.timedelta(days=1)
                if(date_index > datetime.datetime.now().date()): 
                    ci = max_cols
                ri+=1
            ci+=1

    def on_canvas_click(self, event, square_length, padding, habit, canvas):
        #map to canvas coords
        dec_ci = round(event.x/(square_length+padding),2)+1
        dec_ri = round(event.y/(square_length+padding),2)+1
        valid_dec_ci_coord = round(dec_ci%math.floor(dec_ci),2) > (padding/(square_length+padding))
        valid_dec_ri_coord = round(dec_ri%math.floor(dec_ri),2) > (padding/(square_length+padding))

        #check valid cell click
        if(valid_dec_ci_coord and valid_dec_ri_coord):
            ci = math.floor(dec_ci)-1
            ri = math.floor(dec_ri)-1

            #get clicked squares date
            date = habit["start_date"] + datetime.timedelta(days=7*ci+ri-habit["start_date"].weekday())
            #check valid if cell active
            if(date >= habit["start_date"] and date <= datetime.datetime.now().date()):
                x1 = padding + ci * (square_length + padding)
                y1 = padding + ri * (square_length + padding)
                x2 = x1 + square_length
                y2 = y1 + square_length
                
                colour = "#000000"
                if(date in habit["dates_complete"]):
                    colour = habit["incomplete_colour"]
                else:
                    colour = habit["complete_colour"]
                canvas.create_rectangle(x1, y1, x2, y2, fill = colour, outline = "#000000", width = 1, tags = f"rect_{ri}_{ci}")
