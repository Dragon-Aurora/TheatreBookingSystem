from SeatLabel import *
from SeatBooking import *
from SeatInfoWindow import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import SQLServerAccess


class BookingWindow(QMainWindow, Ui_SeatBooking):
    """ Records inherits from the UI 'Records.ui' python implementation.

    The UI objects signal are connected to a slot that implement the functionality required.

    The data is loaded into the UI objects and the database updated as required.
    """

    def __init__(self, parent=None):
        """ Constructor
        Initialises the UI.
        """
        super(BookingWindow, self).__init__()
        self.db_connection = None
        self.setupUi(self)
        self.seatInfoWindow = SeatInfoWindow(self)
        self.BookingData()
        self.CustData()
        self.PerfData()
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        """ Connects the Qt UI signals to the slots (methods) that perform the work.

        Fills in the Seat grid with the 200 seats in a grid of 10 rows with 20 seats per row
        and connects them to a single slot that is called on a seat being pressed.
        """

        # create the seats
        for row in range(0, 10):
            for column in range(0, 20):
                # note: the SeatLabel could be drawn differently if the seat has been booked.
                seat = SeatLabel(self.gridLayoutWidget)
                seat.setEnabled(True)
                seat.setAlignment(QtCore.Qt.AlignCenter)
                seat.setObjectName("row " + str(row) + "col " + str(column))
                seat.setRowColumn(row, column)
                # connect the Seat to the slot.
                seat.clicked.connect(self.seatClicked)
                # place the Seat in the grid at row column
                self.SeatLayout.addWidget(seat, row, column, 1, 1)

        # connect the combo-boxes and buttons (signals and slots)
        self.Cust_comboBox.currentIndexChanged.connect(self.Customer_ComboBox)
        self.Performance_comboBox.currentIndexChanged.connect(self.Performance_ComboBox)
        # Connects booking button
        self.Book_PushButton.clicked.connect(self.Booking_Save)

    def BookingData(self):
        BookingSQL = "SELECT * FROM tBooking"
        # dump all the data into the table
        # call SQLServerAccess to get data from db
        self.db_connection = SQLServerAccess.SQLServerAccess()
        self.db_connection.open()
        # extract all data using cursor and put in UI
        """ Booking_cursor = self.db_connection.execute(BookingSQL).fetchall()
        Performance_cursor = self.db_connection.execute("SELECT * FROM tPerformance").fetchall()
        SeatID_cursor = self.db_connection.execute("SELECT * FROM tSeats").fetchall()
        Cust_cursor = self.db_connection.execute("SELECT * FROM tCustomer")"""

    def PerfData(self):
        self.db_connection.open()
        SQL_Perf = self.db_connection.execute("SELECT * FROM tPerformance").fetchall()
        for item in SQL_Perf:
            # Get the Time of the performance - the index 1 is the second column which is Performance_Time
            performanceTime = item[1].strftime('%H:%M')
            # Get the date of the performance - third column Performance_Date
            performanceDate = str(item[2])
            # Format the value for adding to the combobox
            value = performanceTime + " " + performanceDate
            self.Performance_comboBox.addItem(value)
        self.db_connection.close()

    def CustData(self):
        self.db_connection.open()
        SQL_Cust = self.db_connection.execute("SELECT * FROM tCustomer").fetchall()
        for item in SQL_Cust:
            FirstName = item[1]
            Surname = item[2]
            fullname = FirstName+" "+Surname
            self.Cust_comboBox.addItem(fullname)
        self.db_connection.close()

    def seatClicked(self, row, column):
        """When the SealLabel is pressed this method is called with the row and column of the seat"""
        self.displaySeatInformation(row, column)

    def displaySeatInformation(self, row, column):
        """ Display the Seat information for the seat at row column """
        print(row, column)
        self.seatInfoWindow.loadDisplay(row, column)
        self.seatInfoWindow.show()

    def Performance_ComboBox(self, index):
        print("performance ", index)

    def Customer_ComboBox(self, index):
        print("customer ", index)

    def Booking_Save(self):
        print("Saved")
        # INSERT new values into the booking table


if __name__ == "__main__":
    import sys

    test = BookingWindow()
    print("fini finum")
