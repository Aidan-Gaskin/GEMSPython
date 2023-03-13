#GUI practice stuff


import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("G.E.M.S - Gaskin Enterprise Management System")
        self.window.geometry("900x600")
        self.crudButtons = [] #this allows the buttons to be destroyed
        ##Probably won't implement fullscreen. When implemented the 3 top buttons don't appear
        #self.window.attributes('-fullscreen', True)
        # myFrame = tk.Frame(self.window, width=900, height=600)
        # myFrame.pack()

    def createCrudButtons(self):
        print("Creating CRUD buttons")
        if self.crudButtons:
            for but in self.crudButtons:
                but.destroy()
        createButton = tk.Button(self.window, text="Create", font=("Ariel", 20), width=12, height=4)
        updateButton = tk.Button(self.window, text="Update", font=("Ariel", 20), width=12)
        deleteButton = tk.Button(self.window, text="Delete", font=("Ariel", 20), width=12)
        refreshButton = tk.Button(self.window, text="Refresh", font=("Ariel", 20), width=12)
        self.crudButtons = [createButton, updateButton, deleteButton, refreshButton]
        for but in self.crudButtons:
            but.pack(side="left", fill="both", expand=True, padx=5, pady=5, anchor="nw")

    def viewItemButtonClicked(self):
       print("Pressed: View Item")
       self.createCrudButtons()

    def viewClientButtonClicked(self):
       print("Pressed: View Client")
       self.createCrudButtons()

    def viewAccountManagerButtonClicked(self):
       print("Pressed: View AccountManager")
       self.createCrudButtons()

    def viewAdministratorButtonClicked(self):
       print("Pressed: View Administrator")
       self.createCrudButtons()

    def viewOrderButtonClicked(self):
       print("Pressed: View Order")
       self.createCrudButtons()

    def viewSupplierButtonClicked(self):
       print("Pressed: View Supplier")
       self.createCrudButtons()

    def createGUI(self):
        ##creating the buttons & adding handlers.
        viewItemButton = tk.Button(self.window,text="View: \nItem",font=("Ariel",20),width=12,
                                   command=self.viewItemButtonClicked)
        viewClientButton = tk.Button(self.window,text="View: \nClient",font=("Ariel",20),width=12,
                                     command=self.viewClientButtonClicked)
        viewAccountManagerButton = tk.Button(self.window,text="View: \nAccountManager",font=("Ariel",20),width=12,
                                             command=self.viewAccountManagerButtonClicked)
        viewAdministratorButton = tk.Button(self.window,text="View: \nAdministrator",font=("Ariel",20),width=12,
                                            command=self.viewAdministratorButtonClicked)
        viewOrderButton = tk.Button(self.window,text="View: \nOrder",font=("Ariel",20), width=12,
                                    command=self.viewOrderButtonClicked)
        viewSupplierButton = tk.Button(self.window,text="View: \nSupplier",font=("Ariel",20),width=12,
                                       command=self.viewSupplierButtonClicked)

        # Button(win, text="Button-1", height=5, width=10).pack()

        ##Creating list of the buttons for looping through later on
        buttonList = [viewItemButton,viewClientButton,viewAccountManagerButton,
                      viewAdministratorButton, viewOrderButton, viewSupplierButton]



        ##Packs all buttons to screen in one logic block instead of multiple statements
        for butt in buttonList:
            butt.pack(side="top",fill="y",expand=True,padx=5,pady=5,anchor="nw")


        self.window.mainloop()


#call this stuff within the "Main" file later when finalising - Aidan Gaskin
gui = GUI()
gui.createGUI()