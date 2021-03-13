import sys
from ui.ui_dialogeffect import Ui_DialogEffect
from PyQt5 import QtCore, QtWidgets, uic 

class DialogEffect(QtWidgets.QDialog, Ui_DialogEffect):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.combo_effect.currentTextChanged.connect(self.on_effect_type_changed)

    def on_effect_type_changed(self):
        duration_condition = not self.combo_effect.currentText() == "HEALTH_EFFECT"
        value_condition = not self.combo_effect.currentText() == "STUNNED"

        self.label_duration.setEnabled(duration_condition)
        self.spinner_duration.setEnabled(duration_condition)
        self.label_amount.setEnabled(value_condition)
        self.spinner_value.setEnabled(value_condition)