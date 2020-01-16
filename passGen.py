####################################
# Random Password Generator
####################################
import tkinter as tk
from string import ascii_letters, digits
from random import choice


def generate():
    entry.delete(0, tk.END)
    SYMBOL = '!?'
    passw = ''.join([choice(ascii_letters + digits + SYMBOL)
                     for i in range(10)])
    entry.insert(0, passw)


def clear():
    entry.delete(0, tk.END)


root = tk.Tk()


label = tk.Label(root, text="Password Generator")
label.pack(padx=10, pady=10)

entryText = tk.StringVar()
entry = tk.Entry(root, textvariable=entryText)
entry.pack(side=tk.TOP)

button = tk.Button(root, text='Generate', command=generate)
button2 = tk.Button(root, text='Clear', command=clear)
button.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)

root.mainloop()
