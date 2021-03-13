import os
import sys

from ui.ui_tabitems import Ui_ItemTabContents
from PyQt5 import QtCore, QtWidgets, uic 
from model.item import Item
from model.effect import Effect
from dialogs.effect import DialogEffect

class ItemTab(QtWidgets.QWidget, Ui_ItemTabContents):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
               # Vars
        self.items = []
        # Table 
        header = self.table_effects.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.table_effects.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Connections
        self.button_new.clicked.connect(self.on_new_item_pressed)
        self.button_delete.clicked.connect(self.on_delete_item_pressed)
        self.list_items.itemClicked.connect(self.on_item_list_pressed)
        self.button_item_add_effect.clicked.connect(self.on_item_add_effect_pressed)
        # Create an item
        self.on_new_item_pressed()

    def on_new_item_pressed(self):
        item = Item()
        self.list_items.addItem("Item")
        self.list_items.item(self.list_items.count()-1).setSelected(True)
        self.list_items.setCurrentRow(self.list_items.count()-1)
        self.items.append(item)
        self.set_item_fields(item)

    def on_delete_item_pressed(self):
        if self.list_items.currentRow() == -1:
            print("No items")
            return
        if self.list_items.count() <= 1:
            print("Don't delete last item")
            return

        selected_idx = self.list_items.currentRow()
        self.list_items.takeItem(self.list_items.currentRow())
        self.items.pop(selected_idx)
        if self.list_items.count() > 0:
            self.list_items.item(self.list_items.currentRow()).setSelected(True)
            self.set_item_fields(self.get_selected_item())

    def on_item_list_pressed(self):
        self.set_item_fields(self.get_selected_item())

    def on_item_add_effect_pressed(self):
        print("show dialog")
        effect_dialog = DialogEffect(self)
        if effect_dialog.exec_():
            # Create the UI element
            rowCount = self.table_effects.rowCount()
            self.table_effects.insertRow(rowCount)
            self.table_effects.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(effect_dialog.combo_effect.currentText()))
            self.table_effects.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(str(effect_dialog.spinner_value.value())))
            # Create the actual data
            effect = Effect()
            effect.status_effect = effect_dialog.combo_effect.currentText()
            effect.value = effect_dialog.spinner_value.value()
            if effect_dialog.spinner_duration.isEnabled:
                effect.duration = effect_dialog.spinner_duration.value()
            # Add effect data to the item
            item = self.get_selected_item()
            item.effects.append(effect)

    def set_item_fields(self, item):
        self.text_item_name.setText(item.name)
        self.text_item_description.setText(item.description)
        self.set_combo(self.combo_item_type, item.type)
        self.spinner_item_value.setValue(item.value)
        self.set_weapon_fields_enabled(self.combo_item_type.currentText() == "WEAPON")

    def set_combo(self, combo, text):
        index = combo.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
            combo.setCurrentIndex(index)

    def set_weapon_fields_enabled(self, enabled):
        self.spinner_item_damage.setEnabled(enabled)
        self.spinner_item_durability.setEnabled(enabled)
        self.combo_item_ammo.setEnabled(enabled)

    def get_selected_item(self):
        selected_idx = self.list_items.currentRow()
        return self.items[selected_idx]
