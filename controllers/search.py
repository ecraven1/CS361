import requests


class SearchController():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["search"]
        self.config_com()
        self.URL = 'http://127.0.0.1:5000/pets'

    def set_controllers(self, controllers):
        self.controllers = controllers

    def config_com(self):
        self.frame.back_button.config(command=self.back)
        self.frame.advanced_button.config(command=self.advanced)
        self.frame.search_button.config(command=self.search)

    def back(self):
        self.view.switch_frame("home")

    def advanced(self):
        self.view.switch_frame("advanced")

    def search(self):
        location = self.frame.get_location()
        limit = 100
        params = {"location": location, "limit": limit}
        response = requests.get(self.URL, params=params)
        self.model.update_response(response.text)
        self.view.get_frame("results").results()
        self.controllers["results"].config_bio()
        self.view.switch_frame("results")