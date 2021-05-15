import sys
from ui.ui_dialogoutcome import Ui_DialogOutcome
from PyQt5 import QtCore, QtWidgets, uic 
from model.outcome import Outcome
from widgets.tags import TagsWidget

class DialogOutcome(QtWidgets.QDialog, Ui_DialogOutcome):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        # Vars
        self.outcome = Outcome()
        # Create tags widget
        self.tags_widget = TagsWidget(self, self.on_tag_changed)
        self.container_tags.addWidget(self.tags_widget)
        # Connections
        self.combo_action.currentTextChanged.connect(self.on_action_changed)
        self.spinner_chance.valueChanged.connect(self.on_chance_changed)
        self.spinner_eventid.valueChanged.connect(self.on_eventid_changed)
        self.text_outcome_text.textChanged.connect(self.on_outcome_text_changed)
        self.button_add_enemy.clicked.connect(self.on_add_enemy_pressed)
        self.button_remove_enemy.clicked.connect(self.on_remove_enemy_pressed)
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

    def on_outcome_text_changed(self):
        outcome_text = self.text_outcome_text.toPlainText()
        self.outcome.text = outcome_text.split('\n') 

    def on_chance_changed(self):
        self.outcome.chance = self.spinner_chance.value()

    def on_eventid_changed(self):
        self.outcome.data["event_id"] = self.spinner_eventid.value()

    def on_tag_changed(self, tags):
        self.outcome.data["tags"] = tags

    def set_outcome_fields(self, outcome):
        self.outcome = outcome
        self.set_combo(self.combo_action, outcome.action)
        self.spinner_chance.setValue(outcome.chance)
        self.text_outcome_text.setPlainText('\n'.join(outcome.text))
        event_id = outcome.data.get("event_id", None)
        if event_id:
            self.spinner_eventid.setValue(event_id)
        self.tags_widget.set_tags(outcome.data.get("tags", []))
        for id in outcome.data.get("enemies", []):
            self.list_enemies.addItem(str(id))
            self.list_enemies.item(self.list_enemies.count()-1).setSelected(True)
            self.list_enemies.setCurrentRow(self.list_enemies.count()-1)


    def set_combo(self, combo, text):
        index = combo.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
            combo.setCurrentIndex(index)

    def on_add_enemy_pressed(self):
        self.list_enemies.addItem(str(self.spinner_enemy_id.value()))
        self.list_enemies.item(self.list_enemies.count()-1).setSelected(True)
        self.list_enemies.setCurrentRow(self.list_enemies.count()-1)
        enemies = self.outcome.data.get("enemies", [])
        enemies.append(self.spinner_enemy_id.value())
        self.outcome.data["enemies"] = enemies

    def on_remove_enemy_pressed(self):
        if self.list_enemies.currentRow() == -1:
            print("No items")
            return

        selected_idx = self.list_enemies.currentRow()
        self.list_enemies.takeItem(self.list_enemies.currentRow())
        enemies = self.outcome.data.get("enemies", [])
        print(enemies)
        enemies.pop(selected_idx)
        print(enemies)
        self.outcome.data["enemies"] = enemies
        if self.list_enemies.count() > 0:
            self.list_enemies.item(self.list_enemies.currentRow()).setSelected(True)