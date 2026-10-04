from View.window import Window

class Controller:
    def __init__(self):
        self.window = Window("Consistency", 1080, 720, self)
        self.display_main_page()
        self.window.run()

    def display_main_page(self):
        self.window.display_main_page()