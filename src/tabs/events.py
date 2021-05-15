import os
import sys
import json

from ui.ui_tabevents import Ui_EventTabContents
from PyQt5 import QtCore, QtWidgets, uic 
from model.event import Event
from model.option import Option
from model.outcome import Outcome
from dialogs.option import DialogOption
from widgets.tags import TagsWidget

class EventTab(QtWidgets.QWidget, Ui_EventTabContents):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Vars
        self.filename = None
        self.events = []
        # Create tags widget
        self.tags_widget = TagsWidget(self, self.on_tag_changed)
        self.container_tags.addWidget(self.tags_widget)
        # Table
        header = self.table_event_options.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.table_event_options.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Connections
        self.button_events_new.clicked.connect(self.on_new_event_pressed)
        self.button_events_delete.clicked.connect(self.on_delete_event_pressed)
        self.list_events.itemClicked.connect(self.on_event_list_pressed)
        self.spinner_event_id.valueChanged.connect(self.on_event_id_changed)
        self.spinner_event_chance.valueChanged.connect(self.on_event_chance_changed)
        self.text_event_name.textChanged.connect(self.on_event_name_changed)
        self.text_event_text.textChanged.connect(self.on_event_text_changed)
        self.button_option_add.clicked.connect(self.on_new_option_clicked)
        self.button_option_remove.clicked.connect(self.on_remove_option_clicked)
        self.button_option_edit.clicked.connect(self.on_edit_option_clicked)
        # Init
        self.on_new_event_pressed()

    def on_event_name_changed(self):
        event_name = self.text_event_name.text()
        selected_event = self.get_selected_event()
        self.list_events.currentItem().setText(str(selected_event.id) + " - " + event_name)
        selected_event.name = event_name

    def on_event_text_changed(self):
        event_text = self.text_event_text.toPlainText()
        self.get_selected_event().text = event_text.split('\n')

    def on_event_id_changed(self):
        event_id = self.spinner_event_id.value()
        selected_event = self.get_selected_event()
        self.list_events.currentItem().setText(str(event_id) + " - " + selected_event.name)
        self.get_selected_event().id = event_id

    def on_event_chance_changed(self):
        event_chance = self.spinner_event_chance.value()
        self.get_selected_event().chance = event_chance

    def on_new_event_pressed(self):
        event = Event()
        self.list_events.addItem("0 - ")
        self.list_events.item(self.list_events.count()-1).setSelected(True)
        self.list_events.setCurrentRow(self.list_events.count()-1)
        self.events.append(event)
        self.set_event_fields(event)

    def on_delete_event_pressed(self):
        if self.list_events.currentRow() == -1:
            print("No events")
            return
        if self.list_events.count() <= 1:
            print("Don't delete last event")
            return

        selected_idx = self.list_events.currentRow()
        self.list_events.takeItem(self.list_events.currentRow())
        self.events.pop(selected_idx)
        if self.list_events.count() > 0:
            self.list_events.item(self.list_events.currentRow()).setSelected(True)
            self.set_event_fields(self.get_selected_event())

    def on_event_list_pressed(self):
        self.set_event_fields(self.get_selected_event())

    def get_selected_event(self):
        selected_idx = self.list_events.currentRow()
        return self.events[selected_idx]

    def set_event_fields(self, event):
        self.spinner_event_id.setValue(event.id)
        self.text_event_name.setText(event.name)
        self.text_event_text.setPlainText('\n'.join(event.text))
        self.spinner_event_chance.setValue(event.chance)
        self.tags_widget.set_tags(event.tags)
        self.table_event_options.setRowCount(0)
        for option in self.get_selected_event().options:
            self.add_option(option)

    def on_tag_changed(self, tags):
        self.get_selected_event().tags = tags

    def on_new_option_clicked(self):
        option_dialog = DialogOption(self)
        if option_dialog.exec_():
            option = option_dialog.option
            self.get_selected_event().options.append(option)
            self.add_option(option)

    def add_option(self, option):
        # Add to the table
        rowCount = self.table_event_options.rowCount()
        self.table_event_options.insertRow(rowCount)
        self.table_event_options.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(option.text))
        self.table_event_options.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(', '.join(map(lambda x: x.action, option.outcomes))))

    def on_remove_option_clicked(self):
        idx = self.table_event_options.currentRow()
        if idx != -1:
            self.table_event_options.removeRow(idx)
            self.get_selected_event().options.pop(idx)

    def on_edit_option_clicked(self):
        idx = self.table_event_options.currentRow()
        if idx != -1:
            selected_option = self.get_selected_event().options[idx]
            option_dialog = DialogOption(self)
            option_dialog.setWindowTitle("Edit Option")
            option_dialog.set_option_fields(selected_option)
            if option_dialog.exec_():
                selected_option.text = option_dialog.option.text
                selected_option.outcomes = option_dialog.option.outcomes
                self.table_event_options.item(idx, 0).setText(selected_option.text)
                self.table_event_options.item(idx, 1).setText(', '.join(map(lambda x: x.action, selected_option.outcomes)))

    def save(self, save_as = False):
        print("Saving Events...")
        event_dict = {}
        for (i, x) in enumerate(self.events):
            x.id = i
            event_dict[i] = x

        if save_as or not self.filename:
            filename = self.get_save_filename()
            if filename:
                self.filename = filename

        if self.filename:
            with open(self.filename, 'w+') as outfile:
                json.dump(event_dict, outfile, default=lambda o: o.__dict__, indent=4)
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

        events = []
        for event_data in data.values():
            event = Event()
            event.id = event_data["id"]
            event.name = event_data["name"]
            event.chance = event_data.get("chance", 1)
            event.text = event_data["text"]
            event.tags = event_data["tags"]
            for option_data in event_data["options"]:
                option = Option()
                option.text = option_data["text"]
                for outcome_data in option_data["outcomes"]:
                    outcome = Outcome()
                    outcome.text = outcome_data.get("text", [])
                    outcome.action = outcome_data["action"]
                    outcome.chance = outcome_data["chance"]
                    outcome.data = outcome_data["data"]
                    option.outcomes.append(outcome)
                event.options.append(option)
            events.append(event)

        if events:
            self.events = events
            self.list_events.clear()
            for event in self.events:
                self.list_events.addItem(str(event.id) + " - " + event.name)
                self.list_events.setCurrentRow(self.list_events.count()-1)
                self.list_events.item(self.list_events.count()-1).setSelected(True)
                self.set_event_fields(event)
    
    def get_load_filename(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Load Events...",
            os.path.expanduser("~")
        )
        return filename

    def get_save_filename(self):
        filename, a = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Save Events...",
            os.path.join(os.path.expanduser("~"), "events.json")
        )
        return filename