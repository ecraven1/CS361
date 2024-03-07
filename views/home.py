from tkinter import *
import ttkbootstrap as tb


class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.intro_headline = tb.Label(self, text="Pet Finder", font=("Kristen ITC", 24))
        desc_string = "Pet Finder allows you to find a furry friend by\n" \
                      "searching adoption agencies near you. Click 'Search'\n" \
                      "and fill out the form with all the details you're looking\n" \
                      "for in your new pet!\n" \
                      "This app is free to use but makes no guarantees about\n" \
                      "how much the adoption agency may choose to charge for\n" \
                      "their services."
        self.app_desc = tb.Label(self, text=desc_string)
        self.search_button = tb.Button(self, text="Search", bootstyle="primary outline")

        self.intro_headline.grid(row=0, column=0, pady=50)
        self.app_desc.grid(row=1, column=0, pady=50)
        self.search_button.grid(row=2, column=0, pady=20)