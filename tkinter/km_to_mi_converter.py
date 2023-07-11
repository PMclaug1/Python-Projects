from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
#sets window to minimum size of objects, or specified size
window.minsize()
#padding
window.config(padx=20, pady=20)

def convert_units():
    print("I got clicked")
    if measurement_unit.cget("text") == "Km":
        km = float(input.get()) * 1.60934
        measurement_text.config(text=f"{km}")
    else:
        mi = float(input.get()) * 0.621371
        measurement_text.config(text=f"{mi}")

def km_to_miles():
    print("I got clicked 2")
    if entry_label.cget("text") == "Miles":
        entry_label.config(text="Km")
        measurement_unit.config(text="Miles")
        measurement_text.config(text="")
    else:
        entry_label.config(text="Miles")
        measurement_unit.config(text="Km")
        measurement_text.config(text="")

#entry component
input = Entry(width=8)
input.grid(row=0, column=1)

entry_label = Label(text="Miles", font=("Arial",20))
entry_label.grid(row=0, column=2)

#converter row
conversion_text = Label(text="Is equal to:", font=("Arial",20))
conversion_text.grid(row=1, column=0)

measurement_text = Label(text="0", font=("Arial",20))
measurement_text.grid(row=1, column=1)

measurement_unit = Label(text="Km", font=("Km",20))
measurement_unit.grid(row=1, column=2)

button = Button(text="Convert", command=convert_units)
button.grid(column=1,row=2)

button = Button(text="Change Units", command=km_to_miles)
button.grid(column=1,row=3)

window.mainloop()