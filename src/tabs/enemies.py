import os
import sys
import json

from ui.ui_tabenemies import Ui_EnemyTabContents
from PyQt5 import QtCore, QtWidgets, uic 
from model.enemy import Enemy

class EnemyTab(QtWidgets.QWidget, Ui_EnemyTabContents):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Vars
        self.enemies = []
        self.tag_checks = [
            self.check_tag_common,
            self.check_tag_medical,
            self.check_tag_millitary,
            self.check_tag_police
        ]
        # Connections
        self.button_enemy_new.clicked.connect(self.on_new_enemy_pressed)
        self.button_enemy_delete.clicked.connect(self.on_delete_enemy_pressed)
        self.list_enemies.itemClicked.connect(self.on_enemy_list_pressed)
        self.text_enemy_name.textChanged.connect(self.on_enemy_name_changed)
        self.spinner_enemy_attack.valueChanged.connect(self.on_enemy_attack_changed)
        self.spinner_enemy_defence.valueChanged.connect(self.on_enemy_defence_changed)
        self.spinner_enemy_health.valueChanged.connect(self.on_enemy_health_changed)
        self.spinner_enemy_melee_acc.valueChanged.connect(self.on_enemy_melee_changed)
        self.spinner_enemy_ranged_acc.valueChanged.connect(self.on_enemy_ranged_changed)
        self.spinner_enemy_spawn_rate.valueChanged.connect(self.on_enemy_spawn_rate_changed)
        for check in self.tag_checks:
            check.clicked.connect(self.on_tag_changed)
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
        print(enemy.tags)
        self.text_enemy_name.setText(enemy.name)
        self.spinner_enemy_attack.setValue(enemy.attack)
        self.spinner_enemy_defence.setValue(enemy.defence)
        self.spinner_enemy_health.setValue(enemy.max_health)
        self.spinner_enemy_melee_acc.setValue(enemy.melee_accuracy)
        self.spinner_enemy_ranged_acc.setValue(enemy.ranged_accuracy)
        self.spinner_enemy_spawn_rate.setValue(enemy.spawn_rate)
        for check in self.tag_checks:
            if check.text() in enemy.tags:
                check.setChecked(True)
            else:
                check.setChecked(False)

    def on_enemy_name_changed(self):
        enemy_name = self.text_enemy_name.text()
        self.list_enemies.currentItem().setText(enemy_name)
        self.get_selected_enemy().name = enemy_name

    def on_enemy_attack_changed(self):
        enemy_attack = self.spinner_enemy_attack.value()
        self.get_selected_enemy().attack = enemy_attack

    def on_enemy_defence_changed(self):
        enemy_defence = self.spinner_enemy_defence.value()
        self.get_selected_enemy().defence = enemy_defence

    def on_enemy_health_changed(self):
        enemy_health = self.spinner_enemy_health.value()
        self.get_selected_enemy().max_health = enemy_health
    
    def on_enemy_melee_changed(self):
        enemy_melee = self.spinner_enemy_melee_acc.value()
        self.get_selected_enemy().melee_accuracy = enemy_melee

    def on_enemy_ranged_changed(self):
        enemy_ranged = self.spinner_enemy_ranged_acc.value()
        self.get_selected_enemy().ranged_accuracy = enemy_ranged

    def on_enemy_spawn_rate_changed(self):
        enemy_spawn_rate = self.spinner_enemy_spawn_rate.value()
        self.get_selected_enemy().spawn_rate = enemy_spawn_rate

    def on_tag_changed(self):
        print("tag changed")
        selected_tags = []
        for check in self.tag_checks:
            if check.isChecked():
                selected_tags.append(check.text())
        self.get_selected_enemy().tags = selected_tags
        print(selected_tags)

    def save(self):
        print("Saving Enemies...")
        filename= self.get_save_filename()
        if filename:
            with open(filename, 'w+') as outfile:
                json.dump(self.enemies, outfile, default=lambda o: o.__dict__, indent=4)
        else: 
            print("Directory not selected.")


    def load(self):
        filename = self.get_load_filename()
        if not filename:
            return

        data = {}
        with open(filename) as json_file:
            data = json.load(json_file)

        enemies = []
        for enemy_data in data.values():
            enemy = Enemy()
            enemy.name = enemy_data["name"]
            enemy.sprite_slug = enemy_data["sprite_slug"]
            enemy.max_health = enemy_data["max_health"]
            enemy.attack = enemy_data["attack"]
            enemy.defence = enemy_data["defence"]
            enemy.melee_accuracy = enemy_data["melee_accuracy"]
            enemy.ranged_accuracy = enemy_data["ranged_accuracy"]
            enemy.speed = enemy_data["speed"]
            enemy.spawn_rate = enemy_data["spawn_rate"]
            enemy.tags = enemy_data["tags"]


        if enemies:
            self.enemies = enemies
            self.list_enemies.clear()
            for enemy in self.enemies:
                self.list_enemies.addItem(enemy.name)
                self.list_enemies.setCurrentRow(self.list_enemies.count()-1)
                self.list_enemies.item(self.list_enemies.count()-1).setSelected(True)
                self.set_enemy_fields(enemy)

    def get_save_filename(self):
        filename, a = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Save Items...",
            os.path.join(os.path.expanduser("~"), "enemies.txt")
        )
        print(a)
        return filename