import customtkinter as ctk

from PIL import Image

from View.habitChart import HabitChart

class HabitCharts(ctk.CTkScrollableFrame):
    def __init__(self, parent, habits_dict, remove_habit_func, **kwargs):
        super().__init__(parent, **kwargs)
        self.habit_charts = []
        self.display_habit_charts(habits_dict)
        self.remove_habit_func = remove_habit_func

    def display_habit_charts(self, habits_dict):
        for key in habits_dict:
            habit_dict = habits_dict[key]
            habit_dict["habit_id"] = key
            frame = ctk.CTkFrame(self)
            frame.pack(pady = 10)
            habit_chart = HabitChart(frame, habit_dict, fg_color = "transparent")
            habit_chart.pack(side = "left")

            img = Image.open("./Images/delete.png")
            delete_button = ctk.CTkButton(
                frame, 
                text="", 
                image=ctk.CTkImage(light_image=img, dark_image=img, size = (32, 32)), 
                width = 0, 
                height = 0,
                fg_color = "transparent",
                hover=False
            )
            delete_button.configure(command=lambda hc=habit_chart, hd=habit_dict, f=frame, db=delete_button: self.remove(hc, hd, db, f))
            delete_button.pack(expand = True, padx = 10, pady = (20,0))

            self.habit_charts.append(habit_chart)

    def remove(self, habit_chart, habit_dict, delete_button, frame):
        habit_chart.pack_forget()
        delete_button.pack_forget()
        frame.pack_forget()
        self.habit_charts.remove(habit_chart)
        self.remove_habit_func(habit_dict)

    def save_changes(self, save_func):
        for habit_chart in self.habit_charts:
            habit_chart.save_changes(save_func)