import tkinter
from typing import Text

window = tkinter.Tk()

window.title("Love calculator")

window.geometry("500x500")

Text1 = tkinter.Entry(window,width=15)

Text2 = tkinter.Entry(window,width=15)

def click():

    POINTS = 0

    Love1 = Text1.get()
    Love2 = Text2.get()

    L1 = (len(Love1))
    L2 = (len(Love2))
 
    S1 = (Love1[:1])
    S2 = (Love2[:1])
 
    if L1 == L2:
        POINTS = POINTS + 20
 
    if S1 == "a" or "e" or "i" or "o" or "u":
        POINTS = POINTS + 5
    else:
        POINTS = POINTS + 2.5
    if S2 == "a" or "e" or "i" or "o" or "u":
        POINTS = POINTS + 5
    else:
        POINTS = POINTS + 2.5

    tkinter.Label(window,text= POINTS).pack()

but = tkinter.Button(window,text="love calculator",command=click)

Text1.pack()

Text2.pack()

but.pack()

window.mainloop()