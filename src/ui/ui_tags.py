# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/tags.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tags(object):
    def setupUi(self, tags):
        tags.setObjectName("tags")
        tags.resize(400, 128)
        self.gridLayout = QtWidgets.QGridLayout(tags)
        self.gridLayout.setObjectName("gridLayout")
        self.check_medical = QtWidgets.QCheckBox(tags)
        self.check_medical.setObjectName("check_medical")
        self.gridLayout.addWidget(self.check_medical, 4, 1, 1, 1)
        self.check_residential = QtWidgets.QCheckBox(tags)
        self.check_residential.setObjectName("check_residential")
        self.gridLayout.addWidget(self.check_residential, 3, 1, 1, 1)
        self.check_food = QtWidgets.QCheckBox(tags)
        self.check_food.setObjectName("check_food")
        self.gridLayout.addWidget(self.check_food, 5, 1, 1, 1)
        self.check_police = QtWidgets.QCheckBox(tags)
        self.check_police.setObjectName("check_police")
        self.gridLayout.addWidget(self.check_police, 4, 0, 1, 1)
        self.check_millitary = QtWidgets.QCheckBox(tags)
        self.check_millitary.setObjectName("check_millitary")
        self.gridLayout.addWidget(self.check_millitary, 5, 0, 1, 1)
        self.check_common = QtWidgets.QCheckBox(tags)
        self.check_common.setObjectName("check_common")
        self.gridLayout.addWidget(self.check_common, 3, 0, 1, 1)
        self.check_fuel = QtWidgets.QCheckBox(tags)
        self.check_fuel.setObjectName("check_fuel")
        self.gridLayout.addWidget(self.check_fuel, 6, 0, 1, 1)
        self.check_guns = QtWidgets.QCheckBox(tags)
        self.check_guns.setObjectName("check_guns")
        self.gridLayout.addWidget(self.check_guns, 6, 1, 1, 1)

        self.retranslateUi(tags)
        QtCore.QMetaObject.connectSlotsByName(tags)

    def retranslateUi(self, tags):
        _translate = QtCore.QCoreApplication.translate
        tags.setWindowTitle(_translate("tags", "Form"))
        self.check_medical.setText(_translate("tags", "MEDICAL"))
        self.check_residential.setText(_translate("tags", "RESIDENTIAL"))
        self.check_food.setText(_translate("tags", "FOOD"))
        self.check_police.setText(_translate("tags", "POLICE"))
        self.check_millitary.setText(_translate("tags", "MILITARY"))
        self.check_common.setText(_translate("tags", "COMMON"))
        self.check_fuel.setText(_translate("tags", "FUEL"))
        self.check_guns.setText(_translate("tags", "GUNS"))
