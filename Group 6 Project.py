import tkinter as tk
import os
from tkinter import *
from pyo import *

s = Server().boot()
s.start()
moving_sound = SfPlayer("/Users/rucha/Desktop/cluster5/myProject/ShortBirdNoises.wav", mul=0.3)
phasor = Phasor(0.1)
binaural = Binaural(moving_sound, azimuth = phasor, elevation = 10)

currentCount = 0

def button_input(direction):
    print("test")

def play_music():
    binaural.out()
    print("Sound is playing")

def nextQuestion():
    setButton()
    print(currentCount)

root = tk.Tk()
root.title("Group 6 Project")

canvas = tk.Canvas(root, height=800, width=800, bg="#871414")  # red color
canvas.pack()

frame = tk.Frame(root, bg="#e3e8df")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

titleBkgd = tk.Frame(root, bg="#871414")
titleBkgd.place(relwidth=1, relheight=0.1, x=0, y=0)
#insert image for title text? "APD Test"

#Images:
photo0 = PhotoImage(file = r"/Users/rucha/Desktop/cluster5/myProject/clue.png")
photoImg0 = photo0.subsample(5, 5)

photo1 = PhotoImage(file = r"/Users/rucha/Desktop/cluster5/myProject/leaves.png")
photoImg1 = photo1.subsample(5, 5)

photo2 = PhotoImage(file = r"/Users/rucha/Desktop/cluster5/myProject/dice.png")
photoImg2 = photo2.subsample(5, 5)

photo3 = PhotoImage(file = r"/Users/rucha/Desktop/cluster5/myProject/round.png")
photoImg3 = photo3.subsample(3, 3)


images = [photoImg0, photoImg1, photoImg2, photoImg3]

play_0 = tk.Button(root, image=images[0], padx=5, pady=5, command=play_music)
#play_0.place(x=330, y=250)

play_1 = tk.Button(root, image=images[1], padx=5, pady=5, command=play_music)
#play_1.place(x=330, y=250)

play_2 = tk.Button(root, image=images[2], padx=5, pady=5, command=play_music)
#play_2.place(x=330, y=250)

play_3 = tk.Button(root, image=images[3], padx=5, pady=5, command=play_music)
#play_3.place(x=330, y=250)

#List of play buttons:
buttons = [play_0, play_1, play_2, play_3]

#Regular Buttons:
button_play = tk.Button(root, image=images[0], padx=5, pady=5, command=play_music)
button_play.place(x=330, y=250)
button_left = tk.Button(root, text="Left", padx=40, pady=20, fg = "#871414", command=lambda: button_input('left'))
button_left.place(x=260, y=450)
button_right = tk.Button(root, text="Right", padx=40, pady=20, fg = "#871414", command=lambda: button_input('right'))
button_right.place(x=460, y=450)

#Function to destroy old button & create new one (need to fix)
def setButton():
    button_play.destroy()
    global currentCount
    currentCount+=1
    button_play1 = tk.Button(root, image=images[currentCount], padx=5, pady=5, command=play_music)
    button_play1.place(x=330, y=250)

button_next = tk.Button(root, text="Next", padx=40, pady=20, fg = "#871414", command=lambda: nextQuestion())
button_next.place(x=550, y=650)

root.resizable(0, 0)  # user cannot resize window
root.mainloop()
