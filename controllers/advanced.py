import requests


class AdvancedController():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["advanced"]
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
        self.view.switch_frame("search")

    def search(self):
        self.params = {}
        self.params["location"] = self.frame.get_location()
        self.search_params()
        self.params["limit"] = 100
        response = requests.get(self.URL, params=self.params)
        self.model.update_response(response.text)
        self.view.get_frame("results").results()
        self.controllers["results"].config_bio()
        self.view.switch_frame("results")

    def search_params(self):
        if self.frame.get_distance():
            self.params["distance"] = self.frame.get_distance()
        if self.frame.get_gender():
            self.params["gender"] = self.frame.get_gender()
        if self.frame.get_type():
            self.params["type"] = self.frame.get_type()
        if self.frame.get_size():
            self.params["size"] = self.frame.get_size()
        if self.frame.get_gwdogs():
            self.params["good_with_dogs"] = self.frame.get_gwdogs()
        if self.frame.get_gwcats():
            self.params["good_with_cats"] = self.frame.get_gwcats()
        if self.frame.get_gwchild():
            self.params["good_with_children"] = self.frame.get_gwchild()
        if self.frame.get_housetrained():
            self.params["house_trained"] = self.frame.get_housetrained()