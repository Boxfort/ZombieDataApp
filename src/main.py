import sys
import json
from PyQt5 import QtCore, QtWidgets, uic

from ui.ui_mainwindow import Ui_ZombieData
from model.item import Item

class MainWindow(QtWidgets.QMainWindow, Ui_ZombieData):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # Vars
        self.items = []
        # Connections
        self.button_new.clicked.connect(self.on_new_item_pressed)
        self.button_delete.clicked.connect(self.on_delete_item_pressed)
        self.list_items.itemClicked.connect(self.on_item_list_pressed)
        self.actionSave.triggered.connect(self.on_save_action_pressed)

    def on_save_action_pressed(self):
        print("Saving...")
        item_dict = {}
        for (i, x) in enumerate(self.items):
            x.id = i
            item_dict[i] = x
        with open('items.txt', 'w') as outfile:
            json.dump(item_dict, outfile, default=lambda o: o.__dict__, indent=4)


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

        selected_idx = self.list_items.currentRow()
        self.list_items.takeItem(self.list_items.currentRow())
        self.items.pop(selected_idx)
        if self.list_items.count() > 0:
            if self.list_items.currentRow() == 0:
                self.list_items.item(0).setSelected(True)
            else:    
                self.list_items.item(self.list_items.currentRow()-1).setSelected(True)
            selected_idx = self.list_items.currentRow()
            self.set_item_fields(self.items[selected_idx])

    def on_item_list_pressed(self):
        selected_idx = self.list_items.currentRow()
        self.set_item_fields(self.items[selected_idx])

    def set_item_fields(self, item):
        self.text_item_name.setText(item.name)
        self.text_item_description.setText(item.description)
        self.set_combo(self.combo_item_type, item.type)
        self.spinner_item_value.setValue(item.value)
        self.set_weapon_fields_enabled(self.combo_item_type.currentText == "WEAPON")

    def set_combo(self, combo, text):
        index = combo.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
            combo.setCurrentIndex(index)

    def set_weapon_fields_enabled(self, enabled):
        self.spinner_item_damage.setEnabled(enabled)
        self.spinner_item_durability.setEnabled(enabled)
        self.combo_item_ammo.setEnabled(enabled)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
