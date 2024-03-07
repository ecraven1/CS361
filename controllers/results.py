import requests
from functools import partial


class ResultsController():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["results"]
        self.config_com()

    def set_controllers(self, controllers):
        self.controllers = controllers

    def config_com(self):
        self.frame.back_button.config(command=self.back)

    def back(self):
        self.model.reset()
        self.view.get_frame("results").remove()
        self.view.switch_frame("search")

    def bio(self, i):
        self.view.get_frame("bio").bio(i)
        self.view.switch_frame("bio")

    def config_bio(self):
        bio_buttons = self.frame.bio_buttons
        for i in range(5):
            bio_buttons[i].config(command=partial(self.bio, i))
