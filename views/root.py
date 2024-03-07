from tkinter import *
import ttkbootstrap as tb


class Root(tb.Window):
    def __init__(self, model):
        super().__init__()
        self.style.theme_use("morph")
        self.title("Pet Finder")
        self.geometry("700x1000")
        pet_icon = PhotoImage(file='images/pet_ico.png')
        self.tk.call('wm', 'iconphoto', Root._w, pet_icon)
        self.model = model