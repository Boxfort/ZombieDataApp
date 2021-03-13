# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dialogoption.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogOption(object):
    def setupUi(self, DialogOption):
        DialogOption.setObjectName("DialogOption")
        DialogOption.resize(400, 319)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogOption)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DialogOption)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.combo_action = QtWidgets.QComboBox(DialogOption)
        self.combo_action.setObjectName("combo_action")
        self.combo_action.addItem("")
        self.combo_action.addItem("")
        self.combo_action.addItem("")
        self.verticalLayout.addWidget(self.combo_action)
        self.label_2 = QtWidgets.QLabel(DialogOption)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.spinner_chance = QtWidgets.QSpinBox(DialogOption)
        self.spinner_chance.setObjectName("spinner_chance")
        self.verticalLayout.addWidget(self.spinner_chance)
        self.label_tags = QtWidgets.QLabel(DialogOption)
        self.label_tags.setObjectName("label_tags")
        self.verticalLayout.addWidget(self.label_tags)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(DialogOption)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 1, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(DialogOption)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 1, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(DialogOption)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(DialogOption)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_eventid = QtWidgets.QLabel(DialogOption)
        self.label_eventid.setObjectName("label_eventid")
        self.verticalLayout.addWidget(self.label_eventid)
        self.spinner_eventid = QtWidgets.QSpinBox(DialogOption)
        self.spinner_eventid.setObjectName("spinner_eventid")
        self.verticalLayout.addWidget(self.spinner_eventid)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogOption)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogOption)
        self.buttonBox.accepted.connect(DialogOption.accept)
        self.buttonBox.rejected.connect(DialogOption.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogOption)

    def retranslateUi(self, DialogOption):
        _translate = QtCore.QCoreApplication.translate
        DialogOption.setWindowTitle(_translate("DialogOption", "New Event Option"))
        self.label.setText(_translate("DialogOption", "Action"))
        self.combo_action.setItemText(0, _translate("DialogOption", "ENEMY_ENCOUNTER"))
        self.combo_action.setItemText(1, _translate("DialogOption", "LOOT_ROLL"))
        self.combo_action.setItemText(2, _translate("DialogOption", "EVENT_TRIGGER"))
        self.label_2.setText(_translate("DialogOption", "Chance"))
        self.label_tags.setText(_translate("DialogOption", "Tags"))
        self.radioButton_3.setText(_translate("DialogOption", "MILLITARY"))
        self.radioButton_4.setText(_translate("DialogOption", "POLICE"))
        self.radioButton.setText(_translate("DialogOption", "COMMON"))
        self.radioButton_2.setText(_translate("DialogOption", "MEDICAL"))
        self.label_eventid.setText(_translate("DialogOption", "Event ID"))
