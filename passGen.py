####################################
# Random Password Generator
####################################
import tkinter as tk
from string import ascii_letters, digits
from random import choice

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300,  relief='raised')
canvas1.pack()

label = tk.Label(root, text="Password Generator")
label.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label)

label2 = tk.Label(root, text='Type the number of characters:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def generate():
    """Generates a random password"""

    nChar = int(entry1.get())
    entry1.delete(0, tk.END)
    SYMBOL = '!?'
    passw = ''.join([choice(ascii_letters + digits + SYMBOL)
                     for i in range(nChar)])
    label3 = tk.Label(root, text='New Password:',
                      font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    label4 = tk.Label(root, text=passw,
                      font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(text='Generate', command=generate,
                    bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)


root.mainloop()
