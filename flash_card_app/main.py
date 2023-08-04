from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front)
    timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back)

window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=550)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_bg = canvas.create_image(400, 275, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

incorrect_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=incorrect_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

correct_img = PhotoImage(file="./images/right.png")
known_button = Button(image=correct_img, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
