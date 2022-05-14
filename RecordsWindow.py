from Records import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from SQLServerAccess import *

class RecordsWindow(QMainWindow, Ui_Records):
    """ Records inherits from the UI 'Records.ui' python implementation.

    The UI objects signal are connected to a slot that implement the functionality required.

    The data is loaded into the UI objects and the database updated as required.
    """

    def __init__(self, parent=None):
        """ Constructor
        Initialises the UI.
        """
        super(RecordsWindow, self).__init__()
        self.db_connection = SQLServerAccess()
        self.setupUi(self)
        self.connectSignalsSlots()
        self.RecordsData()

    def connectSignalsSlots(self):
        """ Connects the Qt UI signals to the slots (methods) that perform the work """
        # connect the combo-boxes and buttons (signals and slots)
        self.Customer_Combo.currentIndexChanged.connect(self.Cust_Combo)
        self.Performance_Combo.currentIndexChanged.connect(self.Perf_Combo)
        self.SeatID_Combo.currentIndexChanged.connect(self.seatID_Combo)
        self.CustType_Combo.currentIndexChanged.connect(self.custType_Combo)

    def RecordsData(self):
        # The database is opened and a single query is executed then the database is closed.
        # Executing a subsequent query before close and open does not seem to work.

        BookingSQL = "SELECT * FROM tBooking"
        # dump all the data into the table
        # call SQLServerAccess to get data from db
        self.db_connection.open()
        # extract all data using cursor and put in UI
        Booking_cursor = self.db_connection.execute(BookingSQL).fetchall()
        for item in Booking_cursor:
            self.RecordsTable.update(item)
        self.db_connection.close()

        self.db_connection.open()
        Performance_cursor = self.db_connection.execute("SELECT * FROM tPerformance").fetchall()
        for item in Performance_cursor:
            # Get the Time of the performance - the index 1 is the second column which is Performance_Time
            performanceTime = item[1].strftime('%H:%M')
            # Get the date of the performance - third column Performance_Date
            performanceDate = str(item[2])
            # Format the value for adding to the combobox
            value = performanceTime + " " + performanceDate
            self.Performance_Combo.addItem(value)
        self.db_connection.close()

        self.db_connection.open()
        SeatID_cursor = self.db_connection.execute("SELECT * FROM tSeats").fetchall()
        for item in SeatID_cursor:
            SeatID = item[0]
            self.SeatID_Combo.addItem(str(SeatID))
        self.db_connection.close()

        self.db_connection.open()
        Cust_cursor = self.db_connection.execute("SELECT * FROM tCustomer")
        for item in Cust_cursor:
            FirstName = item[1]
            Surname = item[2]
            fullname = FirstName+" "+Surname
            self.Customer_Combo.addItem(fullname)

            CustType = item[5]
            self.CustType_Combo.addItem(CustType)
        self.db_connection.close()

    def Cust_Combo(self):
        print("combo cust")

    def Perf_Combo(self):
        print("combo perf")

    def seatID_Combo(self):
        print("seats combo")

    def custType_Combo(self):
        print("time combo")
