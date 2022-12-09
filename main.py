# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip
from setuptools import Command




# for char in range(nr_letters):
#   password_list.append(random.choice(letters))

# for char in range(nr_symbols):
#   password_list += random.choice(symbols)

# for char in range(nr_numbers):
#   password_list += random.choice(numbers)



def generate_button():
    from numpy import number
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    pass3= [random.choice(letters) for x in range(nr_letters)]
    pass1 = [random.choice(numbers) for x in range(nr_numbers)]
    pass2 = [random.choice(symbols) for x in range(nr_symbols)]
    password_list = pass1 + pass2+pass3
    random.shuffle(password_list)

    password1 = ""
    for char in password_list:
        password1 += char
    # print(f"Your password is: {password1}")
    # global password
    # print(f"Your password is: {password1}")
    pyperclip.copy(password1)
    password_input.insert(0,password1)

# ---------------------------- SAVE PASSWORD ------------------------------- #
import json
from tkinter import messagebox

def add_button():
    user_email = email_input.get()
    user_website = website_input.get()
    user_password = password_input.get()
    user_data = {
        user_website : {
            "website":user_website,
            "email":user_email,
            "password": user_password
        }
    }

    if len(user_email) == 0 or len(user_password) == 0 or len(user_website) == 0:
        messagebox.showerror(title="hey", message="please fill all the input")
    else:
        is_ok = messagebox.askokcancel(title="User confirmation", message="Do you want to save your data?")
        if is_ok:
            with open("/Users/andyvo/Desktop/Science/python/100days/porfolio/password-manager/data.json", "r") as data:
                # json.dump(user_data,data,indent=3)
                update_data = json.load(data)
                update_data.update(user_data)
            with open("/Users/andyvo/Desktop/Science/python/100days/porfolio/password-manager/data.json", "w") as data:
                json.dump(update_data, data ,indent=3)
                email_input.delete(0,END)
                website_input.delete(0,END)
                password_input.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Generator")
window.config(padx=20,pady=20)
logo = PhotoImage(file="/Users/andyvo/Desktop/Science/python/100days/porfolio/password-manager/logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)

canvas.grid(column=1,row=0)


website = Label(text="Website", font=("Arial", 24))
website_input = Entry()

website.grid(column=0, row=1)
website_input.grid(column=1, row=1)

email = Label(text="Email/User name", font=("Arial", 24))
email_input = Entry()

# email_input.insert(0,"andy.vo.98vn@gmail.com")
email.grid(column=0, row=2)
email_input.grid(column=1, row=2)

password = Label(text="Password", font=("Arial", 24))
password_input = Entry()
generate_button = Button(text="Generate Password", command=generate_button)

password.grid(column=0, row=3)
password_input.grid(column=1, row=3)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=add_button)
add_button.grid(column=1, row=4)

def search_website():
    user_website = website_input.get()
    with open("/Users/andyvo/Desktop/Science/python/100days/porfolio/password-manager/data.json", "r") as data:
        json_data = json.load(data)
        for website in json_data:
            if website != user_website:
                pass
            else:
                messagebox.askokcancel(title="Results", message=json_data[user_website])

search_button = Button(text="Search", command=search_website)
search_button.grid(column=2, row=1)




window.mainloop()