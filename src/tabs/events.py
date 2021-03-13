import os
import sys
import json

from ui.ui_tabevents import Ui_EventTabContents
from PyQt5 import QtCore, QtWidgets, uic 
from model.event import Event

class EventTab(QtWidgets.QWidget, Ui_EventTabContents):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Vars
        self.events = []
        self.tag_checks = [
            self.check_tag_common,
            self.check_tag_medical,
            self.check_tag_millitary,
            self.check_tag_police
        ]
        # Table
        header = self.table_event_options.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.table_event_options.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Connections
        self.button_events_new.clicked.connect(self.on_new_event_pressed)
        self.button_events_delete.clicked.connect(self.on_delete_event_pressed)
        self.list_events.itemClicked.connect(self.on_event_list_pressed)
        for check in self.tag_checks:
            check.clicked.connect(self.on_tag_changed)
        # Init
        self.on_new_event_pressed()

    def on_new_event_pressed(self):
        event = Event()
        self.list_events.addItem("")
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
        pass

    def on_tag_changed(self):
        print("tag changed")
        selected_tags = []
        for check in self.tag_checks:
            if check.isChecked():
                selected_tags.append(check.text())
        self.get_selected_event().tags = selected_tags
        print(selected_tags)