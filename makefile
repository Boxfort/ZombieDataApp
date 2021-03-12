ui_files := $(wildcard ui/*.ui)

.PHONY: ui

ui:
	for file in $(ui_files) ; do \
		FILENAME=$(subst ui/,,$(patsubst %.ui,%.py,$(ui_files))) ; \
		pyuic5 $$file -o src/ui/ui_$$FILENAME ; \
		echo "Creating 'src/ui/ui_$$FILENAME'..." ; \
	done

windows: 
	docker run -v "$(PWD)/src:/src/" cdrx/pyinstaller-windows:python3
