from pygame import mixer
from tkinter import *
root=Tk()


mixer.init()
mixer.music.load('ringtone_kbc.mp3')
mixer.music.play()

root.mainloop()