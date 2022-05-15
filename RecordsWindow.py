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
        self.BookingData()
        self.SeatsData()
        self.PerformanceData()
        self.CustomerData()
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        """ Connects the Qt UI signals to the slots (methods) that perform the work """
        # connect the combo-boxes and buttons (signals and slots)
        self.Customer_Combo.currentIndexChanged.connect(self.Cust_Combo)
        self.Performance_Combo.currentIndexChanged.connect(self.Perf_Combo)
        self.SeatID_Combo.currentIndexChanged.connect(self.seatID_Combo)
        self.CustType_Combo.currentIndexChanged.connect(self.custType_Combo)

    def BookingData(self):
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

    def PerformanceData(self):
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

    def SeatsData(self):
        self.db_connection.open()
        SeatID_cursor = self.db_connection.execute("SELECT * FROM tSeats").fetchall()
        for item in SeatID_cursor:
            SeatID = item[0]
            self.SeatID_Combo.addItem(str(SeatID))
        self.db_connection.close()

    def CustomerData(self):
        self.db_connection.open()
        Cust_cursor = self.db_connection.execute("SELECT * FROM tCustomer")
        for item in Cust_cursor:
            FirstName = item[1]
            Surname = item[2]
            fullname = FirstName+" "+Surname
            self.Customer_Combo.addItem(fullname)

        self.db_connection.close()

    def Cust_Combo(self):
        print("combo cust")
        #Update table so that the data in it displays all the bookings that customer has made
        CustText = self.Customer_Combo.currentText()
        name = CustText.split(" ")
        firstname = name[0]
        surname = name[1]
        SQLStatement = "SELECT * FROM tBooking WHERE CustomerID =(SELECT CustomerID FROM tCustomer WHERE First_Name = "+firstname+", Surname = "+surname
        self.db_connection.open()
        # extract all data using cursor and put in UI
        BookingCustName_cursor = self.db_connection.execute(SQLStatement).fetchall()
        for item in BookingCustName_cursor:
            self.RecordsTable.update(item)
        self.db_connection.close()

    def Perf_Combo(self):
        print("combo perf")
        #Update table so that the data in it displays all the bookings that performance has
        PerfText = self.Performance_Combo.currentText()
        performances = PerfText.split(" ")
        time = performances[0]
        date = performances[1]
        SQLStatement = "SELECT * FROM tBooking WHERE PerformanceID=(SELECT PerformanceID FROM tPerformance WHERE Performance_Time='"+time+"' AND Performance_Date = '" + date+"')"
        print(SQLStatement)
        self.db_connection.open()
        # extract all data using cursor and put in UI
        Performance_cursor = self.db_connection.execute(SQLStatement).fetchall()
        for item in Performance_cursor:
            self.RecordsTable.update(item)
        self.db_connection.close()

    def seatID_Combo(self):
        print("seats combo")
        #Update table so that the data in it displays all the bookings that Seat has
        SeatIDText = self.CustType_Combo.currentText()
        SQLStatement = "SELECT * FROM tBooking WHERE SeatID=(SELECT SeatID FROM tSeats WHERE SeatID="+SeatIDText+")"
        print(SQLStatement)
        self.db_connection.open()
        # extract all data using cursor and put in UI
        SeatID_cursor = self.db_connection.execute(SQLStatement).fetchall()
        for item in SeatID_cursor:
            self.RecordsTable.update(item)
        self.db_connection.close()

    def custType_Combo(self):
        print("time combo")
        #Update table so that the data in it displays all the bookings that customer type has
        CustTypeText = self.CustType_Combo.currentText()
        SQLStatement = "SELECT * FROM tBooking WHERE Customer_Type='"+CustTypeText+"'"
        self.db_connection.open()
        # extract all data using cursor and put in UI
        print(SQLStatement)
        CustType_cursor = self.db_connection.execute(SQLStatement).fetchall()
        for item in CustType_cursor:
            self.RecordsTable.update(item)
        self.db_connection.close()