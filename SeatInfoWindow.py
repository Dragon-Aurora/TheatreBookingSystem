from SeatInfo import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from SQLServerAccess import *


class SeatInfoWindow(QMainWindow, Ui_SeatInfo):
    """ Records inherits from the UI 'Records.ui' python implementation.

    The UI objects signal are connected to a slot that implement the functionality required.

    The data is loaded into the UI objects and the database updated as required.
    """

    def __init__(self, parent=None):
        """ Constructor
        Initialises the UI.
        """
        super(SeatInfoWindow, self).__init__()
        self.setupUi(self)

    def SQLData(self):
        self.cnxn.open()
        booking_cursor = self.cnxn.execute("SELECT * FROM tBooking").fetchall()
        customer_cursor = self.cnxn.execute("SELECT * FROM tCustomer").fetchall()
        performance_cursor = self.cnxn.execute("SELECT * FROM tPerformance").fetchall()
        seatsID_cursor = self.cnxn.execute("SELECT * FROM tSeatsID").fetchall()
        self.cnxn.close()

    def loadDisplay(self, row, column):
        print("load display ", row, column)
        #Information relating to the specific seatID used is to be displayed
        self.customer.setText("Damian")
        self.phoneNumber.setText("01403 273173")
        self.customerType.setText("Parent")
        self.seatId.setText(str(row) + " " + str(column))
