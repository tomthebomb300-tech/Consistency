import customtkinter as ctk

from PIL import Image
from ctkdateentry import CTkDateEntry

class AddHabit(ctk.CTkToplevel):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent)
        self.controller = controller
    
        self.title_entry = None
        self.date_entry = None
        self.description_entry = None
        self.rules_entry = None
        self.complete_colour_entry = None
        self.incomplete_color_entry = None

        self.title("Add Habit")
        self.geometry("400x400")

        self.transient(parent)
        self.grab_set()

        self.create_title_date_entry()
        self.create_description_entry()
        self.create_rules_entry()
        self.create_colours_entry()

    def create_title_date_entry(self):
        frame = ctk.CTkFrame(self,fg_color="transparent")
        frame.pack(padx = 50, pady = 25, fill = "x")

        title_frame = ctk.CTkFrame(frame,fg_color="#1D1D1D")
        title_frame.pack(side = "left")
        img = Image.open("./Images/title.png")
        image = ctk.CTkLabel(title_frame, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size=(20,20)))
        image.pack(side = "left")
        self.title_entry = ctk.CTkEntry(title_frame,width=120,placeholder_text="Title", fg_color = "transparent", border_width=0)
        self.title_entry.pack(side = "left")

        self.date_entry = CTkDateEntry(frame)
        self.date_entry.pack()

    def create_description_entry(self):
        frame = ctk.CTkFrame(self,fg_color="#1D1D1D")
        frame.pack(padx = 50, pady = 25, fill = "x")
        img = Image.open("./Images/description.png")
        image = ctk.CTkLabel(frame, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size=(20,20)))
        image.pack(side = "left")
        self.description_entry = ctk.CTkEntry(frame,width=300,placeholder_text="Description", fg_color = "transparent", border_width=0)
        self.description_entry.pack(side = "left")

    def create_rules_entry(self):
        frame = ctk.CTkFrame(self,fg_color="#1D1D1D")
        frame.pack(padx = 50, pady = 25, fill = "x")
        img = Image.open("./Images/rules.png")
        image = ctk.CTkLabel(frame, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size=(20,20)))
        image.pack(side = "left", anchor = "n")
        image = ctk.CTkLabel(frame, text = "Rules")
        image.pack(side = "left", anchor = "n", padx = (10,0))
        self.rules_entry = ctk.CTkEntry(frame,width=300, height=100,placeholder_text="", fg_color = "transparent", border_width=0)
        self.rules_entry.pack(anchor = "w")

    def create_colours_entry(self):
        frame = ctk.CTkFrame(self,fg_color="transparent")
        frame.pack(padx = 50, pady = 25, fill = "x")

        complete_frame = ctk.CTkFrame(frame,fg_color="#1D1D1D")
        complete_frame.pack(side = "left")
        img = Image.open("./Images/tick.png")
        image = ctk.CTkLabel(complete_frame, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size=(20,20)))
        image.pack(side = "left")
        self.complete_colour_entry = ctk.CTkEntry(complete_frame,width=120,placeholder_text="Complete Hex", fg_color = "transparent", border_width=0)
        self.complete_colour_entry.pack(side = "left")

        incomplete_frame = ctk.CTkFrame(frame,fg_color="#1D1D1D")
        incomplete_frame.pack()
        img = Image.open("./Images/x.png")
        image = ctk.CTkLabel(incomplete_frame, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size=(20,20)))
        image.pack(side = "left")
        self.incomplete_color_entry = ctk.CTkEntry(incomplete_frame,width=120,placeholder_text="In-Complete Hex", fg_color = "transparent", border_width=0)
        self.incomplete_color_entry.pack(side = "left")