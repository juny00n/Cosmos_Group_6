import tkinter as tk
import os
from tkinter import *
from pyo import *
import pyo as p
import time
from PIL import ImageTk, Image

currentCount = 0
awardedPoints = 0
played = False
answer = ""
direction = [90, -90, 0]
s = Server().boot()  # initialize pyo server
s.start()
soundFiles = ["blue & clue.wav", "leave & leaf.wav", "dice & dye.wav", "found & round.wav", "desert & dessert.wav",
              "row & raw.wav", "aware & swear.wav", "17 & 70.wav", "meow.wav", "Barking.wav", "softBirds.wav",
              "Dolphin Sound( Edited).wav", "FootstepsAudio.wav", "Sax (Middle C) (1).wav", "Piano(Middle A).wav",
              "Cello(High E).wav",
              "Flute(Middle A)(Edit).wav", "Clarinet(High E).wav", "Flute(High E).wav", ]
answers = ["first", "first", "second", "first", "second", "first", "second", "second", "left", "right", "front",
           "right", "left",
           "different", "different", "same"]



def setButton(button_play):
    global binaural
    global played
    global currentCount
    global var
    global answer
    if currentCount == 7:
        switchText()
    elif currentCount == 12:
        switchText()
    if currentCount < len(answers) - 1:
        if played and not answer == "":
            checkAnswer(answer)
            button_play.destroy()
            currentCount += 1
            buttons[currentCount].place(x=335, y=250)
            var.set(messages[currentCount])
            played = False
            answer = ""
        else:
            print("Not played yet")
    else:
        scorePage()
        print("No more questions.")


def newSound():
    global binaural
    global currentCount
    moving_sound = SfPlayer(f"Sounds/{soundFiles[currentCount]}")
    phasor = Phasor(0.1)
    if currentCount <= 7:
        binaural = Binaural(moving_sound, azimuth=phasor, elevation=10).out()
    elif 8 <= currentCount < 13:
        if answers[currentCount] == "left":
            binaural = p.HRTF(moving_sound, azimuth=direction[1]).out()
        elif answers[currentCount] == "right":
            binaural = p.HRTF(moving_sound, azimuth=direction[0]).out()
        elif answers[currentCount] == "front":
            binaural = p.HRTF(moving_sound, azimuth=direction[2]).out()
    else:
        binaural = Binaural(moving_sound, azimuth=phasor, elevation=10).out()
        time.sleep(5)
        moving_sound = SfPlayer(f"Sounds/{soundFiles[currentCount + 3]}")
        binaural = Binaural(moving_sound, azimuth=phasor, elevation=10).out()

    return binaural


def button_input(direction):
    global awardedPoints
    global answer
    if (direction == "quit"):
        quit()
    elif (direction == "start"):
        setUpWindow()
    answer = direction
    print(direction)


def checkAnswer(answer):
    global awardedPoints
    if answer == answers[currentCount]:
        awardedPoints += 1
        print("correct")
    else:
        print("wrong")


def play_music():
    global played
    newSound()
    print("Sound is playing")
    played = True


def nextQuestion(play_button):
    global binaural
    setButton(play_button)
    print(currentCount)


def switchText():
    global currentCount
    global text0, text1, text2, text3
    global button_first, button_second, button_both, button_none
    global button_front, button_back
    button_first.destroy()
    button_second.destroy()
    button_both.destroy()
    button_none.destroy()

    if currentCount == 7:
        text0 = "Left"
        text1 = "Right"
        text2 = "Front"
        text3 = "Back"
    else:
        text0 = "Same"
        text1 = "Different"
        text2 = ""
        text3 = ""
        button_back.destroy()
        button_front.destroy()

    button_left = tk.Button(root, text=text0, padx=20, pady=15, fg="#871414", command=lambda: button_input(text0.lower()))
    button_left.place(x=290, y=500)
    button_right = tk.Button(root, text=text1, padx=15, pady=15, fg="#871414", command=lambda: button_input(text1.lower()))
    button_right.place(x=490, y=500)
    button_front = tk.Button(root, text=text2, padx=20, pady=15, fg="#871414", command=lambda: button_input(text2.lower()))
    button_front.place(x=390, y=450)
    button_back = tk.Button(root, text=text3, padx=20, pady=15, fg="#871414", command=lambda: button_input(text3.lower()))
    button_back.place(x=390, y=550)

    if currentCount > 7:
        button_front.destroy()
        button_back.destroy()

def scorePage():
    frame = tk.Frame(root, bg="#e3e8df")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    titleBkgd = tk.Frame(root, bg="#871414")
    titleBkgd.place(relwidth=1, relheight=0.1, x=0, y=0)

    message1 = tk.Label(root, text="""You have completed the test!
    Here is your score:""", fg="#871414", bg="#e3e8df", font="Times 24 bold")
    message1.place(x=250, y=100)

    message2 = tk.Label(root, text=f"{str(awardedPoints)}/{len(answers)}", fg="#871414", bg="#e3e8df",
                        font="Times 55 bold")
    message2.place(x=370, y=250)

    message3 = tk.Label(root, text="Score Breakdown:", fg="#871414", bg="#e3e8df", font="Times 25")
    message3.place(x=300, y=400)

    # Need to fill in info on what scores mean/next steps for user

    message4 = tk.Label(root, text="Info will be here...", fg="#871414", bg="#e3e8df", font="Times 16", justify="left")
    message4.place(x=220, y=450)


root = tk.Tk()  # initialize tkinter window
root.title("Group 6 Project")

canvas = tk.Canvas(root, height=800, width=800, bg="#871414")  # red color
canvas.pack()

var = StringVar()
text0 = "First"
text1 = "Second"
text2 = "Both"
text3 = "None"

try:
    # Labels/Questions:
    messages = ["Which audio says the word 'blue'?", "Which audio says the word 'leave'?",
                "Which audio says the word 'dye'?",
                "Which audio says the word 'found'?", "Which audio says the word 'dessert'?",
                "Which audio says the word 'row'?",
                "Which audio says the word 'swear'?", "Which audio says the word 'seventy'?",
                """Which direction is the meowing coming from?""",
                """Which direction is the barking coming from?""", """Which direction is the chirping coming from?""",
                """Which direction are the dolphins coming from?""",
                """Which direction are the footsteps coming from?""",
                "Are the same notes being played?",
                "Are the same notes being played?",
                "Are the same notes being played?"]

    # Images:
    photo0 = PhotoImage(file="Images/clue.png")
    photoImg0 = photo0.subsample(5, 5)

    photo1 = PhotoImage(file="Images/leaves.png")
    photoImg1 = photo1.subsample(5, 5)

    photo2 = PhotoImage(file="Images/dice.png")
    photoImg2 = photo2.subsample(5, 5)

    photo3 = PhotoImage(file="Images/round.png")
    photoImg3 = photo3.subsample(3, 3)

    photo4 = PhotoImage(file="Images/desert.png")
    photoImg4 = photo4.subsample(5, 5)

    photo5 = PhotoImage(file="Images/row.png")
    photoImg5 = photo5.subsample(5, 5)

    photo6 = PhotoImage(file="Images/aware.png")
    photoImg6 = photo6.subsample(4, 4)

    photo7 = PhotoImage(file="Images/70.png")
    photoImg7 = photo7.subsample(5, 5)

    photo8 = PhotoImage(file="Images/meow.png")
    photoImg8 = photo8.subsample(5, 5)

    photo9 = PhotoImage(file="Images/bark.png")
    photoImg9 = photo9.subsample(5, 5)

    photo10 = PhotoImage(file="Images/bird_.png")
    photoImg10 = photo10.subsample(6, 6)

    photo11 = PhotoImage(file="Images/dolph.png")
    photoImg11 = photo11.subsample(6, 6)

    photo12 = PhotoImage(file="Images/foot.png")
    photoImg12 = photo12.subsample(4, 4)

    photo13 = PhotoImage(file="Images/sax.png")
    photoImg13 = photo13.subsample(5, 5)

    photo14 = PhotoImage(file="Images/piano.png")
    photoImg14 = photo14.subsample(3, 3)

    photo15 = PhotoImage(file="Images/cello.png")
    photoImg15 = photo15.subsample(2, 2)

    photo16 = PhotoImage(file="Images/flute.png")
    photoImg16 = photo16.subsample(4, 4)

    photo17 = PhotoImage(file="Images/clarinet.png")
    photoImg17 = photo17.subsample(4, 4)

    photo18 = PhotoImage(file="Images/flute.png")
    photoImg18 = photo18.subsample(4, 4)

    images = [photoImg0, photoImg1, photoImg2, photoImg3, photoImg4, photoImg5, photoImg6, photoImg7,
              photoImg8, photoImg9, photoImg10, photoImg11, photoImg12, photoImg13, photoImg14, photoImg15, photoImg16,
              photoImg17, photoImg18]

except:
    print("Some files cannot be found.")
    quit()

# binaural = newSound()

# Starting page of application:
frame = tk.Frame(root, bg="#e3e8df")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

titleBkgd = tk.Frame(root, bg="#871414")
titleBkgd.place(relwidth=1, relheight=0.1, x=0, y=0)

photo = PhotoImage(file="Images/cover.png")
photo_ = photo.subsample(2, 2)

cover = tk.Label(root, image=photo_, bg="#e3e8df")
cover.place(x=310, y=250)

m1 = tk.Label(root, text="Auditory Processing Disorder", fg="#871414", bg="#e3e8df", font="Times 30 bold")
m1.place(x=230, y=150)

m2 = tk.Label(root, text="Early Detection Assessment for Children", fg="#871414", bg="#e3e8df", font="Times 16")
m2.place(x=280, y=210)

quitButton = tk.Button(root, text="Quit", padx=20, pady=15, fg="#871414", command=lambda: button_input("quit"))
quitButton.place(x=280, y=500)
startButton = tk.Button(root, text="Start", padx=20, pady=15, fg="#871414", command=lambda: button_input("start"))
startButton.place(x=490, y=500)

# ---------
play_0 = tk.Button(root, image=images[0], padx=5, pady=5, command=play_music)

play_1 = tk.Button(root, image=images[1], padx=5, pady=5, command=play_music)

play_2 = tk.Button(root, image=images[2], padx=5, pady=5, command=play_music)

play_3 = tk.Button(root, image=images[3], padx=5, pady=5, command=play_music)

play_4 = tk.Button(root, image=images[4], padx=5, pady=5, command=play_music)

play_5 = tk.Button(root, image=images[5], padx=5, pady=5, command=play_music)

play_6 = tk.Button(root, image=images[6], padx=5, pady=5, command=play_music)

play_7 = tk.Button(root, image=images[7], padx=5, pady=5, command=play_music)

play_8 = tk.Button(root, image=images[8], padx=5, pady=5, command=play_music)

play_9 = tk.Button(root, image=images[9], padx=5, pady=5, command=play_music)

play_10 = tk.Button(root, image=images[10], padx=5, pady=5, command=play_music)

play_11 = tk.Button(root, image=images[11], padx=5, pady=5, command=play_music)

play_12 = tk.Button(root, image=images[12], padx=5, pady=5, command=play_music)
play_13 = tk.Button(root, image=images[13], padx=5, pady=5, command=play_music)
play_14 = tk.Button(root, image=images[14], padx=5, pady=5, command=play_music)
play_15 = tk.Button(root, image=images[15], padx=5, pady=5, command=play_music)
play_16 = tk.Button(root, image=images[16], padx=5, pady=5, command=play_music)
play_17 = tk.Button(root, image=images[17], padx=5, pady=5, command=play_music)
play_18 = tk.Button(root, image=images[18], padx=5, pady=5, command=play_music)

# List of play buttons:
buttons = [play_0, play_1, play_2, play_3, play_4, play_5, play_6, play_7,
           play_8, play_9, play_10, play_11, play_12, play_13, play_14, play_15, play_16, play_17, play_18]


def setUpWindow():
    cover.destroy()
    m1.destroy()
    m2.destroy()
    startButton.destroy()
    quitButton.destroy()

    global button_first, button_second, button_both, button_none

    # Label
    label = tk.Label(root, textvariable=var, fg="#871414", bg="#e3e8df", font="Times 16 bold")
    label.place(x=300, y=180)
    # Buttons
    buttons[0].place(x=330, y=250)
    var.set(messages[0])
    button_first = tk.Button(root, text=text0, padx=20, pady=15, fg="#871414", command=lambda: button_input('first'))
    button_first.place(x=290, y=500)
    button_second = tk.Button(root, text=text1, padx=15, pady=15, fg="#871414", command=lambda: button_input('second'))
    button_second.place(x=490, y=500)

    button_both = tk.Button(root, text=text2, padx=20, pady=15, fg="#871414", command=lambda: button_input('both'))
    button_both.place(x=390, y=450)
    button_none = tk.Button(root, text=text3, padx=20, pady=15, fg="#871414", command=lambda: button_input('none'))
    button_none.place(x=390, y=550)

    button_next = tk.Button(root, text="Next", padx=20, pady=15, fg="#871414",
                            command=lambda: nextQuestion(buttons[currentCount]))
    button_next.place(x=550, y=650)
    button_quit = tk.Button(root, text="Quit", padx=20, pady=15, fg="#871414", command=lambda: button_input('quit'))
    button_quit.place(x=150, y=650)


root.resizable(0, 0)  # user cannot resize window
root.mainloop()
