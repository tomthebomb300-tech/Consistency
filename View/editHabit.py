import customtkinter as ctk

from PIL import Image
from ctkdateentry import CTkDateEntry, CTkStringVar
import datetime

class EditHabit(ctk.CTkToplevel):
    def __init__(self, parent, habit, save_func, **kwargs):
        super().__init__(parent, **kwargs)
    
        self.title_entry = None
        self.date_var = CTkStringVar(self, value=habit["start_date"].strftime("%d/%m/%Y"))
        self.description_entry = None
        self.complete_colour_entry = None
        self.incomplete_color_entry = None

        self.title("Edit Habit")
        self.geometry("400x400")

        self.transient(parent)
        self.grab_set()

        self.create_title_date_entry(habit["title"])
        self.create_description_entry(habit["description"])
        self.create_colours_entry(habit["complete_colour"], habit["incomplete_colour"])

        img = Image.open("./Images/db.png")
        commit_button = ctk.CTkButton(self, text="Save", image = ctk.CTkImage(light_image=img, dark_image=img, size = (20,20)), fg_color="#000000", text_color="#938B94", hover = "False", command=lambda: self.save(habit, save_func))
        commit_button.pack()

    def save(self, habit, save_func):
        habit["title"] = self.title_entry.get()
        habit["start_date"] = datetime.datetime.strptime(self.date_var.get(), "%d/%m/%Y").date()
        habit["description"] = self.description_entry.get()
        habit["complete_colour"] = self.complete_colour_entry.get()
        habit["incomplete_colour"] = self.incomplete_color_entry.get()
        save_func(habit)


    def create_title_date_entry(self, title):
        frame = ctk.CTkFrame(self,fg_color="transparent")
        frame.pack(padx = 50, pady = 25, fill = "x")

        title_frame = ctk.CTkFrame(frame,fg_color="#1D1D1D")
        title_frame.pack(side = "left")
        img = Image.open("./Images/title.png")
        image = ctk.CTkLabel(title_frame, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size=(20,20)))
        image.pack(side = "left")
        self.title_entry = ctk.CTkEntry(title_frame,width=120, fg_color = "transparent", border_width=0)
        self.title_entry.delete(0, "end")
        self.title_entry.insert(0, title)
        self.title_entry.pack(side = "left")

        CTkDateEntry(frame, variable=self.date_var).pack()

    def create_description_entry(self, description):
        frame = ctk.CTkFrame(self,fg_color="#1D1D1D")
        frame.pack(padx = 50, pady = 25, fill = "x")
        img = Image.open("./Images/description.png")
        image = ctk.CTkLabel(frame, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size=(20,20)))
        image.pack(side = "left")
        self.description_entry = ctk.CTkEntry(frame,width=300, fg_color = "transparent", border_width=0)
        self.description_entry.delete(0, "end")
        self.description_entry.insert(0, description)
        self.description_entry.pack(side = "left")

    def create_colours_entry(self, complete_colour, incomplete_colour):
        frame = ctk.CTkFrame(self,fg_color="transparent")
        frame.pack(padx = 50, pady = 25, fill = "x")

        complete_frame = ctk.CTkFrame(frame,fg_color="#1D1D1D")
        complete_frame.pack(side = "left")
        img = Image.open("./Images/tick.png")
        image = ctk.CTkLabel(complete_frame, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size=(20,20)))
        image.pack(side = "left")
        self.complete_colour_entry = ctk.CTkEntry(complete_frame,width=120, fg_color = "transparent", border_width=0)
        self.complete_colour_entry.delete(0, "end")
        self.complete_colour_entry.insert(0, complete_colour)
        self.complete_colour_entry.pack(side = "left")

        incomplete_frame = ctk.CTkFrame(frame,fg_color="#1D1D1D")
        incomplete_frame.pack()
        img = Image.open("./Images/x.png")
        image = ctk.CTkLabel(incomplete_frame, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size=(20,20)))
        image.pack(side = "left")
        self.incomplete_color_entry = ctk.CTkEntry(incomplete_frame,width=120, fg_color = "transparent", border_width=0)
        self.incomplete_color_entry.delete(0, "end")
        self.incomplete_color_entry.insert(0, incomplete_colour)
        self.incomplete_color_entry.pack(side = "left")