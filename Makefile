.PHONY: all test run
.DEFAULT: run

all: test run

test:
	@echo "---------"
	@echo "Testing |"
	@echo "---------\n"
	python3 test_double_helix.py

run:
	@echo "----------------"
	@echo "Code Execution |"
	@echo "----------------"
	@echo "\n1) Dynamic Programming Solution"
	python3 anarc05b_double_helix.py < in.txt
	@echo "\n2) Greedy Algorithm Solution"
	python3 anarc05b_double_helix_greedy.py < in.txt

help:
	@echo "Use the following tags after make command"
	@echo "all - runs both test and code"
	@echo "test - run tests"
	@echo "run - runs the code"
