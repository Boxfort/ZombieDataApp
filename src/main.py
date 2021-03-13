import sys
import os
import json

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from tabs.items import ItemTab
from tabs.enemies import EnemyTab
from tabs.events import EventTab
from ui.ui_mainwindow import Ui_ZombieData

class MainWindow(QtWidgets.QMainWindow, Ui_ZombieData):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # Tabs
        self.item_tab = ItemTab()
        self.tab_items.layout().addWidget(self.item_tab)
        self.enemies_tab = EnemyTab()
        self.tab_enemies.layout().addWidget(self.enemies_tab)
        self.events_tab = EventTab()
        self.tab_events.layout().addWidget(self.events_tab)
        # Connections
        self.actionSave.triggered.connect(self.on_save_action_pressed)
        self.actionLoad.triggered.connect(self.on_load_action_pressed)

    def closeEvent(self, event):
        # TODO: Check for unsaved data
        return
        print("event")
        reply = QtWidgets.QMessageBox.question(self, 'Unsaved Data',
            "There is unsaved data!\n\nAre you sure to quit?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def on_save_action_pressed(self):
        print("Saving...")
        item_dict = {}
        for (i, x) in enumerate(self.items):
            x.id = i
            item_dict[i] = x
        directory = self.get_save_directory()
        if directory:
            with open(os.path.join(directory, 'items.txt'), 'w') as outfile:
                json.dump(item_dict, outfile, default=lambda o: o.__dict__, indent=4)
        else: 
            print("Directory not selected.")

    def on_load_action_pressed(self):
        print("Loading!")

    def get_save_directory(self):
        directory = QFileDialog.getExistingDirectory(
            self,
            "Pick save directory.",
            os.path.expanduser("~"),
            QFileDialog.ShowDirsOnly
        )
        return directory


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
