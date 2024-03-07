class HomeController():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self.config_com()

    def set_controllers(self, controllers):
        self.controllers = controllers

    def config_com(self):
        self.frame.search_button.config(command=self.search)

    def search(self):
        self.view.switch_frame("search")

