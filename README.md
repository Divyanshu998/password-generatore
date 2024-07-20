import this two package 
using (pip install package name)
import random
from tkinter import *

explaination:-root = Tk(): Initializes the main window.
root.title('Random Password Generator'): Sets the title of the window.
root.geometry('450x450'): Sets the window size to 450x450 pixels.
alpha: String containing all lowercase and uppercase alphabetic characters.
numbers: String containing numeric characters.
symbols: String containing special characters.
characters: Concatenates alpha, numbers, and symbols into a single string containing all possible characters for the password.
label_characters: Label widget prompting the user to enter the number of characters for the password.
character_length: Entry widget where the user inputs the desired password length.
generate_password(): Function to generate a random password.
length = character_length.get(): Retrieves the user input for password length.
password = "".join(random.sample(characters, int(length))): Generates a random password by sampling length characters from characters.
label_password.config(text='Generated Password: ' + password): Updates the label to display the generated password.
Button: Button widget that triggers the generate_password function when clicked.
label_password: Label widget to display the generated password.
Button: Button widget that triggers the generate_password function when clicked.
label_password: Label widget to display the generated password.
