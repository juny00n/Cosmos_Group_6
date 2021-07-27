import tkinter as tk
import os
from tkinter import *
from pyo import *
from PIL import ImageTk,Image

currentCount = 0
awardedPoints = 0
played = False

s = Server().boot()  # initialize pyo server
s.start()
#sounds = [SfPlayer("Sounds/blue & clue.wav"), SfPlayer("Sounds/leave & leaf.wav"), SfPlayer("Sounds/dice & dye.wav"), SfPlayer("Sounds/dice & dye.wav"), SfPlayer("Sounds/found & round.wav")]
soundFiles = ["blue & clue.wav", "leave & leaf.wav", "dice & dye.wav", "found & round.wav", "desert & dessert.wav",
              "row & raw.wav", "aware & swear.wav", "17 & 70.wav", "meow.wav", "Barking.wav", "softBirds.wav",
              "Dolphin Sound( Edited).wav", "footstep.wav"]
def setButton(button_play):
    global binaural
    global played
    global currentCount
    global var
    if currentCount == 7:
        switchText()
    if currentCount < len(images) - 1:
        if played:
            button_play.destroy()
            currentCount += 1
            buttons[currentCount].place(x=335, y=250)
            var.set(messages[currentCount])
            played = False
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
    binaural = Binaural(moving_sound, azimuth=phasor, elevation=10)
    return binaural

def button_input(direction):
    if (direction=="quit"):
        quit()
    elif(direction=="start"):
        setUpWindow()

def play_music(bin):
    global played
    global binaural
    binaural = newSound()
    binaural.out()
    print("Sound is playing")
    played = True


def nextQuestion(play_button):
    global binaural
    setButton(play_button)
    print(currentCount)

def switchText():
    global text0, text1, text2, text3
    text0 = "Left"
    text1 = "Right"
    text2 = "Front"
    text3 = "Back"
    global button_first, button_second, button_both, button_none

    button_first.destroy()
    button_second.destroy()
    button_both.destroy()
    button_none.destroy()

    button_left = tk.Button(root, text=text0, padx=20, pady=15, fg="#871414", command=lambda: button_input('left'))
    button_left.place(x=290, y=500)
    button_right = tk.Button(root, text=text1, padx=15, pady=15, fg="#871414", command=lambda: button_input('right'))
    button_right.place(x=490, y=500)

    button_front = tk.Button(root, text=text2, padx=20, pady=15, fg="#871414", command=lambda: button_input('front'))
    button_front.place(x=390, y=450)
    button_back = tk.Button(root, text=text3, padx=20, pady=15, fg="#871414", command=lambda: button_input('back'))
    button_back.place(x=390, y=550)


def scorePage():
    frame = tk.Frame(root, bg="#e3e8df")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    titleBkgd = tk.Frame(root, bg="#871414")
    titleBkgd.place(relwidth=1, relheight=0.1, x=0, y=0)

    message1 = tk.Label(root, text="""You have completed the test!
    Here is your score:""", fg="#871414", bg="#e3e8df", font = "Times 24 bold")
    message1.place(x=250, y=100)

    message2 = tk.Label(root, text="" + str(awardedPoints) + "/12", fg="#871414", bg="#e3e8df", font = "Times 55 bold")
    message2.place(x=370, y=250)

    message3 = tk.Label(root, text="Score Breakdown:", fg="#871414", bg="#e3e8df", font = "Times 25")
    message3.place(x=300, y=400)

    #Need to fill in info on what scores mean/next steps for user

    message4 = tk.Label(root, text="Info will be here...", fg="#871414", bg="#e3e8df", font = "Times 16", justify="left")
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
    #Labels/Questions:
    messages = ["Which audio says the word 'blue'?", "Which audio says the word 'leave'?", "Which audio says the word 'dye'?",
                "Which audio says the word 'found'?", "Which audio says the word 'dessert'?", "Which audio says the word 'row'?",
                "Which audio says the word 'swear'?", "Which audio says the word 'seventy'?", """Which direction is the meowing 
    coming from?""",
                """Which direction is the barking 
    coming from?""", """Which direction is the chirping 
coming from?""", """Which direction are the dolphins 
coming from?""",
                """Which direction are the footsteps 
coming from?"""]

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

    images = [photoImg0, photoImg1, photoImg2, photoImg3, photoImg4, photoImg5, photoImg6, photoImg7,
              photoImg8, photoImg9, photoImg10, photoImg11, photoImg12]

except:
    print("Some files cannot be found.")

binaural = newSound()

#Starting page of application:
frame = tk.Frame(root, bg="#e3e8df")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

titleBkgd = tk.Frame(root, bg="#871414")
titleBkgd.place(relwidth=1, relheight=0.1, x=0, y=0)

photo = PhotoImage(file="Images/cover.png")
photo_ = photo.subsample(2, 2)

cover = tk.Label(root, image=photo_, bg="#e3e8df")
cover.place(x=310, y=250)

m1 = tk.Label(root, text="Auditory Processing Disorder", fg="#871414", bg="#e3e8df", font = "Times 30 bold")
m1.place(x=230, y=150)

m2 = tk.Label(root, text="Early Detection Assessment for Children", fg="#871414", bg="#e3e8df", font = "Times 16")
m2.place(x=280, y=210)

quitButton = tk.Button(root, text="Quit", padx=20, pady=15, fg="#871414", command=lambda: button_input("quit"))
quitButton.place(x=280, y=500)
startButton = tk.Button(root, text="Start", padx=20, pady=15, fg="#871414", command=lambda: button_input("start"))
startButton.place(x=490, y=500)

#---------
play_0 = tk.Button(root, image=images[0], padx=5, pady=5, command=lambda: play_music(binaural))

play_1 = tk.Button(root, image=images[1], padx=5, pady=5, command=lambda: play_music(binaural))

play_2 = tk.Button(root, image=images[2], padx=5, pady=5, command=lambda: play_music(binaural))

play_3 = tk.Button(root, image=images[3], padx=5, pady=5, command=lambda: play_music(binaural))

play_4 = tk.Button(root, image=images[4], padx=5, pady=5, command=lambda: play_music(binaural))

play_5 = tk.Button(root, image=images[5], padx=5, pady=5, command=lambda: play_music(binaural))

play_6 = tk.Button(root, image=images[6], padx=5, pady=5, command=lambda: play_music(binaural))

play_7 = tk.Button(root, image=images[7], padx=5, pady=5, command=lambda: play_music(binaural))

play_8 = tk.Button(root, image=images[8], padx=5, pady=5, command=lambda: play_music(binaural))

play_9 = tk.Button(root, image=images[9], padx=5, pady=5, command=lambda: play_music(binaural))

play_10 = tk.Button(root, image=images[10], padx=5, pady=5, command=lambda: play_music(binaural))

play_11 = tk.Button(root, image=images[11], padx=5, pady=5, command=lambda: play_music(binaural))

play_12 = tk.Button(root, image=images[12], padx=5, pady=5, command=lambda: play_music(binaural))


# List of play buttons:
buttons = [play_0, play_1, play_2, play_3, play_4, play_5, play_6, play_7,
           play_8, play_9, play_10, play_11, play_12]

def setUpWindow():
    cover.destroy()
    m1.destroy()
    m2.destroy()
    startButton.destroy()
    quitButton.destroy()

    global button_first, button_second, button_both, button_none

    #Label
    label = tk.Label(root, textvariable=var, fg="#871414", bg="#e3e8df", font = "Times 16 bold")
    label.place(x=300, y=180)
    #Buttons
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

    button_next = tk.Button(root, text="Next", padx=20, pady=15, fg="#871414", command=lambda: nextQuestion(buttons[currentCount]))
    button_next.place(x=550, y=650)
    button_quit = tk.Button(root, text="Quit", padx=20, pady=15, fg="#871414", command=lambda: button_input('quit'))
    button_quit.place(x=150, y=650)

root.resizable(0, 0)  # user cannot resize window
root.mainloop()
