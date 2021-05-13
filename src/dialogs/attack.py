import sys
from ui.ui_dialogattack import Ui_DialogAttack
from dialogs.effect import DialogEffect
from PyQt5 import QtCore, QtWidgets, uic 
from model.attack import Attack

class DialogAttack(QtWidgets.QDialog, Ui_DialogAttack):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        # Vars
        self.attack = Attack()
        # Connections
        self.spinner_chance.valueChanged.connect(self.on_chance_changed)
        self.spinner_damage.valueChanged.connect(self.on_damage_changed)
        self.check_isRanged.clicked.connect(self.on_isRanged_changed)
        self.combo_attack_type.currentTextChanged.connect(self.on_attack_type_changed)
        self.text_projectile_slug.textChanged.connect(self.on_projectile_slug_changed)
        self.button_add_effect.clicked.connect(self.on_add_effect_pressed)
        self.button_remove_effect.clicked.connect(self.on_delete_effect_pressed)
        self.button_edit_effect.clicked.connect(self.on_edit_effect_pressed)
        # Init
        self.on_chance_changed()
        self.on_damage_changed()
        self.on_isRanged_changed()
        self.on_attack_type_changed()
        self.on_projectile_slug_changed()


    def add_item_effect(self, effect):
        # Add to the table
        rowCount = self.table_effects.rowCount()
        self.table_effects.insertRow(rowCount)
        self.table_effects.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(effect.status_effect))
        self.table_effects.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(str(effect.value)))
        if effect.duration != None:
            self.table_effects.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(str(effect.duration)))
        else:
            self.table_effects.setItem(rowCount, 2, QtWidgets.QTableWidgetItem("N/A"))

    def on_add_effect_pressed(self):
        effect_dialog = DialogEffect(self)
        if effect_dialog.exec_():
            self.add_item_effect(effect_dialog.effect)
            self.attack.effects.append(effect_dialog.effect)

    def on_delete_effect_pressed(self):
        idx = self.table_effects.currentRow()
        if idx != -1:
            self.table_effects.removeRow(idx)
            self.attack.effects.pop(idx)

    def on_edit_effect_pressed(self):
        idx = self.table_effects.currentRow()
        if idx != -1:
            selected_effect = self.attack.effects[idx]
            effect_dialog = DialogEffect(self)
            effect_dialog.setWindowTitle("Edit Effect")
            # Set fields to existing values
            self.set_combo(effect_dialog.combo_effect, selected_effect.status_effect)
            effect_dialog.spinner_value.setValue(selected_effect.value)
            effect_dialog.spinner_chance.setValue(selected_effect.chance)
            if selected_effect.duration != None:
                effect_dialog.spinner_duration.setValue(selected_effect.duration)
            if effect_dialog.exec_():
                selected_effect.status_effect = effect_dialog.combo_effect.currentText()
                selected_effect.value = effect_dialog.spinner_value.value()
                self.table_effects.item(idx, 0).setText(selected_effect.status_effect)
                self.table_effects.item(idx, 1).setText(str(selected_effect.value))
                if effect_dialog.spinner_duration.isEnabled():
                    selected_effect.duration = effect_dialog.spinner_duration.value()
                    self.table_effects.item(idx, 2).setText(str(selected_effect.duration))
                else:
                    self.table_effects.item(idx, 2).setText("N/A")

    def set_combo(self, combo, text):
        index = combo.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
            combo.setCurrentIndex(index)

    def on_chance_changed(self):
        self.attack.chance = self.spinner_chance.value()

    def on_damage_changed(self):
        self.attack.damage = self.spinner_damage.value()

    def on_isRanged_changed(self):
        self.attack.is_ranged = self.check_isRanged.isChecked()

    def on_attack_type_changed(self):
        self.attack.attack_type = self.combo_attack_type.currentText()

    def on_projectile_slug_changed(self):
        self.attack.projectile_slug = self.text_projectile_slug.text()

    def set_fields(self, attack):
        self.attack = attack
        self.spinner_damage.setValue(attack.damage)
        self.spinner_chance.setValue(attack.chance)
        self.set_combo(self.combo_attack_type, attack.attack_type)
        self.text_projectile_slug.setText(attack.projectile_slug)
        self.check_isRanged.setChecked(attack.is_ranged)
        for effect in attack.effects:
            self.add_item_effect(effect)