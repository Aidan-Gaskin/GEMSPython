#GEMS GUI FILE 
import tkinter as tk
from tkinter import ttk

class GEMS_GUI:
    def init(self):
    # Main Frame
    self.gems = tk.Tk()
    self.gems.title("G.E.M.S - Gaskin Enterprise Management System")
    # Main Frame Menu Bar
    self.gemsMenuBar = tk.Menu(self.gems)
    self.gemsMENU = tk.Menu(self.gemsMenuBar, tearoff=0)
    self.gemsMENU.add_command(label="TBC", command=self.tbc)
    self.gemsMENU.add_command(label="TBC", command=self.tbc)
    self.gemsHELP = tk.Menu(self.gemsMenuBar, tearoff=0)
    self.gemsHELP.add_command(label="TBC", command=self.tbc)
    self.gemsHELP.add_command(label="TBC", command=self.tbc)
    self.gemsMenuBar.add_cascade(label="G.E.M.S", menu=self.gemsMENU)
    self.gemsMenuBar.add_cascade(label="Help", menu=self.gemsHELP)
    self.gems.config(menu=self.gemsMenuBar)

    def tbc(self):
        print("To Be Completed")
        gems_gui = GEMS_GUI()
        gems_gui.gems.mainloop()
# Buttons
        self.viewItems = tk.Button(self.westPanel, text="View: Item")
        self.viewClients = tk.Button(self.westPanel, text="View: Client")
        self.viewAdministrators = tk.Button(self.westPanel, text="View: Administrator")
        self.viewAccountManagers = tk.Button(self.westPanel, text="View: AccountManager")
        self.viewSuppliers = tk.Button(self.westPanel, text="View: Supplier")
        self.viewOrders = tk.Button(self.westPanel, text="View: Order")

        # Panels
        self.westPanel = tk.Frame(self.gems)
        self.westPanel.pack(side=tk.LEFT, fill=tk.Y)
        self.westPanel.pack_propagate(False)
        self.westPanel.config(width=200, bd=1, relief=tk.RAISED)
        self.viewItems.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X)
        self.viewClients.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X)
        self.viewAdministrators.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X)
        self.viewAccountManagers.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X)
        self.viewSuppliers.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X)
        self.viewOrders.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X)
    
        self.centerPanel = tk.Frame(self.gems)
        self.centerPanel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.centerPanel.pack_propagate(False)
        self.centerPanel.config(bd=1, relief=tk.RAISED)
    
        self.centerSouth = tk.Frame(self.centerPanel)
        self.centerSouth.pack(side=tk.BOTTOM, fill=tk.X)
        self.centerSouth.pack_propagate(False)
        self.centerSouth.config(bd=1, relief=tk.RAISED)













        

