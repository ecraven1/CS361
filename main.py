from models.main import Model
from controllers.main import Controller
from views.main import View


def main():
    model = Model()
    view = View(model)
    controller = Controller(model, view)
    controller.begin()


if __name__ == "__main__":
    main()