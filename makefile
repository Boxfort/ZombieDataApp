.PHONY: ui

ui:
	pyuic5 ui/mainwindow.ui -o src/ui/ui_mainwindow.py
	pyuic5 ui/dialogeffect.ui -o src/ui/ui_dialogeffect.py
	pyuic5 ui/dialogoption.ui -o src/ui/ui_dialogoption.py
	pyuic5 ui/tabitems.ui -o src/ui/ui_tabitems.py
	pyuic5 ui/tabenemies.ui -o src/ui/ui_tabenemies.py
	pyuic5 ui/tabevents.ui -o src/ui/ui_tabevents.py


windows: 
	docker run -v "$(PWD)/src:/src/" cdrx/pyinstaller-windows:python3
