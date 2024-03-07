from tkinter import *
import ttkbootstrap as tb


class AdvancedView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.labels()
        self.buttons()
        self.comboboxes()
        self.toggles()

        self.place_labels()
        self.place_comboboxes()
        self.place_toggles()
        self.place_buttons()

    def get_location(self):
        return self.location.get()

    def get_type(self):
        return self.type.get()

    def get_distance(self):
        return self.distance.get()

    def get_gender(self):
        return self.gender.get()

    def get_size(self):
        return self.size.get()

    def get_gwdogs(self):
        return self.gwdogs_var.get()

    def get_gwchild(self):
        return self.gwchild_var.get()

    def get_gwcats(self):
        return self.gwcats_var.get()

    def get_housetrained(self):
        return self.housetrain_var.get()

    def labels(self):
        self.search_headline = tb.Label(self, text="Seach for a Pet", font=("Kristen ITC", 24))
        self.location_desc = tb.Label(self, text="Location*", bootstyle="danger")
        self.type_desc = tb.Label(self, text="Type")
        self.gender_desc = tb.Label(self, text="Gender")
        self.distance_desc = tb.Label(self, text="Distance")
        self.size_desc = tb.Label(self, text="Size")

    def place_labels(self):
        self.search_headline.grid(row=0, column=0, pady=20)
        self.location_desc.grid(row=1, column=0)
        self.type_desc.grid(row=4, column=0)
        self.gender_desc.grid(row=6, column=0)
        self.distance_desc.grid(row=8, column=0)
        self.size_desc.grid(row=10, column=0)

    def toggles(self):
        self.gwdogs_var = tb.StringVar()
        self.gwcats_var = tb.StringVar()
        self.gwchild_var = tb.StringVar()
        self.housetrain_var = tb.StringVar()
        self.gw_dogs = tb.Checkbutton(self, text="Good with Dogs", variable=self.gwdogs_var,
                                      bootstyle="primary, round-toggle")
        self.gw_cats = tb.Checkbutton(self, text="Good with Cats", variable=self.gwcats_var,
                                      bootstyle="primary, round-toggle")
        self.gw_child = tb.Checkbutton(self, text="Good with Children", variable=self.gwchild_var,
                                       bootstyle="primary, round-toggle")
        self.house_train = tb.Checkbutton(self, text="Housetrained", variable=self.housetrain_var,
                                          bootstyle="primary, round-toggle")

    def place_toggles(self):
        self.gw_dogs.grid(row=12, column=0, pady=10)
        self.gw_cats.grid(row=13, column=0, pady=10)
        self.gw_child.grid(row=14, column=0, pady=10)
        self.house_train.grid(row=15, column=0, pady=10)

    def comboboxes(self):
        types = ["Dog", "Cat", "Rabbit", "Bird"]
        genders = ["Female", "Male"]
        distances = [1, 5, 10, 20, 50]
        sizes = ["Small", "Medium", "Large", "Xlarge"]
        self.type = tb.Combobox(self, text="Type", bootstyle="secondary", values=types)
        self.gender = tb.Combobox(self, text="Gender", bootstyle="secondary", values=genders)
        self.distance = tb.Combobox(self, text="Distance", bootstyle="secondary", values=distances)
        self.size = tb.Combobox(self, text="Size", bootstyle="secondary", values=sizes)
        self.location = tb.Entry(self, text="Zip Code", bootstyle="danger")

    def place_comboboxes(self):
        self.location.grid(row=2, column=0, pady=10)
        self.type.grid(row=5, column=0, pady=10)
        self.gender.grid(row=7, column=0, pady=10)
        self.distance.grid(row=9, column=0, pady=10)
        self.size.grid(row=11, column=0, pady=10)

    def buttons(self):
        self.back_button = tb.Button(self, text="Back", bootstyle="primary outline")
        self.advanced_button = tb.Button(self, text="Advanced Search", bootstyle="link")
        self.search_button = tb.Button(self, text="Find a Pet", bootstyle="primary outline")

    def place_buttons(self):
        self.advanced_button.grid(row=3, column=0, pady=10)
        self.back_button.grid(row=16, column=0, pady=10)
        self.search_button.grid(row=17, column=0, pady=10)