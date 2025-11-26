# main.py
import tkinter as tk
import tkinter.font as tkFont

class Window(tk.Tk):
    def __init__(self, title, size="800x600", can_resize=False):
        super().__init__()
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(family="FixedSys", size=20)
        self.title(title)
        self.geometry(size)
        self.resizable(can_resize,can_resize)
