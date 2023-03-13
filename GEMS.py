import mysql.connector
class GEMS:
    connection = None
    # user name for database
    username = "root"
    # password for database 
    password = "Candy09!"
    def __init__(self):
        try:
            self.connectGEMS()
        except Exception as e:
            print(e)  # for testing, delete all prints after / put in GUI handlers
    #Connect to GEMS Database
    def connectGEMS(self):
        try:
            GEMS.connection = mysql.connector.connect(host='localhost',
                                                       database='gemsDB',
                                                       user=self.username,
                                                       password=self.password)
        except Exception as e:
            print(e)
##############################################################################################################
    def createAdministratorObject(self, forename, surname, phoneNo):
        try:
            # create a cursor object to execute SQL queries
            cursor = GEMS.connection.cursor()
            # execute the query to insert a new administrator object into the database
            query = "INSERT INTO gemsDB.Administrator (forename, surname, phoneNo) VALUES (%s, %s, %s)"
            values = (forename, surname, phoneNo)
            cursor.execute(query, values)
            # commit the changes to the database
            GEMS.connection.commit()
        except Exception as e:
            print(e)
##############################################################################################################
    def createAccountManagerObject(self, forename, surname, phoneNo):
        try:
            # create a cursor object to execute SQL queries
            cursor = GEMS.connection.cursor()
            # execute the query to insert a new account manager object into the database
            query = "INSERT INTO gemsDB.AccountManager (forename, surname, phoneNo) VALUES (%s, %s, %s)"
            values = (forename, surname, phoneNo)
            cursor.execute(query, values)
            # commit the changes to the database
            GEMS.connection.commit()
        except Exception as e:
            print(e)
##############################################################################################################
    def createClientObject(self, companyName, address, accountManagerID, contactForename, contactSurname, contactEmail, contactPhoneNo):
        try:
            # create a cursor object to execute SQL queries
            cursor = GEMS.connection.cursor()
            # execute the query to insert a new client object into the database
            query = "INSERT INTO gemsDB.Client (companyName, address, accountManagerID, contactForename, contactSurname, contactEmail, contactPhoneNo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (companyName, address, accountManagerID, contactForename, contactSurname, contactEmail, contactPhoneNo)
            cursor.execute(query, values)
            # commit the changes to the database
            GEMS.connection.commit()
        except Exception as e:
            print(e)
##############################################################################################################
    def createItemObject(self, description, supplierID, buyPrice, sellPrice):
        try:
            # create a cursor object to execute SQL queries
            cursor = self.connection.cursor()
            # execute the query to insert a new item object into the database
            query = "INSERT INTO gemsDB.Item (description, supplierID, buyPrice, sellPrice) VALUES (%s, %s, %s, %s)"
            values = (description, supplierID, buyPrice, sellPrice)
            cursor.execute(query, values)
            # commit the changes to the database
            self.connection.commit()
        except Exception as e:
            print(e)
##############################################################################################################
    def createOrderObject(self, clientID, accountManID, adminID, itemID, quantity, supplierID, deliveryAddress):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO gemsDB.Order (clientID, accountManID, adminID, itemID, quantity, supplierID, deliveryAddress) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (clientID, accountManID, adminID, itemID, quantity, supplierID, deliveryAddress)
            cursor.execute(query, values)
            self.connection.commit()
        except Exception as e:
            print(e)
##############################################################################################################
    def createSupplierObject(self, companyName, address, forename, surname, email, phoneNo):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO gemsDB.Supplier (companyName, address, contactForename, contactSurname, contactEmail, contactPhoneNo) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (companyName, address, forename, surname, email, phoneNo)
            cursor.execute(query, values)
            self.connection.commit()
        except Exception as e:
            print(e)
##############################################################################################################
    def retrieveSelectedTable(self, table_name):
        try:
            sql = f"SELECT * FROM gemsDB.{table_name}"
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rs = cursor.fetchall()
            print(f"\n********{table_name} TABLE********\n")
            if not rs:
                print(f"{table_name} Table Empty\n")
            else:
                for row in rs:
                    for i in range(len(row)):
                        column_name = cursor.description[i][0]
                        print(f"{column_name}: {row[i]}  \n")
        except Exception as e:
            print(e)
##############################################################################################################
    def retrieveSelectedTableObject(self, s):
        try:
            sql = "SELECT * FROM gemsDB." + s
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rs = cursor.fetchall()
            if not rs:
                return None
            columnsNumber = cursor.description.__len__()
            dataList = []
            for row in rs:
                dataRow = [None] * columnsNumber
                for i in range(columnsNumber):
                    dataRow[i] = row[i]
                    dataList.append(dataRow)
            data = [[None] * columnsNumber for i in range(dataList.__len__())]
            for i in range(dataList.__len__()):
                data[i] = dataList[i]
            return data
        except Exception as e:
            print(e)
            return None
##############################################################################################################
    def updateEntry(self, databaseTable, row, newEntry, primaryKey, value):
        try:
            query = "UPDATE gemsDB.{0} SET {1} = '{2}' WHERE ({3} = '{4}');".format(databaseTable, row, newEntry, primaryKey, value)
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print(e)
##############################################################################################################
    def deleteRow(self, databaseTable, row, condition):
        try:
            query = "DELETE FROM gemsDB.{0} WHERE ({1} = '{2}');".format(databaseTable, row, condition)
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print(e)
