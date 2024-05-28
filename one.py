from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("450x400")
root.configure(bg="#333333")

image_mic = Image.open("mic.png")
image_mic = image_mic.resize((32, 32))
mic_icon = ImageTk.PhotoImage(image_mic)

listenbtn = Button(root, text="Listen", bg="#808080",
                   image=mic_icon, compound="left", font=("Arial", 14), width=400, height=40)
listenbtn.grid(row=0, column=0, padx=10, pady=5, columnspan=2, sticky="nsew")

image_file = PhotoImage(file="male_voice.png")
image_file = image_file.subsample(
    image_file.width() // 450, image_file.height() // 300)

# Create a label to hold the image
image_label = Label(root, image=image_file)
image_label.grid(row=1, column=1, rowspan=4, padx=10, pady=5, sticky="nsew")

image_male = Image.open("male.png")
image_male = image_male.resize((32, 32))
male_icon = ImageTk.PhotoImage(image_male)
malebtn = Button(root, text="Male", bg="#808080",
                 image=male_icon, compound="left", font=("Arial", 14), width=200, height=40)
malebtn.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")

image_female = Image.open("female.png")
image_female = image_female.resize((32, 32))
female_icon = ImageTk.PhotoImage(image_female)
femalebtn = Button(root, text="Female", bg="#808080",
                   image=female_icon, compound="left", font=("Arial", 14), width=200, height=40)
femalebtn.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")

# Configure the grid layout to center the widgets
for i in range(6):
    Grid.rowconfigure(root, i, weight=1)
for i in range(2):
    Grid.columnconfigure(root, i, weight=1)

root.mainloop()
