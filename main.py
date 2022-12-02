# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import json
import tkinter
from password_generator import Password

password=Password()
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import Tk
window = Tk()
window.title("My PASSWORD GENERATOR")
window.config(padx=50,pady=50)
canvas = tkinter.Canvas(height=200,width=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

###Creating all the required labels:
website_label  =tkinter.Label(text="WEBSITE")
website_label.grid(row=1,column=0)
email_label = tkinter.Label(text="EMAIL/USERNAME")
email_label.grid(row=2,column=0)
password_label  = tkinter.Label(text="Password")
password_label.grid(row=3,column=0)

###Entries:
website_Entries = tkinter.Entry(width=35)

website_Entries.grid(row=1,column=1,columnspan=2)
email_Entry = tkinter.Entry(width=35)
email_Entry.insert(0,"abhyashupreti1@gmail.com")

email_Entry.grid(row=2,column=1,columnspan=2)
password_Entry = tkinter.Entry(width=21)

password_Entry.grid(row=3,column=1)

# ---------------------------- SAVE PASSWORD ------------------------------- #
###Adding password to document:
def  add_password_tofile():

    email_entered_data = email_Entry.get()
    password_entry_data = password_Entry.get()
    website_entered_data = website_Entries.get()
    with open("data.txt","a") as data:
        new_data  = data.write(f"{website_entered_data}||{email_entered_data}||{password_entry_data}\n")




def genarate_password():
    password.create_password()
    password_Entry.insert(0,password.password)

generate_password_button = tkinter.Button(text="Generate password",command=genarate_password)
generate_password_button.grid(row=3,column=2,)
add_button = tkinter.Button(text="Add",width=36,command=add_password_tofile)

add_button.grid(row=4,column=1,columnspan=2)

################################################\\












window.mainloop()