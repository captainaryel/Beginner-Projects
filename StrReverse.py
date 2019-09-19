# Idea from https://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/
# Program takes some input and returns its 'mirror image'
# Made by captainaryel
# v.1.0

import tkinter as tk


window = tk.Tk()
window.geometry("253x200")
window.title("StrReverse")
window.resizable(False, False)

label1 = tk.Label(window, text="Write something here\nto receive a reverse image of this:")
label1.grid(row=0, columnspan=2)

entry = tk.Entry(window)
entry.grid(row=1, column=0)

outMessage = tk.Label(window, text="OUTPUT:")
outMessage.grid(row=3, columnspan=2)

blank = tk.Entry(window)
blank.grid(row=4, columnspan=2)

def output():
    out = entry.get()
    blank.insert(0, out[::-1])

reverseButton = tk.Button(window, text="Reverse it!", width=17, command=output)
reverseButton.grid(row=1, column=1)

def clearEntries():
    blank.delete(0, len(entry.get()))
    entry.delete(0, len(entry.get()))

clearButton = tk.Button(window, text="CLEAR", command=clearEntries)
clearButton.grid(row=5, columnspan=2)

window.mainloop()