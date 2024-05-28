from tkinter import *
from Ash import *
from PIL import Image, ImageTk


def set_female():
    img = Image.open("female_voice.png")
    img_resized = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img_resized)
    img_label.configure(image=img_tk)
    img_label.image = img_tk
    set_gender(1)


def set_male():
    img = Image.open("male_voice.png")
    img_resized = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img_resized)
    img_label.configure(image=img_tk)
    img_label.image = img_tk
    set_gender(0)


def stop_listening():
    exit()


root = Tk()
root.geometry("450x580")
root.configure(bg="#333333")
image_mic = Image.open("mic.png")
image_mic = image_mic.resize((32, 32))
mic_icon = ImageTk.PhotoImage(image_mic)

listenbtn = Button(root, text="Command", bg="#808080",
                   image=mic_icon, command=dowork, compound="left", font=("Arial", 14), width=400, height=40)
image_close = Image.open("close.png")
image_close = image_close.resize((32, 32))
close_icon = ImageTk.PhotoImage(image_close)
closebtn = Button(root, text="Close", bg="#808080", image=close_icon,
                  command=stop_listening, compound="left", font=("Arial", 14), width=400, height=40)
image_male = Image.open("male.png")
image_male = image_male.resize((32, 32))
male_icon = ImageTk.PhotoImage(image_male)
malebtn = Button(root, text="Male Voice", bg="#808080",
                 image=male_icon, command=set_male, compound="left", font=("Arial", 14), width=400, height=40)
image_female = Image.open("female.png")
image_female = image_female.resize((32, 32))
female_icon = ImageTk.PhotoImage(image_female)
femalebtn = Button(root, text="Female Voice", bg="#808080",
                   image=female_icon, command=set_female, compound="left", font=("Arial", 14), width=400, height=40)

img = Image.open("female_voice.png")

# Resize the image
img_resized = img.resize((300, 300))

# Create a PhotoImage object from the resized image
img_tk = ImageTk.PhotoImage(img_resized)

# Create a label to hold the image
img_label = Label(root, image=img_tk)
img_label.grid(row=0, column=0, padx=10, pady=10)


listenbtn.grid(row=0, column=0, padx=20, pady=5)
closebtn.grid(row=1, column=0, padx=20, pady=5)
img_label.grid(row=2, column=0, padx=20, pady=5)
malebtn.grid(row=3, column=0, padx=20, pady=5)
femalebtn.grid(row=4, column=0, padx=20, pady=5)

root.mainloop()
