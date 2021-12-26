from tkinter import *
import pygame
import math
import time

pygame.init()

# initialize tkinter
root = Tk()
# set window title
root.title("Pomodoro Timer by Munta")
root.iconbitmap("clock.ico")
root.geometry("500x120")


# STUDY SECTION
# Study Label
studyTimeText = Label(root, text="Study Time")
studyTimeText.place(x=120, y=30, anchor="center")

# Hour Label and input for Study
hourStudyLabel = Label(root, text="Hour: ")
hourStudyLabel.place(x=30, y=60, anchor="center")
hourStudyInput = Entry(root)
hourStudyInput.place(x=50, y=53, width=35, height=15)

# Minute Label and input for Study
minuteStudyLabel = Label(root, text="Min: ")
minuteStudyLabel.place(x=110, y=60, anchor="center")
minuteStudyInput = Entry(root)
minuteStudyInput.place(x=130, y=53, width=35, height=15)

# Second Label and input for Study
secondStudyLabel = Label(root, text="Sec: ")
secondStudyLabel.place(x=190, y=60, anchor="center")
secondStudyInput = Entry(root)
secondStudyInput.place(x=210, y=53, width=35, height=15)

# BREAK SECTION
# Study Label
breakTimeText = Label(root, text="Break Time")
breakTimeText.place(x=380, y=30, anchor="center")

# Hour Label and input for Study
hourBreakLabel = Label(root, text="Hour: ")
hourBreakLabel.place(x=280, y=60, anchor="center")
hourBreakInput = Entry(root)
hourBreakInput.place(x=300, y=53, width=35, height=15)

# Minute Label and input for Study
minuteBreakLabel = Label(root, text="Min: ")
minuteBreakLabel.place(x=360, y=60, anchor="center")
minuteBreakInput = Entry(root)
minuteBreakInput.place(x=380, y=53, width=35, height=15)

# Second Label and input for Study
secondBreakLabel = Label(root, text="Sec: ")
secondBreakLabel.place(x=440, y=60, anchor="center")
secondBreakInput = Entry(root)
secondBreakInput.place(x=460, y=53, width=35, height=15)


# Check if inputs are valid
def checkInput():
    # STUDY
    isValidStudy = False
    hourStudy = hourStudyInput.get()
    minuteStudy = minuteStudyInput.get()
    secondStudy = secondStudyInput.get()
    try:
        hourStudy = int(hourStudyInput.get())
        minuteStudy = int(minuteStudyInput.get())
        secondStudy = int(secondStudyInput.get())
    except ValueError:
        isValidStudy = False

    if isinstance(hourStudy, int) is True and isinstance(minuteStudy, int) is True and isinstance(secondStudy, int) is True:
        isValidStudy = True
    else:
        isValidStudy = False

    # BREAK
    isValidBreak = False
    hourBreak = hourBreakInput.get()
    minuteBreak = minuteBreakInput.get()
    secondBreak = secondBreakInput.get()
    try:
        hourBreak = int(hourBreakInput.get())
        minuteBreak = int(minuteBreakInput.get())
        secondBreak = int(secondBreakInput.get())
    except ValueError:
        isValidBreak = False

    if isinstance(hourBreak, int) is True and isinstance(minuteBreak, int) is True and isinstance(secondBreak, int) is True:
        isValidBreak = True
    else:
        isValidBreak = False

    if isValidStudy and isValidBreak:
        hourStudyInput.destroy()
        hourStudyLabel.destroy()
        minuteStudyInput.destroy()
        minuteStudyLabel.destroy()
        secondStudyInput.destroy()
        secondStudyLabel.destroy()

        hourBreakInput.destroy()
        hourBreakLabel.destroy()
        minuteBreakInput.destroy()
        minuteBreakLabel.destroy()
        secondBreakInput.destroy()
        secondBreakLabel.destroy()

        startButton.destroy()
        breakTimeText.destroy()
        studyTimeText.destroy()

        # BEGIN TIMER
        # Study Time in Seconds
        hourStudy = hourStudy * 60 * 60
        minuteStudy = (minuteStudy * 60) + hourStudy
        secondStudy = secondStudy + minuteStudy

        # Break Time in Seconds
        hourBreak = hourBreak * 60 * 60
        minuteBreak = (minuteBreak * 60) + hourBreak
        secondBreak = secondBreak + minuteBreak

        global studyTime
        studyTime = secondStudy
        global breakTime
        breakTime = secondBreak
        countdown(studyTime)

    else:
        print("")


# Button to start Timer
startButton = Button(root, text="Start", command=checkInput)
startButton.place(x=255, y=100, anchor="center")


def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")
    label.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
    label.after(1000, clock)


def countdown(seconds):
    label.pack()
    label.config(fg="black")
    hour = seconds / 3600
    minute = (hour % 1) * 60
    second = (minute % 1) * 60
    hour = math.trunc(hour)
    minute = math.trunc(minute)
    second = round(second)
    timer = '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)
    label.config(text=timer)
    if hour == 0.0 and minute == 0.0 and second == 0.0:
        play()
        pause(breakTime)
    else:
        label.after(1000, lambda: countdown(seconds - 1))


def pause(seconds):
    label.config(fg="red")
    hour = seconds / 3600
    minute = (hour % 1) * 60
    second = (minute % 1) * 60
    hour = math.trunc(hour)
    minute = math.trunc(minute)
    second = round(second)
    timer = '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)
    label.config(text=timer)
    if hour == 0.0 and minute == 0.0 and second == 0.0:
        play()
        countdown(studyTime)
    else:
        label.after(1000, lambda: pause(seconds - 1))


def play():
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()


label = Label(root, text="yes", font=("Source Code Pro", 48), pady=10, fg="blue")
label.pack()
label.pack_forget()

root.mainloop()
