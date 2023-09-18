from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_lear = {}


try:
    data = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_lear = original_data.to_dict(orient="records")
else:
    to_lear = data.to_dict(orient="records")


def word_btn():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_lear)
    x = current_card['French']
    canvas.itemconfig(lang_card, text="French",fill="black")
    canvas.itemconfig(word_card, text=x, fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(lang_card, text="English", fill="white")
    canvas.itemconfig(word_card, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_img)


def yet_to_learn():
    to_lear.remove(current_card)
    dat = pd.DataFrame(to_lear)
    dat.to_csv("data/to_learn.csv", index=False)
    word_btn()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

lang_card = canvas.create_text(400, 150, font=("Ariel", 30, "italic"), text="")
word_card = canvas.create_text(400, 263, font=("Ariel", 40, "bold"), text="")

wrong_image = PhotoImage(file="images/wrong.png")
button_w = Button(image=wrong_image, highlightthickness=0, bd=0, command=word_btn)
button_w.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
button_r = Button(image=right_image, highlightthickness=0, bd=0, command=yet_to_learn)
button_r.grid(row=1, column=1)

word_btn()

window.mainloop()
