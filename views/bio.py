from tkinter import *
import ttkbootstrap as tb
from PIL import ImageTk, Image
import urllib.request
import io


class BioView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.intro_headline = tb.Label(self, text="Bio", font=("Kristen ITC", 24))
        self.intro_headline.grid(row=0, column=0)

        self.back_button = tb.Button(self, text="Back", bootstyle="primary")
        self.back_button.grid(row=6, column=0)

        self.adopt_button = tb.Button(self, text="Adopt!", bootstyle="primary")
        self.adopt_button.grid(row=5, column=0)

    def bio(self, i):
        self.animal = self.master.model.fetch(i)
        self.pet_name = tb.Label(self, text=self.animal["name"], font=("Kristen ITC", 24))
        self.pet_name.grid(row=2, column=0)

        with urllib.request.urlopen(self.animal["photos"][0]["medium"]) as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        photo = ImageTk.PhotoImage(image)
        self.pet_photo = tb.Label(self, image=photo)
        # save reference of the image
        self.pet_photo.image = photo
        self.pet_photo.grid(row=3, column=0)

        self.description = tb.Label(self, text=self.animal["description"])
        self.description.grid(row=4, column=0)

    def remove(self):
        self.pet_photo.destroy()
        self.description.destroy()
        del self.pet_photo
        del self.description
        self.pet_name.destroy()
        del self.pet_name
        del self.animal

    def get_animal(self):
        return self.animal