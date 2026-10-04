import customtkinter as ctk

from View.habitChart import HabitChart

class MainPage(ctk.CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.controller = controller

        habit_chart = HabitChart(self, None, fg_color = "transparent")
        habit_chart.pack()