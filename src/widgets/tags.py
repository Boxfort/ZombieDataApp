import sys
from ui.ui_tags import Ui_tags
from dialogs.effect import DialogEffect
from PyQt5 import QtCore, QtWidgets, uic 
from model.attack import Attack

class TagsWidget(QtWidgets.QWidget, Ui_tags):
    # Callback to recieve the tags when changed
    def __init__(self, parent, callback):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.callback = callback
        self.tag_checks = [
            self.check_common,
            self.check_food,
            self.check_fuel,
            self.check_guns,
            self.check_medical,
            self.check_millitary,
            self.check_police,
            self.check_residential
        ]
        for check in self.tag_checks:
            check.clicked.connect(self.on_tag_changed)


    def on_tag_changed(self):
        selected_tags = self.get_selected_tags()
        self.callback(selected_tags)


    def set_tags(self, tags):
        for check in self.tag_checks:
            if check.text() in tags:
                check.setChecked(True)
            else:
                check.setChecked(False)


    # Returns tags in an array
    def get_selected_tags(self):
        selected_tags = []
        for check in self.tag_checks:
            if check.isChecked():
                selected_tags.append(check.text())
        return selected_tags