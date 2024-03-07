from tkinter import *
import ttkbootstrap as tb
import json
from PIL import ImageTk, Image
import urllib.request
import io


class ResultsView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.headline = tb.Label(self, text="Search Results", font=("Kristen ITC", 24))
        self.headline.grid(row=0, column=0)
        self.back_button = tb.Button(self, text="Back", bootstyle="primary outline")
        self.back_button.grid(row=1, column=0)

    def results(self):
        self.bio_buttons = []
        self.pet_names = []
        self.pet_photos = []
        self.pet_ages = []
        self.pet_breeds = []

        try:
            self.master.model.populate()
            self.create_widgets()
            self.place_widgets()

        except json.decoder.JSONDecodeError:
            pass

    def get_biobuttons(self):
        return self.bio_buttons

    def remove(self):
        for i in range(5):
            self.pet_photos[i].destroy()
            self.pet_names[i].destroy()
            self.pet_ages[i].destroy()
            self.pet_breeds[i].destroy()
            self.bio_buttons[i].destroy()

        del self.pet_photos
        del self.pet_names
        del self.pet_ages
        del self.pet_breeds
        del self.bio_buttons

    def create_widgets(self):
        for i in range(5):
            animal = self.master.model.fetch(i)
            with urllib.request.urlopen(animal["photos"][0]["small"]) as u:
                raw_data = u.read()
            image = Image.open(io.BytesIO(raw_data))
            photo = ImageTk.PhotoImage(image)

            self.pet_photos.append(tb.Label(self, image=photo))
            # save reference of the image
            self.pet_photos[i].image = photo

            self.pet_names.append(tb.Label(self, text=animal["name"]))
            self.pet_ages.append(tb.Label(self, text=animal["age"]))
            self.pet_breeds.append(tb.Label(self, text=animal["breeds"]["primary"]))
            self.bio_buttons.append(tb.Button(self, text="Bio", bootstyle="primary outline"))

    def place_widgets(self):
        row_num = 2
        for i in range(5):
            self.pet_photos[i].grid(row=row_num, column=0)
            row_num += 1
            self.pet_names[i].grid(row=row_num, column=0)
            self.bio_buttons[i].grid(row=row_num, column=1)
            row_num += 1
            self.pet_ages[i].grid(row=row_num, column=0)
            self.pet_breeds[i].grid(row=row_num, column=1)
            row_num += 1