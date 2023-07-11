import tkinter

window = tkinter.Tk()
window.title("1st GUI program")
#sets window to minimum size of objects, or specified size
window.minsize(width=500, height=300)

#label
#font is a tuple, name of font, size and styling
my_label = tkinter.Label(text="I am a label", font=("Arial,", 24, "bold"))
#pack places and centers on screen - can set settings for size or expand etc
my_label.pack()

# keeps window open. must be at the end of the file
window.mainloop()