import customtkinter as ctk
import tkinter as tk
import math
import datetime

from PIL import Image

from View.editHabit import EditHabit

class HabitChart(ctk.CTkFrame):

    def __init__(self, parent, habit, **kwargs):
        super().__init__(parent, **kwargs)

        self.dates_changed = False
        self.habit_changed = False
        self.habit = habit
        self.create_heading(self)
        self.create_graphic(self)
        

    def edit_habit(self):
        self.habit_changed = True
        edit_habit = EditHabit(self, self.habit, self.display_habit)

    def display_habit(self, habit):
        self.habit = habit
        self.header.pack_forget()
        self.graphic_frame.pack_forget()
        self.create_heading(self)
        self.create_graphic(self)

    def create_heading(self, parent):
        self.header = ctk.CTkFrame(parent)
        self.header.pack(fill = "x", padx = (22,0))

        title = ctk.CTkLabel(self.header,text=self.habit["title"],font=("Arial", 20),text_color="white")
        title.pack(side = "left")

        description = ctk.CTkLabel(self.header,text="   -   {0}".format(self.habit["description"]),font=("Arial", 16),text_color="white")
        description.pack(side = "left")

        img = Image.open("./Images/edit.png")
        edit_habit_button = ctk.CTkButton(
            self.header, 
            text="", 
            image=ctk.CTkImage(light_image=img, dark_image=img, size = (16,16)), 
            command=self.edit_habit, 
            width = 0, 
            height = 0,
            fg_color = "transparent",
            hover=False
        )
        edit_habit_button.pack(side = "left", padx = (20,0))

        num_days = (datetime.datetime.now().date()-self.habit["start_date"]).days
        if(num_days < 0):
            num_days = 0

        num_days_label = ctk.CTkLabel(self.header,text="{0} days".format(num_days),font=("Arial", 16),text_color="white")
        num_days_label.pack(side = "right", padx = (20,0))

        percentage = 0
        if(num_days > 0):
            percentage = round((num_days-len(self.habit["dates_incomplete"]))/num_days,4)*100
        self.percentage_label = ctk.CTkLabel(self.header,text="{0}%".format(percentage),font=("Arial", 16),text_color="white")
        self.percentage_label.pack(anchor = "e")
        

    def create_graphic(self, parent):
        self.graphic_frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.graphic_frame.pack()

        labels = ctk.CTkFrame(self.graphic_frame)
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

        canvas = tk.Canvas(self.graphic_frame, width = canvas_width, height = canvas_height, bg = "#000000", highlightthickness = 0)
        canvas.pack()

        if(self.habit["start_date"] > datetime.datetime.now().date()):
            return

        canvas.bind("<Button-1>", lambda event: self.on_canvas_click(event, square_length, padding, canvas))

        date_index = self.habit["start_date"]
        ri = self.habit["start_date"].weekday()
        ci = 0

        while(ci < max_cols):
            if(ci > 0):
                ri = 0
            while(ri < rows):
                x1 = padding + ci * (square_length + padding)
                y1 = padding + ri * (square_length + padding)

                x2 = x1 + square_length
                y2 = y1 + square_length

                colour = self.habit["complete_colour"]
                if(date_index in self.habit["dates_incomplete"]):
                    colour = self.habit["incomplete_colour"]

                canvas.create_rectangle(x1, y1, x2, y2, fill = colour, outline = "#000000", width = 1, tags = f"rect_{ri}_{ci}")

                date_index = date_index + datetime.timedelta(days=1)
                if(date_index > datetime.datetime.now().date()): 
                    ci = max_cols
                ri+=1
            ci+=1

    def on_canvas_click(self, event, square_length, padding, canvas):
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
            date = self.habit["start_date"] + datetime.timedelta(days=7*ci+ri-self.habit["start_date"].weekday())
            #check valid if cell active
            if(date >= self.habit["start_date"] and date <= datetime.datetime.now().date()):
                self.dates_changed = True
                x1 = padding + ci * (square_length + padding)
                y1 = padding + ri * (square_length + padding)
                x2 = x1 + square_length
                y2 = y1 + square_length

                colour = "#000000"
                if(date in self.habit["dates_incomplete"]):
                    self.habit["dates_incomplete"].remove(date)
                    colour = self.habit["complete_colour"]
                else:
                    self.habit["dates_incomplete"].append(date)
                    colour = self.habit["incomplete_colour"]
                    
                num_days = (datetime.datetime.now().date()-self.habit["start_date"]).days
                if(num_days > 0):
                    self.percentage_label.configure(text="{0}%".format(round((num_days-len(self.habit["dates_incomplete"]))/num_days,4)*100))
                else:
                    self.percentage_label.configure(text = "0%")
                canvas.create_rectangle(x1, y1, x2, y2, fill = colour, outline = "#000000", width = 1, tags = f"rect_{ri}_{ci}")

    def save_changes(self, save_func):
        save_func(self.habit, self.habit_changed, self.dates_changed)