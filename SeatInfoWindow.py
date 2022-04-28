from SeatInfo import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


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
    #def loaddisplay(self):

