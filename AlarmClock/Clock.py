import time as tm
import os
import tkinter as tk
from tkinter import *
from pygame import mixer
mixer.init()
def getfromfile(rootdir,e):
    filelist = []
    counter = 1
    for root, directories, filenames in os.walk(rootdir):
        for filename in filenames:
            if any(ext in filename for ext in e):
                filelist.append(os.path.join(root, filename))
                counter += 1
    return filelist
def Stop():
    mixer.music.stop()
    sleep['state']=DISABLED
def settune(clicked):
    mixer.music.load(clicked)
def PlayMusic():
    mixer.music.play(-1)
    sleep['state'] = NORMAL
def AlarmClock():
    clock = tk.Label(window, width=5, font=('OCR A Extended', 80, 'bold'),bg="white", fg='blue')
    clock.place(x=80,y=50)
    currentTime = tm.strftime('%H:%M:%S')
    ct = tm.strftime('%H:%M')
    clock['text'] = ct
    if (currentTime == inputtxt.get()+':00'):
        PlayMusic()
    window.after(1000,AlarmClock)
window = tk.Tk()
Music=getfromfile('music','mp3')
mixer.music.load(Music[0])
clicked = StringVar()
clicked.set(Music[0])
window.config(bg="navy")
window.geometry("500x250")
window.title('Alarm Clock')
sleep = tk.Button(window, text="Stop Alarm", width=40,state=DISABLED, bg='white', command=Stop)
sleep.place(x=95, y=180)
inputtxt = tk.Entry(window)
inputtxt.place(x=175,y=30)
lbl=tk.Label(window,bg="navy",fg='white',text='Enter time in 24 hour notation').place(x=175,y=5)
lbl2=tk.Label(window,bg="navy",fg='white',text='Select tone:').place(x=10,y=210)
drop = OptionMenu(window,clicked,*Music,command=settune)
drop.place(x=80,y=210)
AlarmClock()
window.mainloop()



