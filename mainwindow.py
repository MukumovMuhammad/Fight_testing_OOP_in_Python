# main.py
import tkinter as tk
import tkinter.font as tkFont


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(family="FixedSys", size=15)
        self.title("Main Window")
        self.geometry("800x600")
        self.resizable(0,0)
        self.label = tk.Label(self, text="Welcome to Main!")
        self.label.pack(pady=20)
        self.open_button = tk.Button(self, text="Open Other Window", command=self.open_other_window)
        self.open_button.pack(pady=10)

    def open_other_window(self):
        other_window = OtherWindow(self, self.update_main_label) 

    def update_main_label(self, message):
        self.label.config(text=f"Returned from Other: {message}")

class OtherWindow(tk.Toplevel):
    def __init__(self, master, callback_function):
        super().__init__(master)
        self.title("Other Window")
        self.callback_function = callback_function # Store the callback
        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)
        self.submit_button = tk.Button(self, text="Submit", command=self.on_submit)
        self.submit_button.pack(pady=5)

    def on_submit(self):
        data = self.entry.get()
        self.callback_function(data)
        self.destroy()
