from tkinter import ttk

from Defination import DefinationsEveryting


def clicked_rf1():
    print("clll")
    if DefinationsEveryting.togglebuttons['text'] == "Open":
        DefinationsEveryting.togglebuttons.configure(text="Close")
    elif DefinationsEveryting.togglebuttons['text'] == "Close":
        DefinationsEveryting.togglebuttons.configure(text="Open")
