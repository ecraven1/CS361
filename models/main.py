import json


class Model:
    def __init__(self):
        self.handlers = {}
        self.response = ""
        self.count = 0
        self.pets = []

    def add_handler(self, handler, call):
        try:
            self.handlers[handler].append(call)
        except KeyError:
            self.handlers[handler] = [call]

        return lambda: self.handlers[handler].remove(call)

    def click(self, handler):
        if handler not in self.handlers.keys():
            return

        for call in self.handlers[handler]:
            func(self)

    def update_response(self, response):
        self.response = response

    def get_response(self):
        return json.loads(self.response)

    def populate(self):
        for i in range(5):
            while not self.get_response()["animals"][self.count]["photos"]:
                self.count += 1
            self.pets.append(self.get_response()["animals"][self.count])
            self.count += 1
        self.count = 0

    def fetch(self, num):
        return self.pets[num]

    def get_animal(self, count):
        return self.get_response()["animals"][count]

    def reset(self):
        self.count = 0
        self.pets = []