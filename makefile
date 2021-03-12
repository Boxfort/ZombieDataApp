ui_files := $(wildcard ui/*.ui)
output_files := $(subst ui/,,$(patsubst %.ui,%.py,$(ui_files)))

ui:
	for file in $(ui_files) ; do \
		FILENAME=$(subst ui/,,$(patsubst %.ui,%.py,$(ui_files))) ; \
		echo $$FILENAME ; \
		echo $(file) ; \
		pyuic5 $$file -o src/ui/ui_$$FILENAME ; \
	done

windows: 
	docker run -v "$(PWD)/src:/src/" cdrx/pyinstaller-windows:python3
