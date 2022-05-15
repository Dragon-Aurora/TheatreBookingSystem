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
        self.db_connection = SQLServerAccess()
        self.setupUi(self)
        self.SeatsData()
        self.PerformanceData()
        self.CustomerData()
        self.FillTable()
        self.connectSignalsSlots()

        self.CustType_Combo.addItem(" ")
        self.CustType_Combo.addItem("Special Guest")
        self.CustType_Combo.addItem("Reduced")
        self.CustType_Combo.addItem("Standard")

    def connectSignalsSlots(self):
        """ Connects the Qt UI signals to the slots (methods) that perform the work """
        # connect the combo-boxes and buttons (signals and slots)
        self.Customer_Combo.currentIndexChanged.connect(self.FillTable)
        self.Performance_Combo.currentIndexChanged.connect(self.FillTable)
        self.SeatID_Combo.currentIndexChanged.connect(self.FillTable)
        self.CustType_Combo.currentIndexChanged.connect(self.FillTable)

    def configureTable(self):
        self.RecordsTable.clear()
        self.RecordsTable.setColumnCount(7)
        self.RecordsTable.horizontalHeader()
        labels = ("Name", "Surname", "Performance", "Time", "Seat", "Type", "Cost")
        self.RecordsTable.setHorizontalHeaderLabels(labels)

    def PerformanceData(self):
        self.db_connection.open()
        Performance_cursor = self.db_connection.execute("SELECT * FROM tPerformance").fetchall()
        self.Performance_Combo.addItem(' ')
        for item in Performance_cursor:
            # Get the Time of the performance - the index 1 is the second column which is Performance_Time
            performanceTime = item[1].strftime('%H:%M')
            # Get the date of the performance - third column Performance_Date
            performanceDate = str(item[2])
            # Format the value for adding to the combobox
            value = performanceTime + " " + performanceDate
            self.Performance_Combo.addItem(value)
        self.db_connection.close()

    def SeatsData(self):
        self.db_connection.open()
        self.SeatID_Combo.addItem(' ')
        SeatID_cursor = self.db_connection.execute("SELECT * FROM tSeats").fetchall()
        for item in SeatID_cursor:
            SeatID = item[0]
            self.SeatID_Combo.addItem(str(SeatID))
        self.db_connection.close()

    def CustomerData(self):
        self.db_connection.open()
        self.Customer_Combo.addItem(' ')
        Cust_cursor = self.db_connection.execute("SELECT * FROM tCustomer")
        for item in Cust_cursor:
            FirstName = item[1]
            Surname = item[2]
            fullname = FirstName+" "+Surname
            self.Customer_Combo.addItem(fullname)
        self.db_connection.close()

    def FillTable(self):
        SQLStatement = "SELECT * FROM tBooking "
        #Update table so that the data in it displays all the bookings that performance has
        PerfIndex = self.Performance_Combo.currentIndex() - 1
        if PerfIndex >= 0:
            SQLStatement = SQLStatement + " WHERE PerformanceID=" + str(PerfIndex)

        CustomerIndex = self.Customer_Combo.currentIndex() - 1
        if CustomerIndex >= 0:
            if PerfIndex >= 0:
                SQLStatement = SQLStatement + " AND "
            else:
                SQLStatement = SQLStatement + " WHERE "
            SQLStatement = SQLStatement + " CustomerID=" + str(CustomerIndex)

        CustomerTypeIndex = self.CustType_Combo.currentIndex() - 1
        if CustomerTypeIndex >= 0:
            if PerfIndex >= 0 or CustomerIndex >= 0:
                SQLStatement = SQLStatement + " AND "
            else:
                SQLStatement = SQLStatement + " WHERE "
            SQLStatement = SQLStatement + " Customer_Type='" + str(self.CustType_Combo.currentText()) + "'"

        print(SQLStatement)
        self.db_connection.open()
        # extract all data using cursor and put in UI
        bookings_cur = self.db_connection.execute(SQLStatement).fetchall()
        rowCount = len(bookings_cur)
        self.configureTable()
        self.RecordsTable.setRowCount(rowCount)
        rowNumber = 0
        for booking in bookings_cur:
            seatId = booking[1]
            customerId = booking[2]
            performanceId = booking[3]
            cost = booking[4]
            customerType = booking[5]

            # "Name", "Surname", "Performance", "Time", "Seat", "Type", "Cost"
            customer_cur = self.db_connection.execute("SELECT * FROM tCustomer WHERE CustomerID=" + str(customerId)).fetchall()
            for customer in customer_cur:
                self.RecordsTable.setItem(rowNumber, 0, QTableWidgetItem(str(customer[1])))
                self.RecordsTable.setItem(rowNumber, 1, QTableWidgetItem(str(customer[2])))
            performance_cur = self.db_connection.execute("SELECT * FROM tPerformance WHERE PerformanceID=" + str(performanceId)).fetchall()
            for performance in performance_cur:
                self.RecordsTable.setItem(rowNumber, 2, QTableWidgetItem(str(performance[1])))
                self.RecordsTable.setItem(rowNumber, 3, QTableWidgetItem(str(performance[2])))

            self.RecordsTable.setItem(rowNumber, 4, QTableWidgetItem(str(seatId)))
            self.RecordsTable.setItem(rowNumber, 5, QTableWidgetItem(customerType))
            self.RecordsTable.setItem(rowNumber, 6, QTableWidgetItem(str(cost)))

            rowNumber = rowNumber + 1

        self.db_connection.close()
