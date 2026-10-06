import customtkinter as ctk

from View.habitChart import HabitChart
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
        self.load_habit_charts()


    def load_habit_charts(self):
        habits_dict = self.controller.get_habits_dict()
        for key in habits_dict:
            habit_dict = habits_dict[key]
            habit_dict["habit_id"] = key
            habit_chart = HabitChart(self, habit_dict, fg_color = "transparent")
            habit_chart.pack()


    def open_add_habit(self):
        add_habit = AddHabit(self, self.controller)