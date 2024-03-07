from tkinter import *
import ttkbootstrap as tb


class SearchView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.search_headline = tb.Label(self, text="Seach for a Pet", font=("Kristen ITC", 24))
        self.location_desc = tb.Label(self, text="Location*", bootstyle="danger")
        self.location = tb.Entry(self, text="Zip Code", bootstyle="danger")
        self.back_button = tb.Button(self, text="Back", bootstyle="primary outline")
        self.advanced_button = tb.Button(self, text="Advanced Search", bootstyle="link")
        self.search_button = tb.Button(self, text="Find a Pet", bootstyle="link")

        self.search_headline.grid(row=0, column=0, pady=20)
        self.location_desc.grid(row=1, column=0)
        self.location.grid(row=2, column=0, pady=10)
        self.advanced_button.grid(row=3, column=0, pady=10)
        self.search_button.grid(row=4, column=0, pady=10)
        self.back_button.grid(row=5, column=0, pady=10)

    def get_location(self):
        return self.location.get()