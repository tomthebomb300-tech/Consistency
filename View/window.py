import customtkinter as ctk

from View.mainPage import MainPage

class Window(ctk.CTk):
    def __init__(self, name, height, width, controller):
        super().__init__()
        self.controller = controller

        self.title(name)
        self.geometry("{0}x{1}".format(width, height))
        self.protocol("WM_DELETE_WINDOW", self.controller.close_application)

        self.main_page = MainPage(self, self.controller)

    def display_main_page(self):
        self.main_page.pack(fill = "both", expand = True)

    def update_app(self):
        self.main_page.update_page()

    def close(self):
        self.main_page.close()

    def run(self):
        self.mainloop()