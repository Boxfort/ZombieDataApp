import sys
from ui.ui_dialogoption import Ui_DialogOption
from PyQt5 import QtCore, QtWidgets, uic 

class DialogOption(QtWidgets.QDialog, Ui_DialogOption):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)