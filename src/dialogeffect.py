import sys
from ui.ui_dialogeffect import Ui_DialogEffect
from PyQt5 import QtCore, QtWidgets, uic 

class DialogEffect(QtWidgets.QDialog, Ui_DialogEffect):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)