from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def create_password():
    password_list = []

    pass_letters = [choice(letters) for _ in range(randint(8,10))]

    pass_symbols = [choice(symbols) for _ in range(randint(2,4))]

    pass_nums = [choice(numbers) for _ in range(randint(2,4))]

    password_list = pass_letters + pass_symbols + pass_nums

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(END, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    print("saving info")
    website_save = website_input.get()
    email_save = email.get()
    password_save = password_entry.get()
    new_data = {
        website_save: {
            "email": email_save,
            "password": password_save
        }
                }

    if len(website_save) == 0 or len(password_save) == 0:
        messagebox.showinfo(title="Error", message="Invalid entry")
    else:
        is_ok = messagebox.askokcancel(title=website_save, message=f"Info Entered: \nEmail: {email_save}\nPassword: {password_save}\n OK to save?")

        if is_ok:
            try:
                with open("data.json", "w") as data_file:
                    # read old data
                    data = json.load(data_file)
            except FileNotFoundError:
                #file not found - create new file and write
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            else:
                #update data w/ new data - if try block is successful
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    #save updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# canvas logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image((100, 100), image=logo)
canvas.grid(row=0, column=1)

# website entry row
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# email/username entry row
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email = Entry(width=35)
email.insert(END, "my_email@email.com")
email.grid(row=2, column=1, columnspan=2)

# password row
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", highlightthickness=0, command=create_password)
password_button.grid(row=3, column=3)

# add button
add_button = Button(text="Add Password", highlightthickness=0, width=36, command= save_info)
add_button.grid(row=4, column=1)





window.mainloop()