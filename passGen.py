####################################
# Random Password Generator
####################################
import tkinter as tk
from string import ascii_letters, digits
from random import choice

SYMBOL = '!?'
passw = ''.join([choice(ascii_letters + digits + SYMBOL)
                 for i in range(10)])


def generate():
    entry.delete(0, tk.END)
    entry.insert(0, passw)


root = tk.Tk()
root.geometry('400x200')


label = tk.Label(root, text="Password Generator")
label.pack(padx=10, pady=10)

entryText = tk.StringVar()
entry = tk.Entry(root, textvariable=entryText)
entryText.set(generate)
entry.pack(padx=10, pady=10)

button = tk.Button(root, text='Generate', command=generate)
button.pack()

root.mainloop()
