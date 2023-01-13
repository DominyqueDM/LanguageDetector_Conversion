#This is a simple language detector done in python
#This uses the module: langdetect --> pip install langdetect
#Also uses tkinter for GUI

from langdetect import detect
from googletrans import Translator, constants
import tkinter as tk

def detect_language():
    window = tk.Tk()
    translator = Translator()
    window.geometry('600x400')
    heading = tk.Label(window, text='Simple Language Detector', font=('Calibri 15'))
    heading.pack(pady=25)

    def check_language():
        user_input = text.get()
        lang = detect(str(user_input))
        tk.Label(window, text=lang.upper(), font=('Calibri 15 bold')).place(x=280, y=200)
        translation = translator.translate(str(user_input))
        tk.Label(window, text='Below is the translation of your sentence to English!', fon=('Calabri 15')).place(x=80, y=230)
        tk.Label(window, text={translation.text}, font=('Calibri 15')).place(x=180, y= 260)

    text = tk.StringVar()
    tk.Label(window, text='Please type and enter any sentence in any language you choose.', font=('Calabri 15')).place(x=20, y=60)
    tk.Entry(window, textvariable=text).place(x=160, y=100, height=30, width=280)
    tk.Button(window, text='Check Language', command=check_language).place(x=250, y=150)
    window.mainloop()


if __name__ == '__main__':
    detect_language()
