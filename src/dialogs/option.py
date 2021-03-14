import sys
from ui.ui_dialogoption import Ui_DialogOption
from model.option import Option
from PyQt5 import QtCore, QtWidgets, uic 
from dialogs.outcome import DialogOutcome

class DialogOption(QtWidgets.QDialog, Ui_DialogOption):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        # Vars
        self.option = Option()
        # Table
        header = self.table_outcomes.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.table_outcomes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Connections
        self.text_option_text.textChanged.connect(self.on_text_changed)
        self.button_add_outcome.clicked.connect(self.on_add_outcome_clicked)
        self.button_delete_outcome.clicked.connect(self.on_delete_outcome_clicked)
        self.button_edit_outcome.clicked.connect(self.on_edit_outcome_clicked)

    def on_text_changed(self):
        self.option.text = self.text_option_text.text()

    def set_option_fields(self, option):
        self.text_option_text.setText(option.text)
        self.table_outcomes.setRowCount(0)
        for outcome in option.outcomes:
            self.add_outcome(outcome)

    def add_outcome(self, outcome):
        rowCount = self.table_outcomes.rowCount()
        self.table_outcomes.insertRow(rowCount)
        self.table_outcomes.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(outcome.action))
        self.table_outcomes.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(str(outcome.chance)))
        if outcome.action != "EVENT_TRIGGER":
            if outcome.text:
                self.table_outcomes.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(outcome.text[0]))
        else:
            self.table_outcomes.setItem(rowCount, 2, QtWidgets.QTableWidgetItem("N/A"))

    def on_add_outcome_clicked(self):
        outcome_dialog = DialogOutcome(self)
        if outcome_dialog.exec_():
            outcome = outcome_dialog.outcome
            # Add missing data
            if outcome_dialog.spinner_eventid.isEnabled():
                outcome.data["event_id"] = outcome.data.get("event_id", 0)
            if outcome_dialog.label_tags.isEnabled():
                outcome.data["tags"] = outcome.data.get("tags", [])
            self.add_outcome(outcome)
            self.option.outcomes.append(outcome)


    def on_delete_outcome_clicked(self):
        idx = self.table_outcomes.currentRow()
        if idx != -1:
            self.table_outcomes.removeRow(idx)
            self.option.outcomes.pop(idx)

    def on_edit_outcome_clicked(self):
        idx = self.table_outcomes.currentRow()
        if idx != -1:
            outcome = self.option.outcomes[idx]
            outcome_dialog = DialogOutcome(self)
            outcome_dialog.setWindowTitle("Edit Event Outcome")
            outcome_dialog.set_outcome_fields(outcome)
            if outcome_dialog.exec_():
                outcome.text = outcome_dialog.outcome.text
                outcome.action = outcome_dialog.outcome.action
                outcome.chance = outcome_dialog.outcome.chance
                outcome.data = outcome_dialog.outcome.data
                self.table_outcomes.item(idx, 0).setText(outcome.action)
                self.table_outcomes.item(idx, 1).setText(str(outcome.chance))
                if outcome.action != "EVENT_TRIGGER":
                    if outcome.text:
                        self.table_outcomes.item(idx, 2).setText(outcome.text[0])
                else:
                    self.table_outcomes.item(idx, 2).setText("N/A")
