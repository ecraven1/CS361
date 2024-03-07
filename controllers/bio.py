import webbrowser


class BioController():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["bio"]
        self.config_com()

    def set_controllers(self, controllers):
        self.controllers = controllers

    def config_com(self):
        self.frame.back_button.config(command=self.back)
        self.frame.adopt_button.config(command=self.adopt)

    def back(self):
        self.view.get_frame("bio").remove()
        self.view.switch_frame("results")

    def adopt(self):
        pet_url = self.view.get_frame("bio").get_animal()["url"]
        webbrowser.open_new(pet_url)