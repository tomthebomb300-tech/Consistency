from View.window import Window

class Controller:
    def __init__(self):
        self.window = Window("Consistency", 1080, 1920, self)
        self.window.run()