import customtkinter as ctk

from View.habitChart import HabitChart

class HabitCharts(ctk.CTkFrame):
    def __init__(self, parent, habits_dict, **kwargs):
        super().__init__(parent, **kwargs)
        self.habit_charts = []
        self.display_habit_charts(habits_dict)

    def display_habit_charts(self, habits_dict):
        for key in habits_dict:
            habit_dict = habits_dict[key]
            habit_dict["habit_id"] = key
            habit_chart = HabitChart(self, habit_dict, fg_color = "transparent")
            habit_chart.pack()
            self.habit_charts.append(habit_chart)

    def save_changes(self, save_func):
        for habit_chart in self.habit_charts:
            habit_chart.save_changes(save_func)