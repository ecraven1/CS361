# <a href="https://www.flaticon.com/free-icons/pets" title="pets icons">Pets icons created by iconixar - Flaticon</a>

from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="morph")
root.title("Pet Finder")
root.geometry("500x800")
pet_icon = PhotoImage(file='images/pet_ico.png')
root.tk.call('wm', 'iconphoto', root._w, pet_icon)

advanced = True

def search_clicked():
    search_button.pack_forget()
    intro_headline.pack_forget()
    app_desc.pack_forget()
    find_button.pack_forget()

    search_headline.pack(pady=20)
    location_desc.pack()
    location.pack(pady=10)
    advanced_button.pack(pady=10)
    """
    type_desc.pack()
    type.pack(pady=10)
    gender_desc.pack()
    gender.pack(pady=10)
    distance_desc.pack()
    distance.pack(pady=10)
    size_desc.pack()
    size.pack(pady=10)
    gw_dogs.pack(pady=10)
    gw_cats.pack(pady=10)
    gw_child.pack(pady=10)
    house_train.pack(pady=10)
    """
    #find_button.pack(pady=10)
    back_button.pack(pady=10)



def back_clicked():
    global advanced
    search_headline.pack_forget()
    location_desc.pack_forget()
    location.pack_forget()
    #find_button.pack_forget()
    back_button.pack_forget()
    advanced_button.pack_forget()
    if advanced is False:
        type_desc.pack_forget()
        type.pack_forget()
        gender_desc.pack_forget()
        gender.pack_forget()
        distance_desc.pack_forget()
        distance.pack_forget()
        size_desc.pack_forget()
        size.pack_forget()
        gw_dogs.pack_forget()
        gw_cats.pack_forget()
        gw_child.pack_forget()
        house_train.pack_forget()
        advanced = True


    intro_headline.pack(pady=50)
    app_desc.pack(pady=50)
    search_button.pack(pady=20)


def advanced_clicked():
    global advanced
    if advanced:
        back_button.pack_forget()
        type_desc.pack()
        type.pack(pady=10)
        gender_desc.pack()
        gender.pack(pady=10)
        distance_desc.pack()
        distance.pack(pady=10)
        size_desc.pack()
        size.pack(pady=10)
        gw_dogs.pack(pady=10)
        gw_cats.pack(pady=10)
        gw_child.pack(pady=10)
        house_train.pack(pady=10)
        back_button.pack(pady=10)
        advanced = False
    else:
        type_desc.pack_forget()
        type.pack_forget()
        gender_desc.pack_forget()
        gender.pack_forget()
        distance_desc.pack_forget()
        distance.pack_forget()
        size_desc.pack_forget()
        size.pack_forget()
        gw_dogs.pack_forget()
        gw_cats.pack_forget()
        gw_child.pack_forget()
        house_train.pack_forget()
        #back_button.pack_forget()
        #back_button.pack(pady=10)
        advanced = True


# Create Widgets

# Labels
intro_headline = tb.Label(root, text="Pet Finder", font=("Kristen ITC", 24))
desc_string = "Pet Finder allows you to find a furry friend by\n" \
              "searching adoption agencies near you. Click 'Search'\n" \
              "and fill out the form with all the details you're looking\n" \
              "for in your new pet!\n" \
              "This app is free to use but makes no guarantees about\n" \
              "how much the adoption agency may choose to charge for\n" \
              "their services."
app_desc = tb.Label(root, text=desc_string)
search_headline = tb.Label(root, text="Seach for a Pet", font=("Kristen ITC", 24))
location_desc = tb.Label(root, text="Location*", bootstyle="danger")
type_desc = tb.Label(root, text="Type")
gender_desc = tb.Label(root, text="Gender")
distance_desc = tb.Label(root, text="Distance")
size_desc = tb.Label(root, text="Size")


# Buttons
find_button = tb.Button(root, text="Find a Pet", bootstyle="primary outline")
search_button = tb.Button(root, text="Search", bootstyle="primary outline", command=search_clicked)
back_button = tb.Button(root, text="Back", bootstyle="primary outline", command=back_clicked)
advanced_button = tb.Button(root, text="Advanced Search", bootstyle="link", command=advanced_clicked)

# Entries
location = tb.Entry(root, text="Zip Code", bootstyle="danger")

# Comboboxes
types = ["Dog", "Cat", "Rabbit", "Bird"]
genders = ["Female", "Male"]
distances = [1, 5, 10, 20, 50]
sizes = ["Small", "Medium", "Large", "X-Large"]
type = tb.Combobox(root, text="Type", bootstyle="secondary", values=types)
gender = tb.Combobox(root, text="Gender", bootstyle="secondary", values=genders)
distance = tb.Combobox(root, text="Distance", bootstyle="secondary", values=distances)
size = tb.Combobox(root, text="Size", bootstyle="secondary", values=sizes)

# Toggles
gw_dogs = tb.Checkbutton(root, text="Good with Dogs", bootstyle="primary, round-toggle")
gw_cats = tb.Checkbutton(root, text="Good with Cats", bootstyle="primary, round-toggle")
gw_child = tb.Checkbutton(root, text="Good with Children", bootstyle="primary, round-toggle")
house_train = tb.Checkbutton(root, text="Housetrained", bootstyle="primary, round-toggle")

# Place Widgets
intro_headline.pack(pady=50)
app_desc.pack(pady=50)
search_button.pack(pady=20)


root.mainloop()