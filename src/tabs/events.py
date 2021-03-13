import os
import sys

from ui.ui_tabevents import Ui_EventTabContents
from PyQt5 import QtCore, QtWidgets, uic 
from model.event import Event

class EventTab(QtWidgets.QWidget, Ui_EventTabContents):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Vars
        self.events = []
        # Connections
        self.button_events_new.clicked.connect(self.on_new_event_pressed)
        self.button_events_delete.clicked.connect(self.on_delete_event_pressed)
        self.list_events.itemClicked.connect(self.on_event_list_pressed)
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
            self.list_events.event(self.list_events.currentRow()).setSelected(True)
            self.set_event_fields(self.get_selected_event())

    def on_event_list_pressed(self):
        self.set_event_fields(self.get_selected_event())

    def get_selected_event(self):
        selected_idx = self.list_events.currentRow()
        return self.events[selected_idx]

    def set_event_fields(self, event):
        pass