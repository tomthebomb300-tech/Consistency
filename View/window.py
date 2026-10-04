import customtkinter as ctk

class Window(ctk.CTk):
    def __init__(self, name, height, width, controller):
        super().__init__()
        self.controller = controller

        self.title(name)
        self.geometry("{0}x{1}".format(width, height))

    def run(self):
        self.mainloop()