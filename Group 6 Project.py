import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
from pyo import *


def button_input(direction):
    print("test")


root = tk.Tk()
root.title("Group 6 Project")

canvas = tk.Canvas(root, height=800, width=800, bg="#263D42")  # green color
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

titleBkgd = tk.Frame(root, bg="black")
titleBkgd.place(relwidth=1, relheight=0.1, x=0, y=0)
#insert image for title text? "APD Test"

button_left = Button(root, text="Left", padx=40, pady=20, command=lambda: button_input('left'))
button_left.place(x=160, y=150)
button_right = Button(root, text="Right", padx=40, pady=20, command=lambda: button_input('right'))
button_right.place(x=560, y=150)

button_continue = Button(root, text="Continue", padx=40, pady=20, command=lambda: button_input('continue'))
button_continue.place(x=360, y=350)

root.resizable(0, 0)  # user cannot resize window
root.mainloop()
