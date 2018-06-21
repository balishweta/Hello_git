# 1. Q1. Create a dict with name and mobile number.Define a GUI interface
# using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.

# import tkinter
# from tkinter import *
#
# def onselect(event):
#     w = event.widget
#     print(w)
#     idx = int(w.curselection()[0])
#     value = w.get(idx)
#     print("Mobile no is" , dict[value])
#
# root = tkinter.Tk()
#
# dict = {'priyanka': 23215711235, 'shweta':237432459}
# mylist = Listbox(root)
# scrollbar = Scrollbar(root)
# scrollbar.pack(side="right", fill="y")
# for key in dict:
#
#     mylist.insert(END, key)
#
#
# mylist.bind('<<ListboxSelect>>', onselect)
# mylist.pack(side=RIGHT, fill=BOTH)
# scrollbar.config(command=mylist.yview)
# mainloop()


#2. In the same tkinter file as created above, create a function to insert items into the dictionary.

import tkinter
from tkinter import *
def return_e1(en):
    content = e1.get()
    mylist.insert(END, content)
    print(content)

def onselect(event):
    w = event.widget
    print(w)
    idx = int(w.curselection()[0])
    value = w.get(idx)
    print("Mobile no is" , dict[value])

root = tkinter.Tk()

dict = {'priyanka': 23215711235, 'shweta':237432459}
mylist = Listbox(root)
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

for key in dict:

    mylist.insert(END, key)

e1 = Entry(root)
e1.bind('<Return>', return_e1)
e1.pack()


mylist.bind('<<ListboxSelect>>', onselect)
mylist.pack(side=RIGHT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()
