# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/tabitems.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ItemTabContents(object):
    def setupUi(self, ItemTabContents):
        ItemTabContents.setObjectName("ItemTabContents")
        ItemTabContents.resize(1131, 645)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(ItemTabContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(ItemTabContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 722, 970))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.text_item_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.text_item_name.setObjectName("text_item_name")
        self.verticalLayout_2.addWidget(self.text_item_name)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.text_item_description = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.text_item_description.setMaximumSize(QtCore.QSize(16777215, 50))
        self.text_item_description.setObjectName("text_item_description")
        self.verticalLayout_2.addWidget(self.text_item_description)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.combo_item_type = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.combo_item_type.setObjectName("combo_item_type")
        self.combo_item_type.addItem("")
        self.combo_item_type.addItem("")
        self.combo_item_type.addItem("")
        self.verticalLayout_2.addWidget(self.combo_item_type)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.spinner_item_value = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinner_item_value.setObjectName("spinner_item_value")
        self.verticalLayout_2.addWidget(self.spinner_item_value)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 0, 1, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_durability = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_durability.setObjectName("label_durability")
        self.verticalLayout_2.addWidget(self.label_durability)
        self.spinner_item_durability = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinner_item_durability.setObjectName("spinner_item_durability")
        self.verticalLayout_2.addWidget(self.spinner_item_durability)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_damage = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_damage.setObjectName("label_damage")
        self.verticalLayout_2.addWidget(self.label_damage)
        self.spinner_item_damage = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinner_item_damage.setObjectName("spinner_item_damage")
        self.verticalLayout_2.addWidget(self.spinner_item_damage)
        self.label_ammo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_ammo.setObjectName("label_ammo")
        self.verticalLayout_2.addWidget(self.label_ammo)
        self.combo_item_ammo = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.combo_item_ammo.setObjectName("combo_item_ammo")
        self.combo_item_ammo.addItem("")
        self.combo_item_ammo.addItem("")
        self.combo_item_ammo.addItem("")
        self.combo_item_ammo.addItem("")
        self.verticalLayout_2.addWidget(self.combo_item_ammo)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_defense = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_defense.setObjectName("label_defense")
        self.verticalLayout_2.addWidget(self.label_defense)
        self.spinner_item_defense = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinner_item_defense.setObjectName("spinner_item_defense")
        self.verticalLayout_2.addWidget(self.spinner_item_defense)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_combat_description = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_combat_description.setEnabled(True)
        self.label_combat_description.setObjectName("label_combat_description")
        self.verticalLayout_2.addWidget(self.label_combat_description)
        self.text_item_combat_description = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.text_item_combat_description.setEnabled(True)
        self.text_item_combat_description.setObjectName("text_item_combat_description")
        self.verticalLayout_2.addWidget(self.text_item_combat_description)
        self.check_item_offensive = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.check_item_offensive.setEnabled(True)
        self.check_item_offensive.setObjectName("check_item_offensive")
        self.verticalLayout_2.addWidget(self.check_item_offensive)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table_effects = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.table_effects.setMinimumSize(QtCore.QSize(0, 150))
        self.table_effects.setColumnCount(3)
        self.table_effects.setObjectName("table_effects")
        self.table_effects.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_effects.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_effects.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_effects.setHorizontalHeaderItem(2, item)
        self.table_effects.horizontalHeader().setCascadingSectionResizes(False)
        self.table_effects.verticalHeader().setCascadingSectionResizes(False)
        self.table_effects.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.table_effects)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_item_add_effect = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.button_item_add_effect.setMinimumSize(QtCore.QSize(25, 0))
        self.button_item_add_effect.setObjectName("button_item_add_effect")
        self.verticalLayout.addWidget(self.button_item_add_effect)
        self.button_item_delete_effect = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.button_item_delete_effect.setMinimumSize(QtCore.QSize(25, 0))
        self.button_item_delete_effect.setObjectName("button_item_delete_effect")
        self.verticalLayout.addWidget(self.button_item_delete_effect)
        self.button_item_edit_effect = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.button_item_edit_effect.setObjectName("button_item_edit_effect")
        self.verticalLayout.addWidget(self.button_item_edit_effect)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.list_items = QtWidgets.QListWidget(ItemTabContents)
        self.list_items.setObjectName("list_items")
        self.verticalLayout_3.addWidget(self.list_items)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_delete = QtWidgets.QPushButton(ItemTabContents)
        self.button_delete.setObjectName("button_delete")
        self.horizontalLayout_4.addWidget(self.button_delete)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.button_new = QtWidgets.QPushButton(ItemTabContents)
        self.button_new.setObjectName("button_new")
        self.horizontalLayout_4.addWidget(self.button_new)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)

        self.retranslateUi(ItemTabContents)
        QtCore.QMetaObject.connectSlotsByName(ItemTabContents)

    def retranslateUi(self, ItemTabContents):
        _translate = QtCore.QCoreApplication.translate
        ItemTabContents.setWindowTitle(_translate("ItemTabContents", "Form"))
        self.label.setText(_translate("ItemTabContents", "Name"))
        self.label_2.setText(_translate("ItemTabContents", "Description"))
        self.label_4.setText(_translate("ItemTabContents", "Type"))
        self.combo_item_type.setItemText(0, _translate("ItemTabContents", "WEAPON"))
        self.combo_item_type.setItemText(1, _translate("ItemTabContents", "ARMOUR"))
        self.combo_item_type.setItemText(2, _translate("ItemTabContents", "CONSUMABLE"))
        self.label_5.setText(_translate("ItemTabContents", "Value"))
        self.label_6.setText(_translate("ItemTabContents", "Tags"))
        self.radioButton.setText(_translate("ItemTabContents", "COMMON"))
        self.radioButton_2.setText(_translate("ItemTabContents", "MILLITARY "))
        self.radioButton_4.setText(_translate("ItemTabContents", "MEDICAL"))
        self.radioButton_3.setText(_translate("ItemTabContents", "POLICE"))
        self.label_durability.setText(_translate("ItemTabContents", "Durability"))
        self.label_7.setText(_translate("ItemTabContents", "Weapon"))
        self.label_damage.setText(_translate("ItemTabContents", "Damage"))
        self.label_ammo.setText(_translate("ItemTabContents", "Ammo"))
        self.combo_item_ammo.setItemText(0, _translate("ItemTabContents", "NONE"))
        self.combo_item_ammo.setItemText(1, _translate("ItemTabContents", "PISTOL"))
        self.combo_item_ammo.setItemText(2, _translate("ItemTabContents", "RIFLE"))
        self.combo_item_ammo.setItemText(3, _translate("ItemTabContents", "SHOTGUN"))
        self.label_9.setText(_translate("ItemTabContents", "Armour"))
        self.label_defense.setText(_translate("ItemTabContents", "Defense"))
        self.label_8.setText(_translate("ItemTabContents", "Consumable"))
        self.label_combat_description.setText(_translate("ItemTabContents", "Combat Description"))
        self.check_item_offensive.setText(_translate("ItemTabContents", "Is Offensive"))
        self.label_10.setText(_translate("ItemTabContents", "Effects"))
        item = self.table_effects.horizontalHeaderItem(0)
        item.setText(_translate("ItemTabContents", "Effect"))
        item = self.table_effects.horizontalHeaderItem(1)
        item.setText(_translate("ItemTabContents", "Value"))
        item = self.table_effects.horizontalHeaderItem(2)
        item.setText(_translate("ItemTabContents", "Duration"))
        self.button_item_add_effect.setText(_translate("ItemTabContents", "+"))
        self.button_item_delete_effect.setText(_translate("ItemTabContents", "-"))
        self.button_item_edit_effect.setText(_translate("ItemTabContents", "..."))
        self.button_delete.setText(_translate("ItemTabContents", "Delete"))
        self.button_new.setText(_translate("ItemTabContents", "New"))
