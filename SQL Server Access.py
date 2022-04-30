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
        Initialises the UI.
        """
        super(BookingWindow, self).__init__()
        self.setupUi(self)
        self.connectSignalsSlots()

        self.seatInfoWindow = SeatInfoWindow(self)
# "UID=COLLYERS\21DixonSE86;"
# "pwd=galaxy"

statementSQL = "SELECT * from tCarPark"
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
                self.registration.setText(str(row[3]))

        except pyodbc.DatabaseError as err:
            print("Error: ")
            print(err)
            self.databaseView.clearContents()
            exit(1)
            #print(e)

        self.cnxn.close()
        self.cnxn = pyodbc.connect(cs)

        # query the table for the data in a row
        cursor = self.cnxn.execute("SELECT EXPIRE_DATE, names, reg, model, make, permit_type from tCarPark").fetchall()

        self.updateTable(self.cnxn, cursor, "SELECT COUNT() FROM tCarPark")

        self.cnxn.close()
    def Data(): #Retreives data from SQL server and seperates into categories
                """CustData = []
        CustSQL = "SELECT Cust from ..."
        CustData.insert()"""
