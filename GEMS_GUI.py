import tkinter as tk
from tkinter import ttk
from GEMS import GEMS
class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("G.E.M.S - Gaskin Enterprise Management System")
        self.window.geometry("900x600")
        self.crudButtons = [] #this allows the buttons to be destroyed
        self.pageNum = 0
        self.gems = GEMS()
##CREATING CRUD BUTTONS-------------------------------------------------------------------------------------------------
    def createCrudButtons(self):
        print("Creating CRUD buttons")
        if self.crudButtons:
            for but in self.crudButtons:
                but.destroy()
        createButton = tk.Button(self.window, text="Create", font=("Ariel", 20), width=12, height=4,
                                 command=self.createButtonClicked)
        updateButton = tk.Button(self.window, text="Update", font=("Ariel", 20), width=12,
                                 command=self.updateButtonClicked)
        deleteButton = tk.Button(self.window, text="Delete", font=("Ariel", 20), width=12,
                                 command=self.deleteButtonClicked)
        refreshButton = tk.Button(self.window, text="Refresh", font=("Ariel", 20), width=12,
                                  command=self.refreshButtonClicked)
        self.crudButtons = [createButton, updateButton, deleteButton, refreshButton]
        for but in self.crudButtons:
            but.pack(side="left", fill="both", expand=True, padx=5, pady=5, anchor="nw")
##VIEW BUTTON HANDLERS--------------------------------------------------------------------------------------------------
    def viewItemButtonClicked(self):
       print("Pressed: View Item")
       self.createCrudButtons()
       #creating a variable to check which page we clicked on to manage the crud operations
       self.pageNum = 1
       #delete any Treeviews that exists before the method call
       for widget in self.window.winfo_children():
           if isinstance(widget, ttk.Treeview):
               widget.destroy()
       #Creating the Treeview component
       itemTree = ttk.Treeview(self.window)
       itemTree["columns"] = ("description", "supplierID", "buyPrice", "sellPrice")
       itemTree.heading("#0", text="Item ID")
       itemTree.column("#0", width=100)
       itemTree.heading("description", text="Description")
       itemTree.column("description", width=300)
       itemTree.heading("supplierID", text="Supplier ID")
       itemTree.column("supplierID", width=100)
       itemTree.heading("buyPrice", text="Buy Price")
       itemTree.column("buyPrice", width=100)
       itemTree.heading("sellPrice", text="Sell Price")
       itemTree.column("sellPrice", width=100)
       #Get SQL table data and transfer into component
       cursor = GEMS.connection.cursor()
       cursor.execute("SELECT * FROM Item")
       rows = cursor.fetchall()
       for row in rows:
           itemTree.insert("", "end", text=row[0], values=row[1:])
       #Center the table
       itemTree.place(relx=0.5, rely=0.5, anchor="center")
    def viewClientButtonClicked(self):
       print("Pressed: View Client")
       self.createCrudButtons()
       self.pageNum = 2
       for widget in self.window.winfo_children():
           if isinstance(widget, ttk.Treeview):
               widget.destroy()
       clientTree = ttk.Treeview(self.window)
       clientTree["columns"] = ("companyName", "address", "accountManagerID", "contactForename",
                              "contactSurname", "contactEmail", "contactPhoneNo")
       clientTree.heading("#0", text="clientID")
       clientTree.column("#0", width=100)
       clientTree.heading("companyName", text="companyName")
       clientTree.column("companyName", width=300)
       clientTree.heading("address", text="address")
       clientTree.column("address", width=100)
       clientTree.heading("accountManagerID", text="accountmanagerID")
       clientTree.column("accountManagerID", width=100)
       clientTree.heading("contactForename", text="contactForename")
       clientTree.column("contactForename", width=100)
       clientTree.heading("contactSurname", text="contactSurname")
       clientTree.column("contactSurname", width=100)
       clientTree.heading("contactEmail", text="contactEmail")
       clientTree.column("contactEmail", width=100)
       clientTree.heading("contactPhoneNo", text="contactPhoneNo")
       clientTree.column("contactPhoneNo", width=100)
       cursor = GEMS.connection.cursor()
       cursor.execute("SELECT * FROM Client")
       rows = cursor.fetchall()
       for row in rows:
           clientTree.insert("", "end", text=row[0], values=row[1:])
       clientTree.place(relx=0.5, rely=0.5, anchor="center")
    def viewAccountManagerButtonClicked(self):
       print("Pressed: View AccountManager")
       self.createCrudButtons()
       self.pageNum = 3
       for widget in self.window.winfo_children():
           if isinstance(widget, ttk.Treeview):
               widget.destroy()
       accTree = ttk.Treeview(self.window)
       accTree["columns"] = ("forename", "surname", "phoneNo")
       accTree.heading("#0", text="accountManID")
       accTree.column("#0", width=100)
       accTree.heading("forename", text="forename")
       accTree.column("forename", width=300)
       accTree.heading("surname", text="surname")
       accTree.column("surname", width=100)
       accTree.heading("phoneNo", text="phoneNo")
       accTree.column("phoneNo", width=100)
       cursor = GEMS.connection.cursor()
       cursor.execute("SELECT * FROM AccountManager")
       rows = cursor.fetchall()
       for row in rows:
           accTree.insert("", "end", text=row[0], values=row[1:])
       accTree.place(relx=0.5, rely=0.5, anchor="center")
    def viewAdministratorButtonClicked(self):
       print("Pressed: View Administrator")
       self.createCrudButtons()
       self.pageNum = 4
       for widget in self.window.winfo_children():
           if isinstance(widget, ttk.Treeview):
               widget.destroy()
       adminTree = ttk.Treeview(self.window)
       adminTree["columns"] = ("forename", "surname", "phoneNo")
       adminTree.heading("#0", text="adminID")
       adminTree.column("#0", width=100)
       adminTree.heading("forename", text="forename")
       adminTree.column("forename", width=300)
       adminTree.heading("surname", text="surname")
       adminTree.column("surname", width=100)
       adminTree.heading("phoneNo", text="phoneNo")
       adminTree.column("phoneNo", width=100)
       cursor = GEMS.connection.cursor()
       cursor.execute("SELECT * FROM Administrator")
       rows = cursor.fetchall()
       for row in rows:
           adminTree.insert("", "end", text=row[0], values=row[1:])
       adminTree.place(relx=0.5, rely=0.5, anchor="center")
    def viewOrderButtonClicked(self):
       print("Pressed: View Order")
       self.createCrudButtons()
       self.pageNum = 5
       for widget in self.window.winfo_children():
           if isinstance(widget, ttk.Treeview):
               widget.destroy()
       orderTree = ttk.Treeview(self.window)
       orderTree["columns"] = ("clientID", "accountManID", "adminID", "itemID",
                              "quantity", "supplierID", "deliveryAddress")
       orderTree.heading("#0", text="orderID")
       orderTree.column("#0", width=125)
       orderTree.heading("clientID", text="clientID")
       orderTree.column("clientID", width=125)
       orderTree.heading("accountManID", text="accountManID")
       orderTree.column("accountManID", width=125)
       orderTree.heading("adminID", text="adminID")
       orderTree.column("adminID", width=125)
       orderTree.heading("itemID", text="itemID")
       orderTree.column("itemID", width=125)
       orderTree.heading("quantity", text="quantity")
       orderTree.column("quantity", width=125)
       orderTree.heading("supplierID", text="supplierID")
       orderTree.column("supplierID", width=125)
       orderTree.heading("deliveryAddress", text="deliveryAddress")
       orderTree.column("deliveryAddress", width=125)
       cursor = GEMS.connection.cursor()
       cursor.execute("SELECT * FROM gemsDB.Order")
       rows = cursor.fetchall()
       for row in rows:
           orderTree.insert("", "end", text=row[0], values=row[1:])
       orderTree.place(relx=0.5, rely=0.5, anchor="center")
    def viewSupplierButtonClicked(self):
       print("Pressed: View Supplier")
       self.createCrudButtons()
       self.pageNum = 6
       for widget in self.window.winfo_children():
           if isinstance(widget, ttk.Treeview):
               widget.destroy()
       supTree = ttk.Treeview(self.window)
       supTree["columns"] = ("companyName", "address", "contactForename",
                              "contactSurname", "contactEmail", "contactPhoneNo")
       supTree.heading("#0", text="supplierID")
       supTree.column("#0", width=100)
       supTree.heading("companyName", text="companyName")
       supTree.column("companyName", width=300)
       supTree.heading("address", text="address")
       supTree.column("address", width=100)
       supTree.heading("contactForename", text="contactForename")
       supTree.column("contactForename", width=100)
       supTree.heading("contactSurname", text="contactSurname")
       supTree.column("contactSurname", width=100)
       supTree.heading("contactEmail", text="contactEmail")
       supTree.column("contactEmail", width=100)
       supTree.heading("contactPhoneNo", text="contactPhoneNo")
       supTree.column("contactPhoneNo", width=100)
       cursor = GEMS.connection.cursor()
       cursor.execute("SELECT * FROM Client")
       rows = cursor.fetchall()
       for row in rows:
           supTree.insert("", "end", text=row[0], values=row[1:])
       supTree.place(relx=0.5, rely=0.5, anchor="center")

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
                self.gems.createItemObject(description_input.get(), supplierID_input.get(),
                                      buyPrice_input.get(), sellPrice_input.get())
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
                self.gems.createClientObject(companyName_input.get(), address_input.get(), accountManID_input.get(),
                                             forename_input.get(), surname_input.get(),
                                             email_input.get(), phoneNo_input.get())
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
                self.gems.createAccountManagerObject(forename_input.get(), surname_input.get(),
                                                     phoneNo_input.get())
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
                self.gems.createAdministratorObject(forename_input.get(), surname_input.get(),
                                                    phoneNo_input.get())
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
                self.gems.createOrderObject(clientID_input.get(), accountManID_input.get(),adminID_input.get(),
                                            itemID_input.get(), quantity_input.get(), supplierID_input.get(),
                                            deliveryAddress_input.get())
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
                self.gems.createSupplierObject(companyName_input.get(), address_input.get(), forename_input.get(),
                                               surname_input.get(), email_input.get(), phoneNo_input.get())
                create_window.destroy()
            ok_button = tk.Button(create_window, text="OK", command=ok_button_clicked)
            cancel_button = tk.Button(create_window, text="Cancel", command=create_window.destroy)
            ok_button.grid(row=6, column=0)
            cancel_button.grid(row=6, column=1)
    ##REFRESH HANDLER---------------------------------------------------------------------------------------------
    def refreshButtonClicked(self):
        print("refresh button clicked")
        for widget in self.window.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()
        if self.pageNum == 1:
            self.viewItemButtonClicked()
        elif self.pageNum == 2:
            self.viewClientButtonClicked()
        elif self.pageNum == 3:
            self.viewAccountManagerButtonClicked()
        elif self.pageNum == 4:
            self.viewAdministratorButtonClicked()
        elif self.pageNum == 5:
            self.viewOrderButtonClicked()
        elif self.pageNum == 6:
            self.viewSupplierButtonClicked()
    ##CREATING INITIAL GUI VIEW---------------------------------------------------------------------------------------------
    def updateButtonClicked(self):
        print("update button clicked")
        update_window = tk.Toplevel(self.window)
        update_window.title("Update Entry")

        # LABELS FOR INPUT
        tableToUpdate_label = tk.Label(update_window, text="Table To Update:")
        fieldToUpdate_label = tk.Label(update_window, text="The Field To Update:")
        newValue_label = tk.Label(update_window, text="The New Value:")
        firstField_label = tk.Label(update_window, text="First Field (<table>ID):")
        firstFieldValue_lable = tk.Label(update_window, text="First Field Value (<table>ID = ?:")
        # INPUT BOXES
        tableToUpdate_input = tk.Entry(update_window)
        fieldToUpdate_input = tk.Entry(update_window)
        newValue_input = tk.Entry(update_window)
        firstField_input = tk.Entry(update_window)
        firstFieldValue_input = tk.Entry(update_window)

        tableToUpdate_label.grid(row=0, column=0)
        tableToUpdate_input.grid(row=0, column=1)
        fieldToUpdate_label.grid(row=1, column=0)
        fieldToUpdate_input.grid(row=1, column=1)
        newValue_label.grid(row=2, column=0)
        newValue_input.grid(row=2, column=1)
        firstField_label.grid(row=3, column=0)
        firstField_input.grid(row=3, column=1)
        firstFieldValue_lable.grid(row=4, column=0)
        firstFieldValue_input.grid(row=4, column=1)
        def ok_button_clicked():
            self.gems.updateEntry(tableToUpdate_input.get(), fieldToUpdate_input.get(), newValue_input.get(),
                                  firstField_input.get(), firstFieldValue_input.get())
            update_window.destroy()
        ok_button = tk.Button(update_window, text="OK", command=ok_button_clicked)
        cancel_button = tk.Button(update_window, text="Cancel", command=update_window.destroy)
        ok_button.grid(row=5, column=0)
        cancel_button.grid(row=5, column=1)
    ##CREATING INITIAL GUI VIEW---------------------------------------------------------------------------------------------
    def deleteButtonClicked(self):
        print("delete button clicked")
        delete_window = tk.Toplevel(self.window)
        delete_window.title("Delete Entry")
        table_label = tk.Label(delete_window, text="Table:")
        field_label = tk.Label(delete_window, text="Field:")
        value_label = tk.Label(delete_window, text="Value:")
        table_entry = tk.Entry(delete_window)
        field_entry = tk.Entry(delete_window)
        value_entry = tk.Entry(delete_window)
        table_label.grid(row=0, column=0)
        table_entry.grid(row=0, column=1)
        field_label.grid(row=1, column=0)
        field_entry.grid(row=1, column=1)
        value_label.grid(row=2, column=0)
        value_entry.grid(row=2, column=1)
        def ok_button_clicked():
            self.gems.deleteRow(table_entry.get(), field_entry.get(), value_entry.get())
            delete_window.destroy()
        ok_button = tk.Button(delete_window, text="OK", command=ok_button_clicked)
        cancel_button = tk.Button(delete_window, text="Cancel", command=delete_window.destroy)
        ok_button.grid(row=3, column=0)
        cancel_button.grid(row=3, column=1)

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
# gui = GUI()
# gui.createGUI()



        

