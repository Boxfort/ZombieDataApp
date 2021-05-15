import os
import sys
import json

from ui.ui_tabitems import Ui_ItemTabContents
from PyQt5 import QtCore, QtWidgets, uic 
from model.item import Item
from model.effect import Effect
from dialogs.effect import DialogEffect
from widgets.tags import TagsWidget

class ItemTab(QtWidgets.QWidget, Ui_ItemTabContents):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Vars
        self.filename = None
        self.items = []
        # Create tags widget
        self.tags_widget = TagsWidget(self, self.on_tag_changed)
        self.container_tags.addWidget(self.tags_widget)
        # Table 
        header = self.table_effects.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.table_effects.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Connections
        self.button_new.clicked.connect(self.on_new_item_pressed)
        self.button_delete.clicked.connect(self.on_delete_item_pressed)
        self.list_items.itemClicked.connect(self.on_item_list_pressed)
        self.button_item_add_effect.clicked.connect(self.on_item_add_effect_pressed)
        self.button_item_delete_effect.clicked.connect(self.on_item_delete_effect_pressed)
        self.button_item_edit_effect.clicked.connect(self.on_item_edit_effect_pressed)
        self.text_item_name.textChanged.connect(self.on_item_name_changed)
        self.text_item_description.textChanged.connect(self.on_item_description_changed)
        self.combo_item_type.currentTextChanged.connect(self.on_combo_item_type_changed)
        self.spinner_item_value.valueChanged.connect(self.on_item_value_changed)
        self.spinner_item_durability.valueChanged.connect(self.on_item_durability_changed)
        self.spinner_item_damage.valueChanged.connect(self.on_item_damage_changed)
        self.spinner_item_defense.valueChanged.connect(self.on_item_defense_changed)
        self.spinner_item_level.valueChanged.connect(self.on_item_level_changed)
        self.combo_rarity.currentTextChanged.connect(self.on_item_rarity_changed)
        self.combo_item_ammo.currentTextChanged.connect(self.on_item_ammo_changed)
        self.combo_item_icon_slug.currentTextChanged.connect(self.on_item_slug_changed)
        self.text_item_combat_description.textChanged.connect(self.on_item_combat_description_changed)
        self.check_item_offensive.stateChanged.connect(self.on_item_offensive_changed)
        self.text_projectile_slug.textChanged.connect(self.on_projectile_slug_changed)
        # Init
        self.on_new_item_pressed()
        self.on_combo_item_type_changed()

    def on_item_name_changed(self):
        name = self.text_item_name.text()
        self.list_items.currentItem().setText(name)
        self.get_selected_item().name = name

    def on_item_description_changed(self):
        description = self.text_item_description.toPlainText()
        self.get_selected_item().description = description

    def on_combo_item_type_changed(self):
        item_type = self.combo_item_type.currentText()
        self.get_selected_item().type = item_type
        weapon_condition = item_type == "WEAPON"
        ammo_condition = item_type == "AMMO"
        consumable_condition = item_type == "CONSUMABLE"
        armour_condition = item_type == "ARMOUR"
        self.label_damage.setEnabled(weapon_condition)
        self.spinner_item_damage.setEnabled(weapon_condition)
        self.combo_item_ammo.setEnabled(weapon_condition or ammo_condition)
        self.label_durability.setEnabled(not consumable_condition)
        self.spinner_item_durability.setEnabled(not consumable_condition)
        self.label_combat_description.setEnabled(consumable_condition)
        self.text_item_combat_description.setEnabled(consumable_condition)
        self.check_item_offensive.setEnabled(consumable_condition)
        self.label_defense.setEnabled(armour_condition)
        self.spinner_item_defense.setEnabled(armour_condition)
        self.text_projectile_slug.setEnabled((consumable_condition or weapon_condition))
        self.label_projectile_slug.setEnabled((consumable_condition or weapon_condition))

    def on_item_value_changed(self):
        item_value = self.spinner_item_value.value()
        self.get_selected_item().value = item_value

    def on_item_durability_changed(self):
        item_durability = self.spinner_item_durability.value()
        self.get_selected_item().data["max_durability"] = item_durability

    def on_item_damage_changed(self):
        item_damage = self.spinner_item_damage.value()
        self.get_selected_item().data["damage"] = item_damage

    def on_item_defense_changed(self):
        item_defense = self.spinner_item_defense.value()
        self.get_selected_item().data["defence"] = item_defense

    def on_item_level_changed(self):
        item_level = self.spinner_item_level.value()
        self.get_selected_item().level = item_level

    def on_item_ammo_changed(self):
        item_ammo = self.combo_item_ammo.currentText()
        self.get_selected_item().data["ammo_type"] = item_ammo

    def on_item_rarity_changed(self):
        item_rarity = self.combo_rarity.currentText()
        self.get_selected_item().rarity = item_rarity

    def on_item_slug_changed(self):
        item_slug = self.combo_item_icon_slug.currentText()
        self.get_selected_item().icon_slug = item_slug

    def on_item_combat_description_changed(self):
        item_combat_description = self.text_item_combat_description.toPlainText()
        self.get_selected_item().data["combat_description"] = item_combat_description

    def on_item_offensive_changed(self):
        item_offensive = self.check_item_offensive.isChecked()
        self.get_selected_item().data["offensive"] = item_offensive

    def on_tag_changed(self, tags):
        self.get_selected_item().tags = tags

    def on_projectile_slug_changed(self):
        self.get_selected_item().data["projectile_slug"] = self.text_projectile_slug.text()

    def on_new_item_pressed(self):
        item = Item()
        self.list_items.addItem("")
        self.list_items.item(self.list_items.count()-1).setSelected(True)
        self.list_items.setCurrentRow(self.list_items.count()-1)
        self.items.append(item)
        self.set_item_fields(item)

    def on_delete_item_pressed(self):
        if self.list_items.currentRow() == -1:
            print("No items")
            return
        if self.list_items.count() <= 1:
            print("Don't delete last item")
            return

        selected_idx = self.list_items.currentRow()
        self.list_items.takeItem(self.list_items.currentRow())
        self.items.pop(selected_idx)
        if self.list_items.count() > 0:
            self.list_items.item(self.list_items.currentRow()).setSelected(True)
            self.set_item_fields(self.get_selected_item())

    def on_item_list_pressed(self):
        self.set_item_fields(self.get_selected_item())

    def on_item_add_effect_pressed(self):
        effect_dialog = DialogEffect(self)
        if effect_dialog.exec_():
            self.add_item_effect(effect_dialog.effect)
            # Add effect data to the item
            item = self.get_selected_item()
            if not item.data.get("effects", None):
                item.data["effects"] = []
            item.data["effects"].append(effect_dialog.effect)      
    
    def add_item_effect(self, effect):
        # Add to the table
        rowCount = self.table_effects.rowCount()
        self.table_effects.insertRow(rowCount)
        self.table_effects.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(effect.status_effect))
        self.table_effects.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(str(effect.value)))
        if effect.duration != None:
            self.table_effects.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(str(effect.duration)))
        else:
            self.table_effects.setItem(rowCount, 2, QtWidgets.QTableWidgetItem("N/A"))

    def on_item_delete_effect_pressed(self):
        idx = self.table_effects.currentRow()
        if idx != -1:
            self.table_effects.removeRow(idx)
            self.get_selected_item().data["effects"].pop(idx)

    def on_item_edit_effect_pressed(self):
        idx = self.table_effects.currentRow()
        if idx != -1:
            selected_effect = self.get_selected_item().data["effects"][idx]
            effect_dialog = DialogEffect(self)
            effect_dialog.setWindowTitle("Edit Effect")
            # Set fields to existing values
            self.set_combo(effect_dialog.combo_effect, selected_effect.status_effect)
            effect_dialog.spinner_value.setValue(selected_effect.value)
            effect_dialog.spinner_chance.setValue(selected_effect.chance)
            if selected_effect.duration != None:
                effect_dialog.spinner_duration.setValue(selected_effect.duration)
            if effect_dialog.exec_():
                selected_effect.status_effect = effect_dialog.combo_effect.currentText()
                selected_effect.value = effect_dialog.spinner_value.value()
                self.table_effects.item(idx, 0).setText(selected_effect.status_effect)
                self.table_effects.item(idx, 1).setText(str(selected_effect.value))
                if effect_dialog.spinner_duration.isEnabled():
                    selected_effect.duration = effect_dialog.spinner_duration.value()
                    self.table_effects.item(idx, 2).setText(str(selected_effect.duration))
                else:
                    self.table_effects.item(idx, 2).setText("N/A")

    def set_item_fields(self, item):
        self.text_item_name.setText(item.name)
        self.text_item_description.setText(item.description)
        self.set_combo(self.combo_item_type, item.type)
        self.set_combo(self.combo_item_icon_slug, item.icon_slug)
        self.set_combo(self.combo_item_ammo, item.data.get("ammo_type", "NONE"))
        self.set_combo(self.combo_rarity, item.rarity)
        self.spinner_item_value.setValue(item.value)
        self.spinner_item_damage.setValue(item.data.get("damage", 0))
        self.spinner_item_defense.setValue(item.data.get("defence", 0))
        self.spinner_item_durability.setValue(item.data.get("max_durability", 0))
        self.spinner_item_level.setValue(item.level)
        combat_description = item.data.get("combat_description", "")
        self.text_item_combat_description.setText(combat_description)
        offensive = item.data.get("offensive", False)
        self.check_item_offensive.setChecked(offensive)
        self.table_effects.setRowCount(0)
        self.text_projectile_slug.setText(item.data.get("projectile_slug", ""))
        self.tags_widget.set_tags(item.tags)
        for effect in item.data.get("effects", []):
            self.add_item_effect(effect)
        # Update type state
        self.on_combo_item_type_changed()

    def set_combo(self, combo, text):
        index = combo.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
            combo.setCurrentIndex(index)

    def get_selected_item(self):
        selected_idx = self.list_items.currentRow()
        return self.items[selected_idx]

    def save(self, save_as = False):
        print("Saving Items...")
        item_dict = {}
        self.fill_missing_item_data()
        for (i, x) in enumerate(self.items):
            x.id = i
            item_dict[i] = x

        if save_as or not self.filename:
            filename = self.get_save_filename()
            if filename:
                self.filename = filename

        if self.filename:
            with open(self.filename, 'w+') as outfile:
                json.dump(item_dict, outfile, default=lambda o: o.__dict__, indent=4)
        else: 
            print("Directory not selected.")

    def fill_missing_item_data(self):
        for item in self.items:
            if item.type != "CONSUMABLE":
                item.data["max_durability"] = item.data.get("max_durability", 0)
            if item.type == "WEAPON":
                item.data["damage"] = item.data.get("damage", 0)
                item.data["ammo_type"] = item.data.get("ammo_type", "NONE")
            elif item.type == "ARMOUR":
                item.data["defence"] = item.data.get("defence", 0)
            elif item.type == "CONSUMABLE":
                item.data["offensive"] = item.data.get("offensive", False)
                item.data["combat_description"] = item.data.get("combat_description", "")

    def load(self):
        filename = self.get_load_filename()
        if not filename:
            return

        self.filename = filename

        data = {}
        with open(filename) as json_file:
            data = json.load(json_file)

        items = []
        for item_data in data.values():
            item = Item()
            item.name = item_data["name"]
            item.icon_slug = item_data["icon_slug"]
            item.description = item_data["description"]
            item.rarity = item_data.get("rarity", "COMMON")
            item.tags = item_data["tags"]
            item.value = item_data["value"]
            item.type = item_data["type"]
            item.level = item_data.get("level", 1)
            item.data = item_data["data"]
            effects_data = item_data["data"].get("effects", [])
            effects = []
            for effect_data in effects_data:
                effect = Effect()
                effect.status_effect = effect_data["status_effect"]
                effect.value = effect_data.get("value", 0)
                effect.duration = effect_data.get("duration", None)
                effects.append(effect)
            item.data["effects"] = effects
            items.append(item)

        if items:
            self.items = items
            self.list_items.clear()
            for item in self.items:
                self.list_items.addItem(item.name)
                self.list_items.setCurrentRow(self.list_items.count()-1)
                self.list_items.item(self.list_items.count()-1).setSelected(True)
                self.set_item_fields(item)

    def get_load_filename(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Load Items...",
            os.path.expanduser("~")
        )
        return filename

    def get_save_filename(self):
        filename, a = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Save Items...",
            os.path.join(os.path.expanduser("~"), "items.json")
        )
        return filename

