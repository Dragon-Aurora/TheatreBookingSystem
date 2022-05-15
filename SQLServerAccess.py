import pyodbc as pyodbc
from BookingWindow import *

College = False
cs = ""

# https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows
# https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver15
# Try commenting out Trusted_Connection
#
# The scripts on the Microsoft website are not correct for installing the ODBC drivers
# on Ubuntu 20.04. See install_odbc for notes on workarounds.
#
# The SQL server needs to be configured for SQL Server authentication and the following needs to be checked
# and configured if not for remote access (firewall, sql tcp/ip port)
#  - https://social.technet.microsoft.com/wiki/contents/articles/1533.how-to-enable-remote-connections-on-sql-server.aspx

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

"""
The Following is to create the tBooking Table:

    CREATE TABLE tBooking(
        BookingID int primary key,
        SeatID varchar(1) foreign key REFERENCES tSeats(SeatsID),
        CustomerID int foreign key REFERENCES tCustomer(CustomerID),
        PerformanceID int foreign key REFERENCES tPerformace(PerformanceID)
    );


"""

class SQLServerAccess:
    def __init__(self):
        """ Constructor
        """
        # "UID=COLLYERS\21DixonSE86;"
        # "pwd=galaxy"
        self.cnxn = None
        """
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
        self.cnxn = pyodbc.connect(cs)

        # query the table for the data in a row
        Booking_cursor = self.cnxn.execute("SELECT * from tBooking").fetchall()
        Seats_cursor = self.cnxn.execute("SELECT * FROM tSeats").fetchall()
        Perf_cursor = self.cnxn.execute("SELECT * FROM tPerformance").fetchall()
        Cust_cursor = self.cnxn.execute("SELECT * FROM tCustomer").fetchall()

        self.updateTable(self.cnxn, Booking_cursor, "SELECT COUNT() FROM tBooking")
        self.updateTable(self.cnxn, Seats_cursor, "SELECT COUNT() FROM tSeats")
        self.updateTable(self.cnxn, Perf_cursor, "SELECT COUNT() FROM tPerformance")
        self.updateTable(self.cnxn, Cust_cursor, "SELECT COUNT() FROM tCustomer")

        self.cnxn.close()
        """

    def open(self):
        try:
            self.cnxn = pyodbc.connect(cs)

        except pyodbc.DatabaseError as err:
            print("Error: ")
            print(err)
            exit(1)

    def close(self):
        self.cnxn.close()

    def commit(self):
        self.cnxn.commit()

    def execute(self, statement_SQL):
        if self.cnxn is not None:
            cursor = self.cnxn.cursor()
            cursor.execute(statement_SQL)
            return cursor
        return None

    def Data(self):  # Retreives data from SQL server and separates into categories
        CustSQL = "SELECT * from tCustomer"
        PerfSQL = "SELECT * FROM tPerformance"
        BookingSQL = "SELECT * FROM tBooking"
        SeatsSQL = "SELECT * FROM tSeats"

    """def populateTable(self): #Retreives data from SQL server and separates into categories
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

    test = SQLServerAccess()
    print("fini finum")
