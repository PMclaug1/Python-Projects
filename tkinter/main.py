from tkinter import *

window = Tk()
window.title("1st GUI program")
#sets window to minimum size of objects, or specified size
window.minsize(width=500, height=300)
#padding
window.config(padx=20, pady=20)

def button_clicked():
    print("I got clicked")
    next_text = input.get()
    my_label.config(text=next_text)

#label
#font is a tuple, name of font, size and styling
my_label = Label(text="I am a label", font=("Arial,", 24, "bold"))
#pack places and centers on screen - can set settings for size or expand etc and sides
    #my_label.pack()
#place is a specific x and y coord
    #my_label.place(x=100,y=0)
#grid divides into columns and rows
my_label.grid(column=4,row=0)

#update component
my_label["text"] = "New Text"
my_label.config(text="New Text", padx=10, pady=10)

#button

button = Button(text="Click Me", command=button_clicked)
button.grid(column=4,row=1)

#entry component
input = Entry(width=15)
input.grid(row=2, column=5)
entry_label = Label(text="User Input:", font=("Arial",20))
entry_label.grid(row=2, column=3)

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.grid(row=3, column=4)

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(row=4, column=4)

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(row=5, column=4)

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(row=6, column=4)

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(row=7, column=3)
radiobutton2.grid(row=7, column=5)


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(row=8, column=4)

# keeps window open. must be at the end of the file
window.mainloop()