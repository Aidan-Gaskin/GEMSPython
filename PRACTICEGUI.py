#GUI practice stuff


import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("G.E.M.S - Gaskin Enterprise Management System")
        self.window.geometry("900x600")
        self.crudButtons = [] #this allows the buttons to be destroyed

##CREATING CRUD BUTTONS-------------------------------------------------------------------------------------------------
    def createCrudButtons(self):
        print("Creating CRUD buttons")
        if self.crudButtons:
            for but in self.crudButtons:
                but.destroy()
        createButton = tk.Button(self.window, text="Create", font=("Ariel", 20), width=12, height=4
                                 ,command=self.createButtonClicked)
        updateButton = tk.Button(self.window, text="Update", font=("Ariel", 20), width=12)
        deleteButton = tk.Button(self.window, text="Delete", font=("Ariel", 20), width=12)
        refreshButton = tk.Button(self.window, text="Refresh", font=("Ariel", 20), width=12)
        self.crudButtons = [createButton, updateButton, deleteButton, refreshButton]
        for but in self.crudButtons:
            but.pack(side="left", fill="both", expand=True, padx=5, pady=5, anchor="nw")

##VIEW BUTTON HANDLERS--------------------------------------------------------------------------------------------------
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

##CREATE BUTTON HANDLER-------------------------------------------------------------------------------------------------
    def createButtonClicked(self):
        print("create button pressed")
        create_window = tk.Toplevel(self.window)
        create_window.title("Create Item")
        #
        description_input = tk.Entry(create_window)
        supplierID_input = tk.Entry(create_window)
        buyPrice_input = tk.Entry(create_window)
        sellPrice_input = tk.Entry(create_window)
        #
        def ok_button_clicked():
            #HERE IS WHERE I WILL CALL THE DATABASE METHODS WITH GIVEN INPUT
            input_data = [description_input.get(), supplierID_input.get(), buyPrice_input.get(), sellPrice_input.get()]
            print("User entered:", input_data)
            create_window.destroy()
            #
        ok_button = tk.Button(create_window, text="OK", command=ok_button_clicked)
        #
        cancel_button = tk.Button(create_window, text="Cancel", command=create_window.destroy)
        #
        description_input.pack()
        supplierID_input.pack()
        buyPrice_input.pack()
        sellPrice_input.pack()
        ok_button.pack()
        cancel_button.pack()

    ##CREATING INITIAL GUI VIEW---------------------------------------------------------------------------------------------
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