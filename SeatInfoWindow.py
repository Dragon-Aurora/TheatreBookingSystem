from SeatInfo import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import SQLServerAccess


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
        self.db_connection = SQLServerAccess.SQLServerAccess()

    def loadDisplay(self, row, column, seatID, performanceId):
        """Information relating to the specific seatID used is to be displayed"""
        customerId = -1
        bookingtype = ""
        found = False
        self.db_connection.open()
        booking_cursor = self.db_connection.execute("SELECT * FROM tBooking").fetchall()
        for cur in booking_cursor:
            id = cur[1]
            performance = cur[3]
            if id == seatID and performance == performanceId:
                customerId = cur[2]
                bookingtype = cur[5]
                found = True
                break
        self.db_connection.close()

        self.customer.setText("Seat Free")
        self.phoneNumber.setText("")
        self.customerType.setText("")

        if found:
            self.db_connection.open()
            customer_cursor = self.db_connection.execute("SELECT * FROM tCustomer WHERE CustomerID=" + str(customerId)).fetchall()

            for cur in customer_cursor:
                self.customer.setText(cur[1] + " " + cur[2])
                self.phoneNumber.setText(cur[3])
                self.customerType.setText(bookingtype)
            self.db_connection.close()
        self.seatId.setText("row " + str(row) + " col " + str(column))


