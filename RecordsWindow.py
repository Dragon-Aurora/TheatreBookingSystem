from Records import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


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
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        """ Connects the Qt UI signals to the slots (methods) that perform the work """
        print("hi")
