from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint


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

# print(f"your password is {passwords}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = password_entry.get()
    email = username_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the entered details:\n Email{email}\n"
                                                              f""f" password{password}\n is it ok to save?")
        if is_ok:
            with open("saved_passwords.txt", mode="a") as data_file:
                data_file.write(f"{website}| {email}| {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


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

website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(column=2, row=2, columnspan=2)

username_label = Label(text="Email/Username", font=("courier", 12, "normal"))
username_label.grid(column=0, row=3)

username_entry = Entry(width=52)
username_entry.insert(0, "bennedict@gmail.com")
username_entry.grid(column=2, row=3, columnspan=2)

password_label = Label(text="Password", font=("courier", 12, "normal"))
password_label.grid(column=0, row=4)

password_entry = Entry(width=33)
password_entry.grid(column=2, row=4, columnspan=1)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=3, row=4)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
