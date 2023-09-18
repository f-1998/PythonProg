from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import string
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_gen():
    character = string.digits + string.ascii_letters + string.punctuation
    unshuffled_string = ''.join(random.choice(character) for _ in range(12))
    shuffled_list = list(unshuffled_string)
    random.shuffle(shuffled_list)
    shuffled_string = ''.join(shuffled_list)
    inp3.insert(0, shuffled_string)
    pyperclip.copy(shuffled_string)


def find_password():

    website_val = input1.get()

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

            if website_val in data:
                email1 = data[website_val]['email']
                password1 = data[website_val]['password']
                messagebox.showinfo(website_val, f"Email: {email1}\n"
                                                 f"\nPassword: {password1}")
            else:
                messagebox.showinfo("Oops", "No Information found")
    except FileNotFoundError:
        messagebox.showinfo("Oops", "File not Formed")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_content():

    website_val = input1.get()
    email_val = input2.get()
    pass_val = inp3.get()

    new_data = {website_val: {"email": email_val,
                              "password": pass_val}}

    if len(website_val) == 0 or len(pass_val) == 0:
        messagebox.showinfo("Oops", "Please enter the Info")
    else:
        is_ok = messagebox.askokcancel(title=website_val, message=f"These are the details entered. Is it Ok to Save?"
                                                                  f"\nEmail: {email_val}\n Password: {pass_val}")
        if is_ok:

            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
                    data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            finally:
                input1.delete(0, END)
                inp3.delete(0, END)
                input1.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background="white")


canvas = Canvas(width=200, height=200, highlightthickness=0, background="white")
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)


website = Label(text="Website:", background="white")
website.grid(row=1, column=0)
email = Label(text="Email/Username:", background="white")
email.grid(row=2, column=0)
password = Label(text="Password:", background="white")
password.grid(row=3, column=0)


input1 = Entry(width=30)
input1.grid(row=1, column=1)
input1.focus()
input2 = Entry(width=48)
input2.grid(row=2, column=1, columnspan=2)
input2.insert(0, "example@xyz.com")
inp3 = Entry(width=30)
inp3.grid(row=3, column=1)

add_btn = Button(text="Search", highlightthickness=0, width=12, command=find_password)
add_btn.grid(row=1, column=2, columnspan=2)


pass_btn = Button(text="Generate Password", highlightthickness=0, command=pass_gen)
pass_btn.grid(row=3, column=2,)

add_btn = Button(text="Add", highlightthickness=0, width=41, command=add_content)
add_btn.grid(row=4, column=1, columnspan=2)



window.mainloop()
