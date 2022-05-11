from ChoiceMenuWindow import *
from RecordsWindow import *
from BookingWindow import *
from SQLServerAccess import *

# To convert a UI to a python file:
#   pyuic5 -x "Car Park Qt Designer".ui -o "Car Park Qt Designer".py

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    choices = ChoiceMenuWindow()
    choices.show()
    sys.exit(app.exec_())
