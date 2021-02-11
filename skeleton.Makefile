SHELL:=/bin/bash

all:
	@echo "choose explicit target = type 'make ' and press TAB"

S=scripts
I=data
O=out


# ===== MAIN STUFF 

SCRIPT=$S/skeleton.py
do:
	@echo "--- $@" 1>&2
	python3 $(SCRIPT) --help
	@echo
	echo "Na?" | python3 $(SCRIPT) --smiley ':('
	@echo
	echo "Na?" | python3 $(SCRIPT)
	@echo

