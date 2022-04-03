from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SeatLabel(QLabel):
    """Subclass a QLabel so we can get the mouse press event

    see https://stackoverflow.com/questions/60311219/easiest-way-to-subclass-a-widget-in-python-for-use-with-qt-designer
    """
    clicked = pyqtSignal()

    def __init__(self, first_label):
        QLabel.__init__(self, first_label)

    def mousePressEvent(self, event):
        self.clicked.emit()
