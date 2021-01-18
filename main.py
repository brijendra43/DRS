# All media file is available for download as a zip file
import tkinter
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import dialog
from tkinter import ttk
from tkinter.tix import *
import cv2 # pip install opencv-python
import PIL.Image, PIL.ImageTk # pip install pillow
from functools import partial
import threading
import time
import imutils # pip install imutils
import os
import pygame
import Driver_Cam
import sortcut
import youtube
import subprocess
import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

window = tkinter.Tk()
CHEIGHT=window.winfo_height()
CWIDTH=window.winfo_width()
window.state('zoomed')
window.title("Third Umpire")
filename = filedialog.askopenfilename(initialfile = "clip", title = "select a match mp4 file", filetype= (("mp4", "*.mp4"), ("All files", "*.*")))
window.title(f"Third Umpire({filename})")
menubar = tkinter.Menu(window)
window.config(menu=menubar)
subMenu = tkinter.Menu(menubar, tearoff=1)
stream = cv2.VideoCapture(filename)

if (stream.isOpened()==False):
    speak("sir you have not selected a file or the format isn't correct")
# print("i am only using videos folders file, and the file name wil be clip.mp4")
# osm = "C:/Users/Brijendra singh/Videos/clip.mp4"

def console():
    speak("cleaning console")
    time.sleep(1)
    os.system("cls")
    speak("console cleared")

flag = True
def change_file():
    global stream
    filename = filedialog.askopenfilename(initialfile = "clip", title = "select a match mp4 file", filetype= (("mp4", "*.mp4"), ("All files", "*.*")))
    window.title(f"Third Umpire Decision Review Kit ({filename})")  
    stream = cv2.VideoCapture(filename)

    if (stream.isOpened()==False):
        speak("sir no file selected")

def play(speed):
    try:
        global flag
        print(f"You clicked on play. Speed is {speed}")

        # Play the video in reverse mode
        frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
        stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

        grabbed, frame = stream.read()
        # if not grabbed:
        #     messagebox.showinfo("error", "sir the video is ended")
        #     change_file()
        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
        if flag:
            canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
        flag = not flag

    except AttributeError as shapee:
        messagebox.showinfo("error", "sir the video is ended")
        print("The vide is ended")
        speak("The vide is ended")
        change_file()

def play5(event):
    try:
        global flag
        print("You clicked on play. Speed is 5")

        # Play the video in reverse mode
        frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
        stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + 5)

        grabbed, frame = stream.read()
        # if not grabbed:
        #     change_file()
        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
        if flag:
            canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
        flag = not flag
    except AttributeError as shapee:
        messagebox.showinfo("error", "sir the video is ended")
        print("The vide is ended")
        speak("The vide is ended")
        change_file()

def playmin5(event):
    try:
        global flag
        print("You clicked on play. Speed is -5")

        # Play the video in reverse mode
        frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
        stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + -5)

        grabbed, frame = stream.read()
        # if not grabbed:
        #     change_file()
        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
        if flag:
            canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
        flag = not flag
    except AttributeError as shapee:
        messagebox.showinfo("error", "sir the video is ended")
        print("The vide is ended")
        speak("The vide is ended")
        change_file()

def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("dpending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
    time.sleep(1.5)

    # 3. Display sponsor image
    frame = cv2.cvtColor(cv2.imread("sponser2.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
    time.sleep(2.5)
    # 5. Display out/notout image
    if decision == 'out':
        decisionImg = "out.jpg  "
    elif decision == 'not out':
        decisionImg = "lords_notout.png"
    elif decision == 'free hit':
        decisionImg = "lords_freehit.png"
    else:
        decisionImg = "no ball.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")
    speak("Player is out")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")
    speak("Player is not out")

def free_hit():
    thread = threading.Thread(target=pending, args=("free hit",))
    thread.daemon = 1
    thread.start()
    print("free hit")
    speak("free hit")

def no_ball():
    thread = threading.Thread(target=pending, args=("no_ball",))
    thread.daemon = 1
    thread.start()
    print("no_ball")
    speak("no ball")

def recoder():
    Driver_Cam.opencam()

def fullscreen():
    window.attributes("-fullscreen", True)

def exitfullscreen():
    window.attributes("-fullscreen", False)

def fullscreen1(event):
    window.attributes("-fullscreen", True)

def exitfullscreen1(event):
    window.attributes("-fullscreen", False)

def color():
    color1 = colorchooser.askcolor()
    window.configure(bg=color1[1])
    print("the color you choose",color1)

def color2(event):
    color1 = colorchooser.askcolor()
    window.configure(bg=color1[1])
    print("the color you choose",color1)


def youtubedowload():
    messagebox.showinfo('info', 'check your console')
    youtube.youtubedow()

def zoom():
    os.startfile("C:/Users/Brijendra singh/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessibility/Magnify.lnk")

def changeframebckground():
    colorc = colorchooser.askcolor()
    canvas.configure(bg=colorc[1])
    print("the color you choose ",colorc)

def changeframebckground3(event):
    colorc = colorchooser.askcolor()
    canvas.configure(bg=colorc[1])
    print("the color you choose ",colorc)

def msg(win, obj, msg):
    pass
window.bind('<Right>', play5)
window.bind('<Left>', playmin5)
window.bind('<f>', fullscreen1)
window.bind('<Escape>', exitfullscreen1)
window.bind("<Control-w>", color2)
window.bind("<Control-f>", changeframebckground3)
# Width and height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368

# Tkinter gui starts here
cv_img = cv2.cvtColor(cv2.imread("sponser1.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.grid(column=2)

def keyboard():
    sortcut.app()

my_canvas = Canvas(window)
main_frame = tkinter.Frame(my_canvas).grid(column=2)
# *********************************menu
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=change_file)
subMenu.add_separator()
subMenu.add_command(label="clean console", command=console)
subMenu.add_command(label="keyboard sortcut", command=keyboard)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=window.destroy)
subMenu = tkinter.Menu(menubar, tearoff=1)
menubar.add_cascade(label="payback", menu=subMenu)
subMenu.add_command(label="min speed -500", command=partial(play, -500))
subMenu.add_command(label="speed -100", command=partial(play, -100))
subMenu.add_command(label="speed -50", command=partial(play, -50))
subMenu.add_command(label="speed -10", command=partial(play, -10))
subMenu.add_command(label="speed -1", command=partial(play, -1))
subMenu.add_command(label="speed 1", command=partial(play, 1))
subMenu.add_command(label="speed 10", command=partial(play, 10))
subMenu.add_command(label="speed 50", command=partial(play, 50))
subMenu.add_command(label="speed 100", command=partial(play, 100))
subMenu.add_command(label="max speed 500", command=partial(play, 500))
# ************************************submenu
# Buttons to control playback
# ******8888sortcutt
btn = tkinter.Button(main_frame, text="<< Previous (fast)", width=30, command=partial(play, -25))
btn.grid()

btn = tkinter.Button(main_frame, text="<<< Previous (very fast)", width=30, command=partial(play, -50))
btn.grid()

btn = tkinter.Button(main_frame, text="< Previous (slow)", width=30, command=partial(play, -2))
btn.grid()

btn = tkinter.Button(main_frame, text="Next (slow) >", width=30, command=partial(play, 1))
btn.grid()

btn = tkinter.Button(main_frame, text="Next (fast) >>", width=30, command=partial(play, 25))
btn.grid()

btn = tkinter.Button(main_frame, text="Next (very fast) >>>", width=30, command=partial(play, 50))
btn.grid()

btn = tkinter.Button(main_frame, text="Give Out", width=30, command=out)
btn.grid()

btn = tkinter.Button(main_frame, text="Give free hit", width=30, command=free_hit)
btn.grid()

btn = tkinter.Button(main_frame, text="Give no ball", width=30, command=no_ball)
btn.grid()

btn = tkinter.Button(main_frame, text="Give Not Out", width=30, command=not_out)
btn.grid()

btn = tkinter.Button(main_frame, text="change file", width=30, command=change_file)
btn.grid(row=1,column=1)

btn = tkinter.Button(main_frame, text="clean console", width=30, command=console)
btn.grid(row=2,column=1)

btn = tkinter.Button(main_frame, text="full 100 speed", width=30, command=partial(play, 100))
btn.grid(row=3,column=1)

btn = tkinter.Button(main_frame, text="open Driver cam", width=30, command=recoder)
btn.grid(row=4, column=1)

btn = tkinter.Button(main_frame, text="full screen", width=30, command=fullscreen)
btn.grid(row=5, column=1)

btn = tkinter.Button(main_frame, text="exit full screen", width=30, command=exitfullscreen)
btn.grid(row=6, column=1)

btn = tkinter.Button(main_frame, text="change window color", width=30, command=color)
btn.grid(row=7, column=1)

btn = tkinter.Button(main_frame, text="change frame color", width=30, command=changeframebckground)
btn.grid(row=8, column=1)

btn = tkinter.Button(main_frame, text="youtube dowloader", width=30, command=youtubedowload)
btn.grid(row=9, column=1)

btn = tkinter.Button(main_frame, text="zoom", width=30, command=zoom)
btn.grid(row=10, column=1)

m = tkinter.Menu(window, tearoff = 0)
m.add_command(label ="change file", command=change_file)
m.add_command(label ="clean console", command=console)
m.add_command(label ="full screen", command=fullscreen)
m.add_command(label ="exit full screen", command=exitfullscreen)
m.add_command(label ="change window color", command=color)
m.add_command(label ="change frame color", command=changeframebckground)

def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

status = tkinter.Label(window, text=f"file name: {filename}")
status.grid(column=1, columnspan=3)
# binding mouse right button to root
window.bind("<Button-3>", do_popup)
window.mainloop()