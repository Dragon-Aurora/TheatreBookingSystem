from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SeatLabel(QLabel):
    """Subclass a QLabel so we can get the mouse press event

    see
    - https://stackoverflow.com/questions/60311219/easiest-way-to-subclass-a-widget-in-python-for-use-with-qt-designer
    - https://stackoverflow.com/questions/962640/pyqt-qlabel-inheriting?rq=1


    """

    # create a qt signal object
    clicked = pyqtSignal()

    def __init__(self, first_label):
        QLabel.__init__(self, first_label)

    def mousePressEvent(self, event):
        #emit the signal
        #to capture the signal use variable.clicked.connect(slotfunction)
        #Slotfunction will get called when you click on a seat label
        self.clicked.emit()
