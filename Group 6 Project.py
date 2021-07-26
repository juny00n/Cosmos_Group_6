import tkinter as tk
import os
from tkinter import *
from pyo import *

currentCount = 0
played = False

s = Server().boot()  # initialize pyo server
s.start()
#sounds = [SfPlayer("Sounds/blue & clue.wav"), SfPlayer("Sounds/leave & leaf.wav"), SfPlayer("Sounds/dice & dye.wav"), SfPlayer("Sounds/dice & dye.wav"), SfPlayer("Sounds/found & round.wav")]
soundFiles = ["blue & clue.wav", "leave & leaf.wav", "dice & dye.wav", "found & round.wav"]
def setButton(button_play):
    global binaural
    global played
    global currentCount
    if currentCount < len(images) - 1:
        if played:
            button_play.destroy()
            currentCount += 1
            buttons[currentCount].place(x=330, y=250)
            played = False
        else:
            print("Not played yet")
    else:
        print("No more questions.")


def newSound():

    global binaural
    global currentCount
    #moving_sound = sounds[currentCount]
    moving_sound = SfPlayer(f"Sounds/{soundFiles[currentCount]}", mul=0.1)
    phasor = Phasor(0.1)
    binaural = Binaural(moving_sound, azimuth=phasor, elevation=10)
    return binaural

def button_input(direction):
    print(direction)

def play_music(binaural):
    global played
    global currentCount
    #binSounds[currentCount].out()
    binaural.out()
    print("Sound is playing")
    played = True


def nextQuestion(play_button):
    global binaural
    setButton(play_button)
    binaural = newSound()
    print(currentCount)


root = tk.Tk()  # initialize tkinter window
root.title("Group 6 Project")

canvas = tk.Canvas(root, height=800, width=800, bg="#871414")  # red color
canvas.pack()

try:
    # Images:
    photo0 = PhotoImage(file="Images/clue.png")
    photoImg0 = photo0.subsample(5, 5)

    photo1 = PhotoImage(file="Images/leaves.png")
    photoImg1 = photo1.subsample(5, 5)

    photo2 = PhotoImage(file="Images/dice.png")
    photoImg2 = photo2.subsample(5, 5)

    photo3 = PhotoImage(file="Images/round.png")
    photoImg3 = photo3.subsample(3, 3)

    images = [photoImg0, photoImg1, photoImg2, photoImg3]
except:
    print("Some files cannot be found.")

#phasor = Phasor(0.1)
#binaural = Binaural(moving_sound, azimuth=phasor, elevation=10)

binaural = newSound()

frame = tk.Frame(root, bg="#e3e8df")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

titleBkgd = tk.Frame(root, bg="#871414")
titleBkgd.place(relwidth=1, relheight=0.1, x=0, y=0)
# insert image for title text? "APD Test"

play_0 = tk.Button(root, image=images[0], padx=5, pady=5, command=lambda: play_music(binaural))

play_1 = tk.Button(root, image=images[1], padx=5, pady=5, command=lambda: play_music(binaural))

play_2 = tk.Button(root, image=images[2], padx=5, pady=5, command=lambda: play_music(binaural))

play_3 = tk.Button(root, image=images[3], padx=5, pady=5, command=lambda: play_music(binaural))

# List of play buttons:
buttons = [play_0, play_1, play_2, play_3]

# Regular Buttons:
buttons[0].place(x=330, y=250)
button_left = tk.Button(root, text="Left", padx=40, pady=20, fg="#871414", command=lambda: button_input('left'))
button_left.place(x=260, y=450)
button_right = tk.Button(root, text="Right", padx=40, pady=20, fg="#871414", command=lambda: button_input('right'))
button_right.place(x=460, y=450)

button_next = tk.Button(root, text="Next", padx=40, pady=20, fg="#871414", command=lambda: nextQuestion(buttons[currentCount]))
button_next.place(x=550, y=650)

root.resizable(0, 0)  # user cannot resize window
root.mainloop()
