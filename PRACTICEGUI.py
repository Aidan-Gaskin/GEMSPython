#GUI practice stuff


import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("G.E.M.S - Gaskin Enterprise Management System")
        self.window.geometry("900x600")
        ##Probably won't implement fullscreen. When implemented the 3 top buttons don't appear
        #self.window.attributes('-fullscreen', True)
        # myFrame = tk.Frame(self.window, width=900, height=600)
        # myFrame.pack()

    def viewItemButtonClicked(self):
       print("Pressed: View Item")

    def viewClientButtonClicked(self):
       print("Pressed: View Client")

    def viewAccountManagerButtonClicked(self):
       print("Pressed: View AccountManager")

    def viewAdministratorButtonClicked(self):
       print("Pressed: View Administrator")

    def viewOrderButtonClicked(self):
       print("Pressed: View Order")

    def viewSupplierButtonClicked(self):
       print("Pressed: View Supplier")

    def createGUI(self):
        ##creating the buttons & adding handlers.
        viewItemButton = tk.Button(self.window, text="View: Item",  height=5, width=8,
                                   command=self.viewItemButtonClicked)
        viewClientButton = tk.Button(self.window, text="View: Client", height=5, width=8,
                                     command=self.viewClientButtonClicked)
        viewAccountManagerButton = tk.Button(self.window, text="View: AccountManager", height=5, width=8,
                                             command=self.viewAccountManagerButtonClicked)
        viewAdministratorButton = tk.Button(self.window, text="View: Administrator", height=5, width=8,
                                            command=self.viewAdministratorButtonClicked)
        viewOrderButton = tk.Button(self.window, text="View: Order", height=5, width=8,
                                    command=self.viewOrderButtonClicked)
        viewSupplierButton = tk.Button(self.window, text="View: Supplier", height=5, width=8,
                                       command=self.viewSupplierButtonClicked)

        # Button(win, text="Button-1", height=5, width=10).pack()

        ##Creating list of the buttons for looping through later on
        buttonList = [viewItemButton,viewClientButton,viewAccountManagerButton,
                      viewAdministratorButton, viewOrderButton, viewSupplierButton]
        ##Positioning Buttons
        # for butt in buttonList:
        #     butt



        ##Packs all buttons to screen in one logic block instead of multiple statements
        for butt in buttonList:
            butt.pack()
        self.window.mainloop()


#call this stuff within the "Main" file later when finalising - Aidan Gaskin
gui = GUI()
gui.createGUI()