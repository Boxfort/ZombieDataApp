import sys
from PyQt5 import QtCore, QtWidgets, uic

from ui.ui_mainwindow import Ui_ZombieData
from model.item import Item

class MainWindow(QtWidgets.QMainWindow, Ui_ZombieData):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # Button connections
        self.button_new.clicked.connect(self.on_new_item_pressed)
        self.button_delete.clicked.connect(self.on_delete_item_pressed)

    def on_new_item_pressed(self):
        item = Item()
        self.list_items.addItem("Item")
        self.list_items.item(self.list_items.count()-1).setSelected(True)
        self.set_item_fields(item)

    def on_delete_item_pressed(self):
        print("Delete")

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
