import os
import sys

from ui.ui_tabenemies import Ui_EnemyTabContents
from PyQt5 import QtCore, QtWidgets, uic 

class EnemyTab(QtWidgets.QWidget, Ui_EnemyTabContents):
    def __init__(self):
        super().__init__()
        self.setupUi(self)