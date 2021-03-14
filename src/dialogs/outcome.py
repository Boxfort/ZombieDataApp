import sys
from ui.ui_dialogoutcome import Ui_DialogOutcome
from PyQt5 import QtCore, QtWidgets, uic 

class DialogOutcome(QtWidgets.QDialog, Ui_DialogOutcome):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        # Vars
        self.tag_checks = [
            self.check_tag_common,
            self.check_tag_medical,
            self.check_tag_millitary,
            self.check_tag_police
        ]
        # Connections
        self.combo_action.currentTextChanged.connect(self.on_action_changed)
        # Init
        self.on_action_changed()

    def on_action_changed(self):
        condition = self.combo_action.currentText() == "EVENT_TRIGGER"
        self.label_eventid.setEnabled(condition)
        self.spinner_eventid.setEnabled(condition)
        self.label_tags.setEnabled(not condition)
        for check in self.tag_checks:
            check.setEnabled(not condition)