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
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        """ Connects the Qt UI signals to the slots (methods) that perform the work """
        # connect the combo-boxes and buttons (signals and slots)
        self.Customer_Combo.currentIndexChanged.connect(self.Cust_Combo)
        self.Performance_Combo.currentIndexChanged.connect(self.Perf_Combo)
        self.SeatID_Combo.currentIndexChanged.connect(self.seatID_Combo)
        self.Time_Combo.currentIndexChanged.connect(self.time_Combo)

    def RecordsData(self):
        BookingSQL = "SELECT * FROM tBooking"
        # dump all the data into the table
        # call SQLServerAccess to get data from db
        sqlServerDb.open()
        cursor = sqlServerDb.excute(BookingSQL)
        # extract all data using cursor and put in UI

        sqlServerDb.close();

        """rowCount = len(cursor)

        RecordsTable"""

    def Cust_Combo(self):
        print("combo cust")

    def Perf_Combo(self):
        print("combo perf")

    def seatID_Combo(self):
        print("seats combo")

    def time_Combo(self):
        print("time combo")
