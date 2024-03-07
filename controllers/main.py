from .home import HomeController
from .search import SearchController
from .advanced import AdvancedController
from .results import ResultsController
from .bio import BioController


class Controller:
    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.controllers = {}
        self.add_controller("home", HomeController)
        self.add_controller("search", SearchController)
        self.add_controller("advanced", AdvancedController)
        self.add_controller("results", ResultsController)
        self.add_controller("bio", BioController)
        self.pass_controllers()

    def begin(self):
        self.view.switch_frame("home")
        self.view.begin_mainloop()

    def add_controller(self, controller_name, Controller):
        self.controllers[controller_name] = Controller(self.model, self.view)

    def pass_controllers(self):
        for controller_name in self.controllers:
            self.controllers[controller_name].set_controllers(self.controllers)

    def get_controllers(self):
        return self.controllers