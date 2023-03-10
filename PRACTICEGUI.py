#GUI practice stuff


import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("G.E.M.S - Gaskin Enterprise Management System")
        self.window.geometry("300x200")
        self.window.attributes('-fullscreen', True)

    def button_clicked(self):
       print("Button clicked!")

    def createGUI(self):
        button = tk.Button(self.window, text="Click me!", command=self.button_clicked)
        button.pack()
        self.window.mainloop()


#call this stuff within the "Main" file later when finalising - Aidan Gaskin
gui = GUI()
gui.createGUI()