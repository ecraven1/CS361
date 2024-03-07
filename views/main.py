from .root import Root
from .home import HomeView
from .search import SearchView
from .advanced import AdvancedView
from .results import ResultsView
from .bio import BioView
import ttkbootstrap as tb
from tkinter import Tk


class View():
    def __init__(self, model):
        self.model = model
        self.root = Root(self.model)
        self.frames = {}
        self.add_frame("home", HomeView)
        self.add_frame("search", SearchView)
        self.add_frame("advanced", AdvancedView)
        self.add_frame("results", ResultsView)
        self.add_frame("bio", BioView)

    def add_frame(self, frame_name, Frame=None):
        if Frame:
            self.frames[frame_name] = Frame(self.root)
            self.frames[frame_name].grid(row=0, column=0, sticky="nsew")
        else:
            Frame = self.frames[frame_name].__class__
            self.frames[frame_name] = Frame(self.root)
            self.frames[frame_name].grid(row=0, column=0, sticky="nsew")

    def switch_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

    def get_frame(self, frame_name):
        return self.frames[frame_name]

    def begin_mainloop(self):
        self.root.mainloop()