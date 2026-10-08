import customtkinter as ctk

from View.habitCharts import HabitCharts
from View.addHabit import AddHabit

from PIL import Image

class MainPage(ctk.CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.controller = controller

        img = Image.open("./Images/add.png")
        add_habit_button = ctk.CTkButton(
            self, 
            text="", 
            image=ctk.CTkImage(light_image=img, dark_image=img, size = (48,48)), 
            command=self.open_add_habit, 
            width = 0, 
            height = 0,
            fg_color = "transparent",
            hover=False
        )
        add_habit_button.pack(anchor = "e", padx = (0,40), pady = (10,10))

        self.create_habit_charts()


    def create_habit_charts(self):
        self.habit_charts = HabitCharts(self, self.controller.get_habits_dict(), self.controller.remove_habit, fg_color = "transparent")
        self.habit_charts.pack(fill = "both", expand = True)

    def update_page(self):
        self.habit_charts.pack_forget()
        self.create_habit_charts()

    def open_add_habit(self):
        add_habit = AddHabit(self, self.controller.add_habit)

    def close(self):
        self.habit_charts.save_changes(self.controller.save_changes)