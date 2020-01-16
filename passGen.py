####################################
# Random Password Generator
####################################
import tkinter as tk
from string import ascii_letters, digits
from random import choice

root = tk.Tk()
root.geometry('400x200')

SYMBOL = '!?'

passw = ''.join([choice(ascii_letters + digits + SYMBOL)
                 for i in range(10)])

label = tk.Label(root, text="Password Generator")
label.pack(padx=10, pady=10)

entryText = tk.StringVar()
entry = tk.Entry(root, textvariable=entryText)
entryText.set(passw)
entry.pack(padx=10, pady=10)

root.mainloop()
