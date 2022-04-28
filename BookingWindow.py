from SeatLabel import *
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

        self.dummydata()


    def connectSignalsSlots(self):
        """ Connects the Qt UI signals to the slots (methods) that perform the work """
        # Puts out a signal when the seats are clicked
        for row in range(0, 10):
            for column in range(0, 20):
                seat = SeatLabel(self.gridLayoutWidget)
                seat.setEnabled(True)
                seat.setAlignment(QtCore.Qt.AlignCenter)
                seat.setObjectName("row " + str(row) + "col " + str(column))
                self.SeatLayout.addWidget(seat, row, column, 1, 1)
                seat.setRowColumn(row, column)
                seat.clicked.connect(self.seatClicked)

        self.Cust_comboBox.currentIndexChanged.connect(self.Customer_ComboBox)
        self.Performance_comboBox.currentIndexChanged.connect(self.Performance_ComboBox)

        self.Book_PushButton.clicked.connect(self.Booking_Save)

    def dummydata(self):
        # Fill the combo boxes with data from the SQL database
        self.Cust_comboBox.addItem("hi")
        self.Cust_comboBox.addItem("hi1")
        self.Cust_comboBox.addItem("hi2")

        self.Performance_comboBox.insertItem(0, "index0")
        self.Performance_comboBox.insertItem(1, "index1")

    def seatClicked(self, row, column):
        self.displaySeatInformation(row, column)

    def displaySeatInformation(self, row, column):
        print(row, column)
        self.seatInfoWindow.loadDisplay(row, column)
        self.seatInfoWindow.show()

    def Performance_ComboBox(self, index):
        print("performance ", index)

    def Customer_ComboBox(self, index):
        print("customer ", index)

    def Booking_Save(self):
        print("Saved")
