.PHONY: all test run
.DEFAULT: run

all: test run

test:
	@echo "---------"
	@echo "Testing |"
	@echo "---------\n"
	python3 ./test/test_double_helix.py

run:
	@echo "----------------"
	@echo "Code Execution |"
	@echo "----------------"
	@echo "\n1) Dynamic Programming Solution"
	python3 ./code/anarc05b_double_helix.py < ./code/in.txt
	@echo "\n2) Greedy Algorithm Solution"
	python3 ./code/anarc05b_double_helix_greedy.py < ./code/in.txt

help:
	@echo "Use the following tags after make command"
	@echo "all - runs both test and code"
	@echo "test - run tests"
	@echo "run - runs the code"
