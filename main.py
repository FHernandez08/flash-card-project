import random
from tkinter import *

import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(french_title, text="French", fill="black")
    canvas.itemconfig(main_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=old_image)
    flip_timer = window.after(3000, func=change_card)

def change_card():
    new_image = PhotoImage(file="images/card_back.png")

    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(french_title, fill='#FFFFFF', text="English")
    canvas.itemconfig(main_word, fill='#FFFFFF', text=current_card["English"])

def is_known():
    to_learn.remove(current_card)

    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=change_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
old_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=old_image)
canvas.grid(row=0, column=0, columnspan=2)

french_title = canvas.create_text(400, 150, text="", font=TITLE_FONT)
main_word = canvas.create_text(400, 263, text="", font=WORD_FONT)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()