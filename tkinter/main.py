from tkinter import *

window = Tk()
window.title("1st GUI program")
#sets window to minimum size of objects, or specified size
window.minsize(width=500, height=300)

#label
#font is a tuple, name of font, size and styling
my_label = Label(text="I am a label", font=("Arial,", 24, "bold"))
#pack places and centers on screen - can set settings for size or expand etc
my_label.pack()

#update component
my_label["text"] = "New Text"
my_label.config(text="New Text")

#button

def button_clicked():
    print("I got clicked")
    next_text = input.get()
    my_label.config(text=next_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()

#entry component
input = Entry(width=15)
input.pack()


# keeps window open. must be at the end of the file
window.mainloop()