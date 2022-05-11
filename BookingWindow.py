from SeatLabel import *
from SeatBooking import *
from SeatInfoWindow import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from SQLServerAccess import *

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
        self.setupUi(self)
        self.connectSignalsSlots()

        self.seatInfoWindow = SeatInfoWindow(self)

        self.BookingData()


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
        #Connects booking button
        self.Book_PushButton.clicked.connect(self.Booking_Save)

    def BookingData(self):
        BookingSQL = "SELECT * FROM tBooking"
        # dump all the data into the table
        # call SQLServerAccess to get data from db
        sqlServerDb.open()
        cursor = sqlServerDb.excute(BookingSQL)
        # extract all data using cursor and put in UI
        Booking_cursor = self.cnxn.execute("SELECT * from tBooking").fetchall()
        Performance_cursor = self.cnxn.execute("SELECT * FROM tPerformance").fetchall()
        Cust_cursor = self.cnxn.execute("SELECT * FROM tCustomer")
        sqlServerDb.close()

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
        self.Performance_comboBox.addItems("SELECT Performance_Time FROM tPerformance")

    def Customer_ComboBox(self, index):
        print("customer ", index)
        self.Cust_comboBox.addItems("SELECT First_name, Surname FROM tCustomer")

    def Booking_Save(self):
        print("Saved")
        #INSERT new values into the booking table
