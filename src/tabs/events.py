import os
import sys

from ui.ui_tabevents import Ui_EventTabContents
from PyQt5 import QtCore, QtWidgets, uic 

class EventTab(QtWidgets.QWidget, Ui_EventTabContents):
    def __init__(self):
        super().__init__()
        self.setupUi(self)