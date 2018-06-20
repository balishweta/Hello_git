

# 1. Write a python using tkinter interface to write Hello World and an exit button that closes the interface

import tkinter
import sys

m = tkinter.Tk(className='first program')

w = tkinter.Label(m, text='Hello World')
w.pack(side=tkinter.LEFT)
button = tkinter.Button(m, text='Exit', command=sys.exit)
button.pack(side=tkinter.RIGHT)
m.mainloop()

#2. Write a python program to the same interface and create a action when the button is clicked some text is displayed


import tkinter
from tkinter import *
import sys


def display():
    print("Tkinter is easy to use!")
    p = Label(m, text='Clicked')
    p.pack(side=BOTTOM)


m = tkinter.Tk(className='first program')

w = tkinter.Label(m, text='Hello World')
w.pack(side=tkinter.LEFT)
button1 = tkinter.Button(m, text='Click me', command=display)
button1.pack(side=tkinter.LEFT)
button = tkinter.Button(m, text='Exit', command=sys.exit)
button.pack(side=tkinter.RIGHT)
m.mainloop()

# 3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label
# to some other text


import tkinter as Tk
from tkinter import *
import sys


root = Tk()

frame = Frame(root)
frame.pack()

text = StringVar()
text.set('old')
status = IntVar()


def change_label():
    if status.get() == 1:  # if clicked
        text.set('new')
    else:
        text.set('old')


button = Checkbutton(frame, text='Change Label', variable=status, fg='blue', command=change_label)
lb = Label(root, textvariable=text)
button.pack(side=RIGHT)
lb.pack()
redbutton = Checkbutton(frame, text='Exit', highlightbackground='red', fg='red', command=sys.exit)
redbutton.pack(side=RIGHT)

root.mainloop()

#4. Write a python program using tkinter interface to take input in GUI program and print it


import tkinter as tk
from tkinter import ttk

master = tk.Tk()
lbl = ttk.Label(master, text='enter the name').grid(row=0, column=0)


def click():
    print("Hi," + name.get())
    tk.Label(master, text=name.get()).grid(row=2, column=0)



name = tk.StringVar()
nameentered = ttk.Entry(master, textvariable=name).grid(row=1, column=0)

button = ttk.Button(master, text="submit", command=click).grid(row=1, column=1)
master.mainloop()
