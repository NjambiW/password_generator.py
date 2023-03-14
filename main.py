from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# #Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for sym in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    passwords = "".join(password_list)
    password_entry.insert(0, passwords)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = password_entry.get()
    email = username_entry.get()
    global new_data
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="please make sure you haven't left any fields empty")
    else:
        try:
            with open("saved_passwords.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("saved_passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("saved_passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("saved_passwords.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="no dat file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email:{email}\npassword{password}")
        else:
            messagebox.showinfo(title="error", message=f"no details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas_image = canvas.create_image(100, 100, image=image)
canvas.grid(column=2, row=0)

website_label = Label(text="Website", font=("courier", 12, "normal"))
website_label.grid(column=0, row=2)

website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(column=2, row=2, columnspan=1)

username_label = Label(text="Email/Username", font=("courier", 12, "normal"))
username_label.grid(column=0, row=3)

username_entry = Entry(width=52)
username_entry.insert(0, "bennedict@gmail.com")
username_entry.grid(column=2, row=3, columnspan=2)

password_label = Label(text="Password", font=("courier", 12, "normal"))
password_label.grid(column=0, row=4)

password_entry = Entry(width=33)
password_entry.grid(column=2, row=4, columnspan=1)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=3, row=2)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=3, row=4)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
