.PHONY: ui

ui:
	pyuic5 ui/mainwindow.ui -o src/ui/ui_mainwindow.py
	pyuic5 ui/dialogeffect.ui -o src/ui/ui_dialogeffect.py


windows: 
	docker run -v "$(PWD)/src:/src/" cdrx/pyinstaller-windows:python3
