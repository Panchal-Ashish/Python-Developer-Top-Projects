## json.dump() - write
## json.load() - read
## json.update() - update

## refer save function

## json format stores data as a dictionary... so it is used with python to take inputs, save as a dictionary
## and then work with the dictionary in python... as it is easy

from tkinter import *
from tkinter import messagebox  ## messagebox is not imported even though we have imported all from tkinter
import pyperclip
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for letter in range(random.randint(4, 5))]
    password_numbers = [random.choice(numbers) for number in range(random.randint(2, 3))]
    password_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 3))]

    password_list = password_letters + password_symbols + password_letters

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
    # to copy the new generated password and use it wherever reqd... since you are generating the pswd

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    email_username = email_username_entry.get()
    website = website_entry.get()
    password = password_entry.get()

    new_data = {website:
        {
            "email": email_username,
            "password": password
        }
    }

    if len(email_username) > 0 and len(password) > 0 and len(website) > 0:
        # print(f"{website} | {email_username} | {password}\n")

        try:
            ## json.update---- mode = w ---needs to have something previously, updates it, shows err if file not already present-----#
            with open("pswd_manager.json", mode="r") as data:
                loaded_data = json.load(data)  # loading / reading
                loaded_data.update(new_data)  # updating
            with open("pswd_manager.json", mode="w") as data:
                json.dump(loaded_data, data, indent=4)  # writing updated data

        except FileNotFoundError:
            with open("pswd_manager.json", mode="w") as data:
                json.dump(new_data, data, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    else:
        messagebox.showerror(title="Error", message="Please fill in all relevant details. All fields are compulsory")

# ---------------------------- SEARCH ------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open("pswd_manager.json", mode="r") as data:
            stored_data = json.load(data)
            email_username = stored_data[website]["email"]
            password = stored_data[website]["password"]
            messagebox.showinfo(title=website, message=f"\nEmail/Username: {email_username}"
                                                       f"\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showerror(title= "Error", message= "No such file found")
    except KeyError:
        messagebox.showerror(title= "Error", message= f"The data does not contain the information related to {website} website")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

## LABELS ##
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

## ENTRIES ##
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)

email_username_entry = Entry(width=60)
email_username_entry.insert(INSERT, "panchalashish28321@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

## BUTTONS ##
generate_pswd_button = Button(text="Generate Password", command=generate_password, width=15)
generate_pswd_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text= "Search", width= 15, command= search)
search_button.grid(row= 1, column= 2)

window.mainloop()