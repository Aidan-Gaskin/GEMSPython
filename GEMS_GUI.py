import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("G.E.M.S - Gaskin Enterprise Management System")
        self.window.geometry("900x600")
        self.crudButtons = [] #this allows the buttons to be destroyed
        self.pageNum = 0

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
       #creating a variable to check which page we clicked on to manage the crud operations
       self.pageNum = 1
    def viewClientButtonClicked(self):
       print("Pressed: View Client")
       self.createCrudButtons()
       self.pageNum = 2
    def viewAccountManagerButtonClicked(self):
       print("Pressed: View AccountManager")
       self.createCrudButtons()
       self.pageNum = 3
    def viewAdministratorButtonClicked(self):
       print("Pressed: View Administrator")
       self.createCrudButtons()
       self.pageNum = 4
    def viewOrderButtonClicked(self):
       print("Pressed: View Order")
       self.createCrudButtons()
       self.pageNum = 5
    def viewSupplierButtonClicked(self):
       print("Pressed: View Supplier")
       self.createCrudButtons()
       self.pageNum = 6

##CREATE BUTTON HANDLER-------------------------------------------------------------------------------------------------
    def createButtonClicked(self):
        if self.pageNum == 1:
            print("create button pressed")
            create_window = tk.Toplevel(self.window)
            create_window.title("Create Item")
            #LABELS FOR INPUT
            description_label = tk.Label(create_window, text="Description")
            supplierID_label = tk.Label(create_window, text="Supplier ID")
            buyPrice_label = tk.Label(create_window, text="Buy Price")
            sellPrice_label = tk.Label(create_window, text="Sell Price")
            #INPUT BOXES
            description_input = tk.Entry(create_window)
            supplierID_input = tk.Entry(create_window)
            buyPrice_input = tk.Entry(create_window)
            sellPrice_input = tk.Entry(create_window)
            #COMBINING LABEL AND INPUT BOXES
            description_label.grid(row=0, column=0)
            description_input.grid(row=0, column=1)
            supplierID_label.grid(row=1, column=0)
            supplierID_input.grid(row=1, column=1)
            buyPrice_label.grid(row=2, column=0)
            buyPrice_input.grid(row=2, column=1)
            sellPrice_label.grid(row=3, column=0)
            sellPrice_input.grid(row=3, column=1)
            def ok_button_clicked():
                #************HERE IS WHERE I WILL CALL THE DATABASE METHODS WITH GIVEN INPUT***************
                input_data = [description_input.get(), supplierID_input.get(), buyPrice_input.get(),
                              sellPrice_input.get()]
                print("User entered:", input_data)
                create_window.destroy()
            ok_button = tk.Button(create_window, text="OK", command=ok_button_clicked)
            cancel_button = tk.Button(create_window, text="Cancel", command=create_window.destroy)
            ok_button.grid(row=4, column=0)
            cancel_button.grid(row=4, column=1)
        elif self.pageNum == 2:
            print("create button pressed")
            create_window = tk.Toplevel(self.window)
            create_window.title("Create Client")
            # LABELS FOR INPUT
            companyName_label = tk.Label(create_window, text="Company Name")
            address_label = tk.Label(create_window, text="Address")
            accountManID_label = tk.Label(create_window, text="accountManagerID")
            forename_label = tk.Label(create_window, text="contactForename")
            surname_label = tk.Label(create_window, text="contactSurname")
            email_label = tk.Label(create_window, text="contactEmail")
            phoneNo_label = tk.Label(create_window, text="contactPhoneNo")
            # INPUT BOXES
            companyName_input = tk.Entry(create_window)
            address_input = tk.Entry(create_window)
            accountManID_input = tk.Entry(create_window)
            forename_input = tk.Entry(create_window)
            surname_input = tk.Entry(create_window)
            email_input = tk.Entry(create_window)
            phoneNo_input = tk.Entry(create_window)
            # COMBINING LABEL AND INPUT BOXES
            companyName_label.grid(row=0, column=0)
            companyName_input.grid(row=0, column=1)
            address_label.grid(row=1, column=0)
            address_input.grid(row=1, column=1)
            accountManID_label.grid(row=2, column=0)
            accountManID_input.grid(row=2, column=1)
            forename_label.grid(row=3, column=0)
            forename_input.grid(row=3, column=1)
            surname_label.grid(row=4, column=0)
            surname_input.grid(row=4, column=1)
            email_label.grid(row=5, column=0)
            email_input.grid(row=5, column=1)
            phoneNo_label.grid(row=6, column=0)
            phoneNo_input.grid(row=6, column=1)
            def ok_button_clicked():
                # ************HERE IS WHERE I WILL CALL THE DATABASE METHODS WITH GIVEN INPUT***************
                input_data = [companyName_input.get(), address_input.get(), accountManID_input.get(),
                              forename_input.get(), surname_input.get(), email_input.get(), phoneNo_input.get()]
                print("User entered:", input_data)
                create_window.destroy()
            ok_button = tk.Button(create_window, text="OK", command=ok_button_clicked)
            cancel_button = tk.Button(create_window, text="Cancel", command=create_window.destroy)
            ok_button.grid(row=7, column=0)
            cancel_button.grid(row=7, column=1)
        elif self.pageNum == 3:
            print("create button pressed")
            create_window = tk.Toplevel(self.window)
            create_window.title("Create Account Manager")
            # LABELS FOR INPUT
            forename_label = tk.Label(create_window, text="forename")
            surname_label = tk.Label(create_window, text="surname")
            phoneNo_label = tk.Label(create_window, text="phoneNo")
            # INPUT BOXES
            forename_input = tk.Entry(create_window)
            surname_input = tk.Entry(create_window)
            phoneNo_input = tk.Entry(create_window)
            # COMBINING LABEL AND INPUT BOXES
            forename_label.grid(row=0, column=0)
            forename_input.grid(row=0, column=1)
            surname_label.grid(row=1, column=0)
            surname_input.grid(row=1, column=1)
            phoneNo_label.grid(row=2, column=0)
            phoneNo_input.grid(row=2, column=1)
            def ok_button_clicked():
                # ************HERE IS WHERE I WILL CALL THE DATABASE METHODS WITH GIVEN INPUT***************
                input_data = [forename_input.get(), surname_input.get(), phoneNo_input.get()]
                print("User entered:", input_data)
                create_window.destroy()
            ok_button = tk.Button(create_window, text="OK", command=ok_button_clicked)
            cancel_button = tk.Button(create_window, text="Cancel", command=create_window.destroy)
            ok_button.grid(row=3, column=0)
            cancel_button.grid(row=3, column=1)
        elif self.pageNum == 4:
            create_window = tk.Toplevel(self.window)
            create_window.title("Create Administrator")
            # LABELS FOR INPUT
            forename_label = tk.Label(create_window, text="forename")
            surname_label = tk.Label(create_window, text="surname")
            phoneNo_label = tk.Label(create_window, text="phoneNo")
            # INPUT BOXES
            forename_input = tk.Entry(create_window)
            surname_input = tk.Entry(create_window)
            phoneNo_input = tk.Entry(create_window)
            # COMBINING LABEL AND INPUT BOXES
            forename_label.grid(row=0, column=0)
            forename_input.grid(row=0, column=1)
            surname_label.grid(row=1, column=0)
            surname_input.grid(row=1, column=1)
            phoneNo_label.grid(row=2, column=0)
            phoneNo_input.grid(row=2, column=1)
            def ok_button_clicked():
                # ************HERE IS WHERE I WILL CALL THE DATABASE METHODS WITH GIVEN INPUT***************
                input_data = [forename_input.get(), surname_input.get(), phoneNo_input.get()]
                print("User entered:", input_data)
                create_window.destroy()
            ok_button = tk.Button(create_window, text="OK", command=ok_button_clicked)
            cancel_button = tk.Button(create_window, text="Cancel", command=create_window.destroy)
            ok_button.grid(row=3, column=0)
            cancel_button.grid(row=3, column=1)
        elif self.pageNum == 5:
            create_window = tk.Toplevel(self.window)
            create_window.title("Create Order")
            # LABELS FOR INPUT
            clientID_label = tk.Label(create_window, text="clientID")
            accoutManID_label = tk.Label(create_window, text="accountManID")
            adminID_label = tk.Label(create_window, text="adminID")
            itemID_label = tk.Label(create_window, text="itemID")
            quantity_label = tk.Label(create_window, text="quantity")
            supplierID_label = tk.Label(create_window, text="supplierID")
            deliveryAddress_label = tk.Label(create_window, text="deliveryAddress")
            # INPUT BOXES
            clientID_input = tk.Entry(create_window)
            accountManID_input = tk.Entry(create_window)
            adminID_input = tk.Entry(create_window)
            itemID_input = tk.Entry(create_window)
            quantity_input = tk.Entry(create_window)
            supplierID_input = tk.Entry(create_window)
            deliveryAddress_input = tk.Entry(create_window)
            # COMBINING LABEL AND INPUT BOXES
            clientID_label.grid(row=0, column=0)
            clientID_input.grid(row=0, column=1)
            accoutManID_label.grid(row=1, column=0)
            accountManID_input.grid(row=1, column=1)
            adminID_label.grid(row=2, column=0)
            adminID_input.grid(row=2, column=1)
            itemID_label.grid(row=3, column=0)
            itemID_input.grid(row=3, column=1)
            quantity_label.grid(row=4, column=0)
            quantity_input.grid(row=4, column=1)
            supplierID_label.grid(row=5, column=0)
            supplierID_input.grid(row=5, column=1)
            deliveryAddress_label.grid(row=6, column=0)
            deliveryAddress_input.grid(row=6, column=1)
            def ok_button_clicked():
                # ************HERE IS WHERE I WILL CALL THE DATABASE METHODS WITH GIVEN INPUT***************
                input_data = [clientID_input.get(), accountManID_input.get(), itemID_input.get(), quantity_input.get(),
                               supplierID_input.get(), deliveryAddress_input.get()]
                print("User entered:", input_data)
                create_window.destroy()
            ok_button = tk.Button(create_window, text="OK", command=ok_button_clicked)
            cancel_button = tk.Button(create_window, text="Cancel", command=create_window.destroy)
            ok_button.grid(row=7, column=0)
            cancel_button.grid(row=7, column=1)
        elif self.pageNum == 6:
            create_window = tk.Toplevel(self.window)
            create_window.title("Create Supplier")
            # LABELS FOR INPUT
            companyName_label = tk.Label(create_window, text="companyName")
            address_label = tk.Label(create_window, text="address")
            forename_label = tk.Label(create_window, text="contactForename")
            surname_label = tk.Label(create_window, text="contactSurname")
            email_label = tk.Label(create_window, text="contactEmail")
            phoneNo_label = tk.Label(create_window, text="contactPhoneNo")
            # INPUT BOXES
            companyName_input = tk.Entry(create_window)
            address_input = tk.Entry(create_window)
            forename_input = tk.Entry(create_window)
            surname_input = tk.Entry(create_window)
            email_input = tk.Entry(create_window)
            phoneNo_input = tk.Entry(create_window)
            # COMBINING LABEL AND INPUT BOXES
            companyName_label.grid(row=0, column=0)
            companyName_input.grid(row=0, column=1)
            address_label.grid(row=1, column=0)
            address_input.grid(row=1, column=1)
            forename_label.grid(row=2, column=0)
            forename_input.grid(row=2, column=1)
            surname_label.grid(row=3, column=0)
            surname_input.grid(row=3, column=1)
            email_label.grid(row=4, column=0)
            email_input.grid(row=4, column=1)
            phoneNo_label.grid(row=5, column=0)
            phoneNo_input.grid(row=5, column=1)
            def ok_button_clicked():
                # ************HERE IS WHERE I WILL CALL THE DATABASE METHODS WITH GIVEN INPUT***************
                input_data = [companyName_input.get(), address_input.get(), forename_input.get(), surname_input.get(),
                              email_input.get(), phoneNo_input.get()]
                print("User entered:", input_data)
                create_window.destroy()
            ok_button = tk.Button(create_window, text="OK", command=ok_button_clicked)
            cancel_button = tk.Button(create_window, text="Cancel", command=create_window.destroy)
            ok_button.grid(row=6, column=0)
            cancel_button.grid(row=6, column=1)









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



        

