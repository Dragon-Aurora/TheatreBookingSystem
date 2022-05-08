import pyodbc as pyodbc
from BookingWindow import *


College = False
cs = ""

if College:
    cs = (
        "Driver={SQL Server};"  # deprecated
        "Server=svr-cmp-01;"
        "Database=21DixonSE86;"
        "Trusted_Connection=yes;"  # try removing as you specify UID and pwd
        "UID=COLLYERS\21DixonSE86;"
        "pwd=galaxy"
    )
else:
    cs = (
        "Driver={ODBC Driver 17 for SQL Server};"  # SQL server 2008 to 2019
        "Server=MSI-SUSIE;"
        "Database=21DixonSE86;"
        "Trusted_Connection=yes;"
    )

class SQL_Info():
    def __init__(self, parent=None):
        """ Constructor
        """
# "UID=COLLYERS\21DixonSE86;"
# "pwd=galaxy"

        statementSQL = "SELECT * from tSeats"
        try:
            self.cnxn = pyodbc.connect(cs)
            print("Connected")

            if self.cnxn is not None:
                cursor = self.cnxn.cursor()
                cursor.execute(statementSQL)
                row = cursor.fetchone()
                print(row)

        except pyodbc.DatabaseError as err:
            print("Error: ")
            print(err)
            # self.databaseView.clearContents()
            exit(1)
            #print(e)

        self.cnxn.close()

    """def Data(self): #Retreives data from SQL server and separates into categories
        CustSQL = "SELECT * from tCustomer


    def populateTable(self): #Retreives data from SQL server and separates into categories
        # open database
        statementSQL = "SELECT * from tBooking"
        try:
            self.cnxn = pyodbc.connect(cs)
            print("Connected")

            if self.cnxn is not None:
                cursor = self.cnxn.cursor()
                cursor.execute(statementSQL)
                row = cursor.fetchone()
                print(row)
                self.make.setText(str(row[0]))
                self.model.setText(str(row[1]))
                self.name.setText(str(row[2]))
                self.registration.setText(str(row[3]))"""


if __name__ == "__main__":
    import sys
    test = SQL_Info()
    print("fini finum")