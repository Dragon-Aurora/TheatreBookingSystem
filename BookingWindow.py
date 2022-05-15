from SeatLabel import *
from SeatBooking import *
from SeatInfoWindow import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import SQLServerAccess

# Number of rows of chairs
MaxRows = 10
# Number of columns of chairs
MaxColumns = 20

# Cost of ticket types
SpecialGuest = 0
Standard = 10
Reduced = 5

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

        self.seats = {}
        self.selectedRow = -1
        self.selectedColumn = -1
        self.performanceId = 0
        self.numberOfSeatsAvailable = 0
        # call SQLServerAccess to get data from db
        self.db_connection = SQLServerAccess.SQLServerAccess()
        self.setupUi(self)
        self.maxBookingID = self.SeatMaxID()
        self.seatInfoWindow = SeatInfoWindow(self)
        self.CostDisplay()
        self.CustData()
        self.PerfData()
        self.CustTypeData()
        self.connectSignalsSlots()

    def SeatMaxID(self):
        MaxID = -1
        self.db_connection.open()
        cursor = self.db_connection.execute("SELECT * FROM tBooking").fetchall()
        for cur in cursor:
            id = cur[0]
            if id > MaxID:
                MaxID = id
        self.db_connection.close()
        return MaxID

    def SeatAvailable(self, seatID, performanceId):
        self.db_connection.open()
        cursor = self.db_connection.execute("SELECT * FROM tBooking").fetchall()
        for cur in cursor:
            id = cur[1]
            performance = cur[3]
            if id == seatID and performance == performanceId:
                self.db_connection.close()
                return False
        self.db_connection.close()
        return True

    @staticmethod
    def seatIdent(row, column):
        return (row * MaxRows) + column

    def connectSignalsSlots(self):
        """ Connects the Qt UI signals to the slots (methods) that perform the work.

        Fills in the Seat grid with the 200 seats in a grid of 10 rows with 20 seats per row
        and connects them to a single slot that is called on a seat being pressed.
        """
        seats = 0
        # create the seats
        for row in range(0, 10):
            for column in range(0, 20):
                # note: the SeatLabel could be drawn differently if the seat has been booked.
                seat = SeatLabel(self.gridLayoutWidget)
                seat.setEnabled(True)
                seat.setAlignment(QtCore.Qt.AlignCenter)
                seat.setObjectName("row " + str(row) + "col " + str(column))
                seat.setRowColumn(row, column)
                seatId = self.seatIdent(row, column)
                self.seats[seatId] = seat

                seatAvailable = self.SeatAvailable(seatId, self.performanceId)
                seat.available(seatAvailable)
                if seatAvailable:
                    seats += 1

                # connect the Seat to the slot.
                seat.clicked.connect(self.seatClicked)
                # place the Seat in the grid at row column
                self.SeatLayout.addWidget(seat, row, column, 1, 1)

        self.numberOfSeatsAvailable = seats
        self.updateNumberOfSeats()

        self.SeatIDOutput.setText("None")
        self.Book_PushButton.setEnabled(False)
        # Connects booking button
        self.Book_PushButton.clicked.connect(self.Booking_Save)
        self.CustomerTypeCombo.currentTextChanged.connect(self.CostDisplay)
        self.Performance_comboBox.currentTextChanged.connect(self.PerformanceChanged)

    def PerformanceChanged(self):
        selectedPerformance = self.Performance_comboBox.currentIndex()
        self.performanceId = selectedPerformance
        seats = 0
        for row in range(0, 10):
            for column in range(0, 20):
                seatId = self.seatIdent(row, column)
                seat = self.seats[seatId]

                seatAvailable = self.SeatAvailable(seatId, self.performanceId)
                seat.available(seatAvailable)
                if seatAvailable:
                    seats += 1
        self.numberOfSeatsAvailable = seats
        self.updateNumberOfSeats()
        self.seatInfoWindow.hide()
        self.SeatIDOutput.setText("None")
        self.Book_PushButton.setEnabled(False)

    def updateNumberOfSeats(self):
        self.SeatsSoldOutput.setText(str((MaxRows * MaxColumns) - self.numberOfSeatsAvailable))
        self.SeatsAvailableOutput.setText(str(self.numberOfSeatsAvailable))

    def CostDisplay(self):
        CustTypeData = self.CustomerTypeCombo.currentText()
        Cost = 0
        if CustTypeData == 'Standard':
            Cost = Standard
        elif CustTypeData == 'Special Guest':
            Cost = SpecialGuest
        elif CustTypeData == 'Reduced':
            Cost = Reduced
        CostStr = str(Cost)
        self.CostOutput.setText("£" + CostStr)

    def PerfData(self):
        self.db_connection.open()
        SQL_Perf = self.db_connection.execute("SELECT * FROM tPerformance").fetchall()
        for item in SQL_Perf:
            # Get the Time of the performance - the index 1 is the second column which is Performance_Time
            performanceTime = item[1].strftime('%H:%M')
            # Get the date of the performance - third column Performance_Date
            performanceDate = str(item[2])
            # Format the value for adding to the combobox
            value = performanceTime + " " + performanceDate
            self.Performance_comboBox.addItem(value)
        self.db_connection.close()

    def CustTypeData(self):
        self.CustomerTypeCombo.addItem("Special Guest")
        self.CustomerTypeCombo.addItem("Reduced")
        self.CustomerTypeCombo.addItem("Standard")

    def CustData(self):
        self.db_connection.open()
        SQL_Cust = self.db_connection.execute("SELECT * FROM tCustomer").fetchall()
        for item in SQL_Cust:
            FirstName = item[1]
            Surname = item[2]
            fullname = FirstName+" "+Surname
            self.Cust_comboBox.addItem(fullname)
        self.db_connection.close()

    def seatClicked(self, row, column):
        """When the SealLabel is pressed this method is called with the row and column of the seat"""
        # Update the selected row and column "chair"
        self.selectedRow = row
        self.selectedColumn = column
        # Get the seat ID
        seatId = self.seatIdent(row, column)
        # Display the Seat information for the seat at row column
        self.seatInfoWindow.loadDisplay(row, column, seatId, self.performanceId)
        self.seatInfoWindow.show()
        self.seatInfoWindow.raise_()
        # Display which seat has been selected
        self.SeatIDOutput.setText("row " + str(row) + " col " + str(column))

        # Enable/disable the Book button
        if self.SeatAvailable(seatId,self.performanceId):
            self.Book_PushButton.setEnabled(True)
        else:
            self.Book_PushButton.setEnabled(False)

    def Booking_Save(self):
        print("Saved")
        self.maxBookingID = self.maxBookingID + 1
        BookingID = self.maxBookingID
        BookingID = str(BookingID)

        PerfData = self.Performance_comboBox.currentText()
        CustData = self.Cust_comboBox.currentText()

        performances = PerfData.split(" ")
        time = performances[0]
        date = performances[1]
        SQLPerf = "SELECT PerformanceID FROM tPerformance WHERE Performance_Time = '" + time + \
                  "' AND Performance_Date = '" + date + "'"

        name = CustData.split(" ")
        firstname = name[0]
        surname = name[1]
        SQLCust = "SELECT CustomerID FROM tCustomer WHERE First_Name = '" + firstname + "' AND Surname = '" + \
                  surname + "'"

        SeatId = self.seatIdent(self.selectedRow, self.selectedColumn)

        CustTypeData = self.CustomerTypeCombo.currentText()
        Cost = 0
        if CustTypeData == 'Special Guest':
            Cost = SpecialGuest
        elif CustTypeData == 'Standard':
            Cost = Standard
        elif CustTypeData == 'Reduced':
            Cost = Reduced

        self.db_connection.open()
        print(SQLCust)
        CustomerId = -1
        SQLCustEx = self.db_connection.execute(SQLCust).fetchall()
        for cur in SQLCustEx:
            CustomerId = cur[0]
        self.db_connection.close()

        self.db_connection.open()
        print(SQLPerf)
        PerformanceId = -1
        SQLPerfEx = self.db_connection.execute(SQLPerf).fetchall()
        for cur1 in SQLPerfEx:
            PerformanceId = cur1[0]
        self.db_connection.close()

        CostStr = str(Cost)
        BookingIDStr = str(BookingID)
        SeatIdStr = str(SeatId)
        SQLPerfStr = str(PerformanceId)
        SQLCustStr = str(CustomerId)

        # Need to add the SeatID to the statement below
        SQLBooking = "INSERT INTO tBooking VALUES (" + BookingIDStr + "," + SeatIdStr + "," + SQLCustStr + "," + \
                     SQLPerfStr + "," + CostStr + ", '" + CustTypeData + "')"
        print(SQLBooking)
        # Save to booking to database
        self.db_connection.open()
        self.db_connection.execute(SQLBooking)
        self.db_connection.commit()
        self.db_connection.close()

        # update data on display
        self.seatTaken(self.selectedRow, self.selectedColumn, SeatId)

        self.numberOfSeatsAvailable = self.numberOfSeatsAvailable - 1
        self.updateNumberOfSeats()

    def seatTaken(self, row, column, SeatId):
        self.Book_PushButton.setEnabled(False)
        seat = self.seats[SeatId]
        seat.available(False)


if __name__ == "__main__":
    import sys
    test = BookingWindow()
