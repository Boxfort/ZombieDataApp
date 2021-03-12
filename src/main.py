import sys
from PyQt5 import QtWidgets, uic

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
        print("Create")
        item = Item()
        self.set_item_fields(item)

    def on_delete_item_pressed(self):
        print("Delete")

    def set_item_fields(self, item):
        self.name_text.setText("fancy")
        pass


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
