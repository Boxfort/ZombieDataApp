import os
import sys

from ui.ui_tabenemies import Ui_EnemyTabContents
from PyQt5 import QtCore, QtWidgets, uic 
from model.enemy import Enemy

class EnemyTab(QtWidgets.QWidget, Ui_EnemyTabContents):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Vars
        self.enemies = []
        # Connections
        self.button_enemy_new.clicked.connect(self.on_new_enemy_pressed)
        self.button_enemy_delete.clicked.connect(self.on_delete_enemy_pressed)
        self.list_enemies.itemClicked.connect(self.on_enemy_list_pressed)
        # Init
        self.on_new_enemy_pressed()

    def on_new_enemy_pressed(self):
        enemy = Enemy()
        self.list_enemies.addItem("")
        self.list_enemies.item(self.list_enemies.count()-1).setSelected(True)
        self.list_enemies.setCurrentRow(self.list_enemies.count()-1)
        self.enemies.append(enemy)
        self.set_enemy_fields(enemy)

    def on_delete_enemy_pressed(self):
        if self.list_enemies.currentRow() == -1:
            print("No items")
            return
        if self.list_enemies.count() <= 1:
            print("Don't delete last item")
            return

        selected_idx = self.list_enemies.currentRow()
        self.list_enemies.takeItem(self.list_enemies.currentRow())
        self.items.pop(selected_idx)
        if self.list_enemies.count() > 0:
            self.list_enemies.item(self.list_enemies.currentRow()).setSelected(True)
            self.set_enemy_fields(self.get_selected_item())

    def on_enemy_list_pressed(self):
        self.set_enemy_fields(self.get_selected_enemy())

    def get_selected_enemy(self):
        selected_idx = self.list_enemies.currentRow()
        return self.enemies[selected_idx]

    def set_enemy_fields(self, enemy):
        pass