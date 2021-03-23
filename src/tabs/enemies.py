import os
import sys
import json

from ui.ui_tabenemies import Ui_EnemyTabContents
from PyQt5 import QtCore, QtWidgets, uic 
from model.enemy import Enemy
from model.attack import Attack
from model.effect import Effect
from dialogs.attack import DialogAttack

class EnemyTab(QtWidgets.QWidget, Ui_EnemyTabContents):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Vars
        self.filename = None
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
        self.text_sprite_slug.textChanged.connect(self.on_sprite_slug_changed)
        self.spinner_enemy_defence.valueChanged.connect(self.on_enemy_defence_changed)
        self.spinner_enemy_health.valueChanged.connect(self.on_enemy_health_changed)
        self.spinner_enemy_melee_acc.valueChanged.connect(self.on_enemy_melee_changed)
        self.spinner_enemy_ranged_acc.valueChanged.connect(self.on_enemy_ranged_changed)
        self.spinner_enemy_spawn_rate.valueChanged.connect(self.on_enemy_spawn_rate_changed)
        self.button_attack_add.clicked.connect(self.on_add_attack_pressed)
        self.button_attack_remove.clicked.connect(self.on_delete_attack_pressed)
        self.button_attack_edit.clicked.connect(self.on_edit_attack_pressed)
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
    
    def on_sprite_slug_changed(self):
        self.get_selected_enemy().sprite_slug = self.text_sprite_slug.text()

    def get_selected_enemy(self):
        selected_idx = self.list_enemies.currentRow()
        return self.enemies[selected_idx]

    def set_enemy_fields(self, enemy):
        self.text_enemy_name.setText(enemy.name)
        self.text_sprite_slug.setText(enemy.sprite_slug)
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
        self.table_attacks.setRowCount(0)
        for attack in enemy.attacks:
            self.add_enemy_attack(attack)

    def on_enemy_name_changed(self):
        enemy_name = self.text_enemy_name.text()
        self.list_enemies.currentItem().setText(enemy_name)
        self.get_selected_enemy().name = enemy_name

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
        selected_tags = []
        for check in self.tag_checks:
            if check.isChecked():
                selected_tags.append(check.text())
        self.get_selected_enemy().tags = selected_tags
        print(selected_tags)


    def add_enemy_attack(self, attack):
        # Add to the table
        rowCount = self.table_attacks.rowCount()
        self.table_attacks.insertRow(rowCount)
        self.table_attacks.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(str(attack.chance)))
        self.table_attacks.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(str(attack.damage)))
        self.table_attacks.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(str(attack.is_ranged)))
        self.table_attacks.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(', '.join(map(lambda x: x.status_effect, attack.effects))))

    def on_add_attack_pressed(self):
        attack_dialog = DialogAttack(self)
        if attack_dialog.exec_():
            self.add_enemy_attack(attack_dialog.attack)
            self.get_selected_enemy().attacks.append(attack_dialog.attack)

    def on_delete_attack_pressed(self):
        idx = self.table_attacks.currentRow()
        if idx != -1:
            self.table_attacks.removeRow(idx)
            self.get_selected_enemy().attacks.pop(idx)

    def on_edit_attack_pressed(self):
        idx = self.table_attacks.currentRow()
        if idx != -1:
            selected_attack = self.get_selected_enemy().attacks[idx]
            attack_dialog = DialogAttack(self)
            attack_dialog.setWindowTitle("Edit Attack")
            # Set fields to existing values
            attack_dialog.set_fields(selected_attack)
            if attack_dialog.exec_():
                selected_attack.is_ranged = attack_dialog.attack.is_ranged
                selected_attack.damage = attack_dialog.attack.damage
                selected_attack.chance = attack_dialog.attack.chance
                selected_attack.effects = attack_dialog.attack.effects
                selected_attack.attack_type = attack_dialog.attack.attack_type
                self.table_event_options.item(idx, 0).setText(str(selected_attack.chance))
                self.table_event_options.item(idx, 0).setText(str(selected_attack.damage))
                self.table_event_options.item(idx, 0).setText(str(selected_attack.is_ranged))
                self.table_event_options.item(idx, 0).setText(', '.join(map(lambda x: x.status_effect, selected_attack.effects)))


    def save(self, save_as = False):
        print("Saving Enemies...")
        enemy_dict = {}
        for (i, x) in enumerate(self.enemies):
            x.id = i
            enemy_dict[i] = x

        if save_as or not self.filename:
            filename = self.get_save_filename()
            if filename:
                self.filename = filename

        if self.filename:
            with open(self.filename, 'w+') as outfile:
                json.dump(enemy_dict, outfile, default=lambda o: o.__dict__, indent=4)
        else: 
            print("Directory not selected.")


    def load(self):
        filename = self.get_load_filename()
        if not filename:
            return

        self.filename = filename

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
            for attackData in enemy_data.get("attacks", []):
                attack = Attack()
                attack.attack_type = attackData["attack_type"]
                attack.chance = attackData["chance"]
                attack.damage = attackData["damage"]
                attack.is_ranged = attackData["is_ranged"]
                for effectData in attackData["effects"]:
                    effect = Effect()
                    effect.chance = effectData["chance"]
                    effect.duration = effectData["duration"]
                    effect.status_effect = effectData["status_effect"]
                    effect.value = effectData["value"]
                    attack.effects.append(effect)
                enemy.attacks.append(attack)
            enemies.append(enemy)

        if enemies:
            self.enemies = enemies
            self.list_enemies.clear()
            for enemy in self.enemies:
                self.list_enemies.addItem(enemy.name)
                self.list_enemies.setCurrentRow(self.list_enemies.count()-1)
                self.list_enemies.item(self.list_enemies.count()-1).setSelected(True)
                self.set_enemy_fields(enemy)

    def get_load_filename(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Load Enemies...",
            os.path.expanduser("~")
        )
        return filename

    def get_save_filename(self):
        filename, a = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Save Enemies...",
            os.path.join(os.path.expanduser("~"), "enemies.json")
        )
        return filename