College = False
cs = ""

if College:
    cs = (
        "Driver={SQL Server};"  # deprecated
        "Server=svr-cmp-01;"
        "Database=21DixonSE86;"
        "Trusted_Connection=yes;"  # try removing as you specify UID and pwd
        "UID=COLLYERS\21DixonSE86;"
        "pwd=galaxy"
    )
else:
    cs = (
        "Driver={ODBC Driver 17 for SQL Server};"  # SQL server 2008 to 2019
        "Server=MSI-SUSIE;"
        "Database=21DixonSE86;"
        "Trusted_Connection=yes;"
    )

class SQL_Info():
    def __init__(self, parent=None):
        """ Constructor
        Initialises the UI.
        """
        super(BookingWindow, self).__init__()
        self.setupUi(self)
        self.connectSignalsSlots()

        self.seatInfoWindow = SeatInfoWindow(self)
# "UID=COLLYERS\21DixonSE86;"
# "pwd=galaxy"
