from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
main_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=main_img)
canvas.grid(row=0, column=0, columnspan=2)

canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
canvas.create_text(400, 263, text="Word", font=WORD_FONT)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)


window.mainloop()