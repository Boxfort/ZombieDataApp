# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ZombieData(object):
    def setupUi(self, ZombieData):
        ZombieData.setObjectName("ZombieData")
        ZombieData.resize(826, 617)
        self.centralwidget = QtWidgets.QWidget(ZombieData)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 791, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.listWidget = QtWidgets.QListWidget(self.tab_1)
        self.listWidget.setGeometry(QtCore.QRect(530, 10, 251, 471))
        self.listWidget.setObjectName("listWidget")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_1)
        self.scrollArea.setGeometry(QtCore.QRect(20, 10, 501, 511))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 485, 760))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.name_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_text.setObjectName("name_text")
        self.verticalLayout_2.addWidget(self.name_text)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.description_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.description_text.setMaximumSize(QtCore.QSize(16777215, 50))
        self.description_text.setObjectName("description_text")
        self.verticalLayout_2.addWidget(self.description_text)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.type_combo = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.type_combo.setObjectName("type_combo")
        self.type_combo.addItem("")
        self.type_combo.addItem("")
        self.type_combo.addItem("")
        self.verticalLayout_2.addWidget(self.type_combo)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.value_spin = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.value_spin.setObjectName("value_spin")
        self.verticalLayout_2.addWidget(self.value_spin)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.radioButton_4 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
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
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.damage_spin = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.damage_spin.setObjectName("damage_spin")
        self.verticalLayout_2.addWidget(self.damage_spin)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.durability_spin = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.durability_spin.setObjectName("durability_spin")
        self.verticalLayout_2.addWidget(self.durability_spin)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.ammo_combo = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.ammo_combo.setObjectName("ammo_combo")
        self.ammo_combo.addItem("")
        self.ammo_combo.addItem("")
        self.ammo_combo.addItem("")
        self.ammo_combo.addItem("")
        self.verticalLayout_2.addWidget(self.ammo_combo)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.effects_list = QtWidgets.QListView(self.scrollAreaWidgetContents)
        self.effects_list.setObjectName("effects_list")
        self.horizontalLayout.addWidget(self.effects_list)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.effects_add = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.effects_add.setMinimumSize(QtCore.QSize(25, 0))
        self.effects_add.setObjectName("effects_add")
        self.verticalLayout.addWidget(self.effects_add)
        self.effects_remove = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.effects_remove.setMinimumSize(QtCore.QSize(25, 0))
        self.effects_remove.setObjectName("effects_remove")
        self.verticalLayout.addWidget(self.effects_remove)
        self.effects_edit = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.effects_edit.setObjectName("effects_edit")
        self.verticalLayout.addWidget(self.effects_edit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(700, 490, 80, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 489, 80, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        ZombieData.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ZombieData)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        ZombieData.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ZombieData)
        self.statusbar.setObjectName("statusbar")
        ZombieData.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(ZombieData)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(ZombieData)
        self.actionLoad.setObjectName("actionLoad")
        self.actionExit = QtWidgets.QAction(ZombieData)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ZombieData)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ZombieData)

    def retranslateUi(self, ZombieData):
        _translate = QtCore.QCoreApplication.translate
        ZombieData.setWindowTitle(_translate("ZombieData", "ZombieData"))
        self.label.setText(_translate("ZombieData", "Name"))
        self.label_2.setText(_translate("ZombieData", "Description"))
        self.label_4.setText(_translate("ZombieData", "Type"))
        self.type_combo.setItemText(0, _translate("ZombieData", "WEAPON"))
        self.type_combo.setItemText(1, _translate("ZombieData", "CONSUMABLE"))
        self.type_combo.setItemText(2, _translate("ZombieData", "ARMOUR"))
        self.label_5.setText(_translate("ZombieData", "Value"))
        self.label_3.setText(_translate("ZombieData", "Icon Slug"))
        self.lineEdit_3.setPlaceholderText(_translate("ZombieData", "icon_itemname"))
        self.label_6.setText(_translate("ZombieData", "Tags"))
        self.radioButton_4.setText(_translate("ZombieData", "MEDICAL"))
        self.radioButton.setText(_translate("ZombieData", "COMMON"))
        self.radioButton_3.setText(_translate("ZombieData", "FOOD"))
        self.radioButton_2.setText(_translate("ZombieData", "MILLITARY "))
        self.label_7.setText(_translate("ZombieData", "Weapon"))
        self.label_8.setText(_translate("ZombieData", "Damage"))
        self.label_9.setText(_translate("ZombieData", "Durability"))
        self.label_11.setText(_translate("ZombieData", "Ammo"))
        self.ammo_combo.setItemText(0, _translate("ZombieData", "NONE"))
        self.ammo_combo.setItemText(1, _translate("ZombieData", "PISTOL"))
        self.ammo_combo.setItemText(2, _translate("ZombieData", "RIFLE"))
        self.ammo_combo.setItemText(3, _translate("ZombieData", "SHOTGUN"))
        self.label_10.setText(_translate("ZombieData", "Effects"))
        self.effects_add.setText(_translate("ZombieData", "+"))
        self.effects_remove.setText(_translate("ZombieData", "-"))
        self.effects_edit.setText(_translate("ZombieData", "..."))
        self.pushButton.setText(_translate("ZombieData", "New"))
        self.pushButton_2.setText(_translate("ZombieData", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("ZombieData", "Items"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ZombieData", "Enemies"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ZombieData", "Events"))
        self.menuFile.setTitle(_translate("ZombieData", "File"))
        self.actionSave.setText(_translate("ZombieData", "Save"))
        self.actionLoad.setText(_translate("ZombieData", "Load"))
        self.actionExit.setText(_translate("ZombieData", "Exit"))
