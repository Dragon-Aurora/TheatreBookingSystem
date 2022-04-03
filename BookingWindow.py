from SeatBooking import *
from SeatInfoWindow import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


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

    def connectSignalsSlots(self):
        """ Connects the Qt UI signals to the slots (methods) that perform the work """
        print("hi")
        # Puts out a signal when the seats are double clicked
        self.A1C1(self.A1C1_clicked)
        self.A2C2.mouseDoubleClickEvent(self.A2C2_clicked)
        self.A3C3.mouseDoubleClickEvent.connect(self.A3C3_clicked)
        self.B1C1.mouseDoubleClickEvent.connect(self.B1C1_clicked)
        self.B2C2.mouseDoubleClickEvent.connect(self.B2C2_clicked)
        self.B3C3.mouseDoubleClickEvent.connect(self.B3C3_clicked)
        self.C1C1.mouseDoubleClickEvent.connect(self.C1C1_clicked)
        self.C2C2.mouseDoubleClickEvent.connect(self.C2C2_clicked)
        self.C3C3.mouseDoubleClickEvent.connect(self.C3C3_clicked)

    def A1C1_clicked(self):
        self.seatClicked(1, 1)

    def A2C2_clicked(self):
        self.seatClicked(1,2)

    def A3C3_clicked(self):
        self.seatClicked(1,3)

    def B1C1_clicked(self):
        self.seatClicked(2,1)

    def B2C2_clicked(self):
        self.seatClicked(2,2)

    def B3C3_clicked(self):
        self.seatClicked(2,3)

    def C1C1_clicked(self):
        self.seatClicked(3,1)

    def C2C2_clicked(self):
        self.seatClicked(3,2)

    def C3C3_clicked(self):
        self.seatClicked(3,3)

    def seatClicked(self, row, column):
        print(row,column)
