
S=scripts
SCRIPT=$S/skeleton.py

all:
	python3 $(SCRIPT) --help
	@echo
	echo "Na?" | python3 $(SCRIPT) --smiley ':('
	@echo
	echo "Na?" | python3 $(SCRIPT)
	@echo

