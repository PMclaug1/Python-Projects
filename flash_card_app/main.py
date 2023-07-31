from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=550)
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 275, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

incorrect_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=incorrect_img, highlightthickness=0)
unknown_button.grid(row=1, column=0)

correct_img = PhotoImage(file="./images/right.png")
known_button = Button(image=correct_img, highlightthickness=0)
known_button.grid(row=1, column=1)

window.mainloop()
