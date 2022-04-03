from ChoiceMenu import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from SeatLabel import *
from RecordsWindow import *
from BookingWindow import *

# To convert a UI to a python file:
#   pyuic5 -x "Menu".ui -o "ChoiceMenu".py


class ChoiceMenuWindow(QMainWindow, Ui_MainWindow):
    """ The MyChoiceMenu inherits from the UI ChoiceMenu.ui class implemented using Qtdesigner.

    Two buttons are provided
    - Seat Booking
    - Existing Records

    When the user clicks on a button the required dialog/window is displayed.
    """

    def __init__(self, parent=None):
        """ Constructor - initialise the class.
        :param parent: see Qt5 docs
        """
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

        self.recordsWindow = RecordsWindow(self)
        self.bookingWindow = BookingWindow(self)

    def connectSignalsSlots(self):
        """Connect the buttons to the methods to display the windows """
        self.BookingButton.pressed.connect(self.bookingButtonClicked)
        self.RecordsButton.pressed.connect(self.recordButtonClicked)

    def bookingButtonClicked(self):
        """Display the booking window - bring it to the front"""
        print("hi Booking")
        self.recordsWindow.show()
        self.recordsWindow.raise_()
        self.recordsWindow.setWindowState(Qt.WindowActive)

    def recordButtonClicked(self):
        """Display the Record Search window - bring it to the front"""
        print("Hi records")
        self.bookingWindow.show()
        self.bookingWindow.raise_()
        self.bookingWindow.setWindowState(Qt.WindowActive)
