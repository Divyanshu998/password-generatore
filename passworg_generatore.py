import random
from tkinter import * 

root = Tk()
root.title('Random Password Generator')
root.geometry('450x450')

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*_-+='

characters = alpha + numbers + symbols

label_characters = Label(root, text="Number of characters", font=('Arial', 12)).pack(padx=10)
character_length = Entry(root, font="Arial 14")
character_length.pack(padx=10)

def generate_password():
    length = character_length.get()
    password = "".join(random.sample(characters, int(length)))
    label_password.config(text='Generated Password: ' + password)

Button(root, text="Generate Password", command=generate_password, font=('Arial', 12)).pack(padx=10)
label_password = Label(root, font=('Arial', 12))
label_password.pack()

root.mainloop()