import sys
from ui.ui_dialogeffect import Ui_DialogEffect
from model.effect import Effect
from PyQt5 import QtCore, QtWidgets, uic 

class DialogEffect(QtWidgets.QDialog, Ui_DialogEffect):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        # Vars
        self.effect = Effect()
        # Connections
        self.combo_effect.currentTextChanged.connect(self.on_effect_type_changed)
        self.spinner_chance.valueChanged.connect(self.on_spinner_chance_changed)
        self.spinner_duration.valueChanged.connect(self.on_spinner_duration_changed)
        self.spinner_value.valueChanged.connect(self.on_spinner_value_changed)
        # Init
        self.on_effect_type_changed()
        self.on_spinner_chance_changed()
        self.on_spinner_duration_changed()
        self.on_spinner_value_changed()

    def on_effect_type_changed(self):
        health_condition = not self.combo_effect.currentText() == "HEALTH_EFFECT"
        stunned_condition = not self.combo_effect.currentText() == "STUNNED"

        self.label_duration.setEnabled(health_condition)
        self.spinner_duration.setEnabled(health_condition)
        self.label_amount.setEnabled(stunned_condition)
        self.spinner_value.setEnabled(stunned_condition)
        self.label_chance.setEnabled(health_condition)
        self.spinner_chance.setEnabled(health_condition)
        
        self.effect.status_effect = self.combo_effect.currentText()

    def on_spinner_chance_changed(self):
        self.effect.chance = self.spinner_chance.value()

    def on_spinner_duration_changed(self):
        self.effect.duration = self.spinner_duration.value()

    def on_spinner_value_changed(self):
        self.effect.value = self.spinner_value.value()