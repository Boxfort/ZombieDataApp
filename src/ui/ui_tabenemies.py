# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/tabenemies.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EnemyTabContents(object):
    def setupUi(self, EnemyTabContents):
        EnemyTabContents.setObjectName("EnemyTabContents")
        EnemyTabContents.resize(1007, 621)
        self.horizontalLayout = QtWidgets.QHBoxLayout(EnemyTabContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(EnemyTabContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 653, 601))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_8.addWidget(self.label_18)
        self.text_enemy_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.text_enemy_name.setObjectName("text_enemy_name")
        self.verticalLayout_8.addWidget(self.text_enemy_name)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_8.addWidget(self.label_19)
        self.spinner_enemy_health = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinner_enemy_health.setObjectName("spinner_enemy_health")
        self.verticalLayout_8.addWidget(self.spinner_enemy_health)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_8.addWidget(self.label_20)
        self.spinner_enemy_attack = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinner_enemy_attack.setObjectName("spinner_enemy_attack")
        self.verticalLayout_8.addWidget(self.spinner_enemy_attack)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_8.addWidget(self.label_21)
        self.spinner_enemy_defence = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinner_enemy_defence.setObjectName("spinner_enemy_defence")
        self.verticalLayout_8.addWidget(self.spinner_enemy_defence)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_8.addWidget(self.label_22)
        self.spinner_enemy_melee_acc = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinner_enemy_melee_acc.setMaximum(10)
        self.spinner_enemy_melee_acc.setObjectName("spinner_enemy_melee_acc")
        self.verticalLayout_8.addWidget(self.spinner_enemy_melee_acc)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_8.addWidget(self.label_23)
        self.spinner_enemy_ranged_acc = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinner_enemy_ranged_acc.setMaximum(10)
        self.spinner_enemy_ranged_acc.setObjectName("spinner_enemy_ranged_acc")
        self.verticalLayout_8.addWidget(self.spinner_enemy_ranged_acc)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_8.addWidget(self.label_24)
        self.spimner_enemy_speed = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.spimner_enemy_speed.setMaximum(10)
        self.spimner_enemy_speed.setObjectName("spimner_enemy_speed")
        self.verticalLayout_8.addWidget(self.spimner_enemy_speed)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_8.addWidget(self.label_25)
        self.spinner_enemy_spawn_rate = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinner_enemy_spawn_rate.setObjectName("spinner_enemy_spawn_rate")
        self.verticalLayout_8.addWidget(self.spinner_enemy_spawn_rate)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_8.addWidget(self.label_26)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.check_tag_common = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.check_tag_common.setObjectName("check_tag_common")
        self.gridLayout_2.addWidget(self.check_tag_common, 0, 0, 1, 1)
        self.check_tag_millitary = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.check_tag_millitary.setObjectName("check_tag_millitary")
        self.gridLayout_2.addWidget(self.check_tag_millitary, 1, 0, 1, 1)
        self.check_tag_medical = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.check_tag_medical.setObjectName("check_tag_medical")
        self.gridLayout_2.addWidget(self.check_tag_medical, 0, 1, 1, 1)
        self.check_tag_police = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.check_tag_police.setObjectName("check_tag_police")
        self.gridLayout_2.addWidget(self.check_tag_police, 1, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.list_enemies = QtWidgets.QListWidget(EnemyTabContents)
        self.list_enemies.setObjectName("list_enemies")
        self.verticalLayout_7.addWidget(self.list_enemies)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.button_enemy_delete = QtWidgets.QPushButton(EnemyTabContents)
        self.button_enemy_delete.setObjectName("button_enemy_delete")
        self.horizontalLayout_8.addWidget(self.button_enemy_delete)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.button_enemy_new = QtWidgets.QPushButton(EnemyTabContents)
        self.button_enemy_new.setObjectName("button_enemy_new")
        self.horizontalLayout_8.addWidget(self.button_enemy_new)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(EnemyTabContents)
        QtCore.QMetaObject.connectSlotsByName(EnemyTabContents)

    def retranslateUi(self, EnemyTabContents):
        _translate = QtCore.QCoreApplication.translate
        EnemyTabContents.setWindowTitle(_translate("EnemyTabContents", "Form"))
        self.label_18.setText(_translate("EnemyTabContents", "Name"))
        self.label_19.setText(_translate("EnemyTabContents", "Max Health"))
        self.label_20.setText(_translate("EnemyTabContents", "Attack"))
        self.label_21.setText(_translate("EnemyTabContents", "Defence"))
        self.label_22.setText(_translate("EnemyTabContents", "Melee Accuracy"))
        self.label_23.setText(_translate("EnemyTabContents", "Ranged Accuracy"))
        self.label_24.setText(_translate("EnemyTabContents", "Speed"))
        self.label_25.setText(_translate("EnemyTabContents", "Spawn Rate"))
        self.label_26.setText(_translate("EnemyTabContents", "Tags"))
        self.check_tag_common.setText(_translate("EnemyTabContents", "COMMON"))
        self.check_tag_millitary.setText(_translate("EnemyTabContents", "MILLITARY"))
        self.check_tag_medical.setText(_translate("EnemyTabContents", "MEDICAL"))
        self.check_tag_police.setText(_translate("EnemyTabContents", "POLICE"))
        self.button_enemy_delete.setText(_translate("EnemyTabContents", "Delete"))
        self.button_enemy_new.setText(_translate("EnemyTabContents", "New"))
