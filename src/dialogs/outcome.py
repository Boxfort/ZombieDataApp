import sys
from ui.ui_dialogoutcome import Ui_DialogOutcome
from PyQt5 import QtCore, QtWidgets, uic 
from model.outcome import Outcome

class DialogOutcome(QtWidgets.QDialog, Ui_DialogOutcome):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        # Vars
        self.outcome = Outcome()
        self.tag_checks = [
            self.check_tag_common,
            self.check_tag_medical,
            self.check_tag_millitary,
            self.check_tag_police
        ]
        # Connections
        self.combo_action.currentTextChanged.connect(self.on_action_changed)
        self.spinner_chance.valueChanged.connect(self.on_chance_changed)
        self.spinner_eventid.valueChanged.connect(self.on_eventid_changed)
        self.text_outcome_text.textChanged.connect(self.on_outcome_text_changed)
        for check in self.tag_checks:
            check.clicked.connect(self.on_tag_changed)
        # Init
        self.on_action_changed()

    def on_action_changed(self):
        self.outcome.action = self.combo_action.currentText()
        condition = self.outcome.action == "EVENT_TRIGGER"
        self.label_eventid.setEnabled(condition)
        self.spinner_eventid.setEnabled(condition)
        self.label_text.setEnabled(not condition)
        self.text_outcome_text.setEnabled(not condition)
        self.label_tags.setEnabled(not condition)
        for check in self.tag_checks:
            check.setEnabled(not condition)

    def on_outcome_text_changed(self):
        outcome_text = self.text_outcome_text.toPlainText()
        self.outcome.text = outcome_text.split('\n') 

    def on_chance_changed(self):
        self.outcome.chance = self.spinner_chance.value()

    def on_eventid_changed(self):
        self.outcome.data["event_id"] = self.spinner_eventid.value()

    def on_tag_changed(self):
        selected_tags = []
        for check in self.tag_checks:
            if check.isChecked():
                selected_tags.append(check.text())

        self.outcome.data["tags"] = selected_tags

    def set_outcome_fields(self, outcome):
        self.set_combo(self.combo_action, outcome.action)
        self.spinner_chance.setValue(outcome.chance)
        self.text_outcome_text.setPlainText('\n'.join(outcome.text))
        event_id = outcome.data.get("event_id", None)
        if event_id:
            self.spinner_eventid.setValue(event_id)
        for check in self.tag_checks:
            if check.text() in outcome.data.get("tags", []):
                check.setChecked(True)
            else:
                check.setChecked(False)

    def set_combo(self, combo, text):
        index = combo.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
            combo.setCurrentIndex(index)