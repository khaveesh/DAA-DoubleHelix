.PHONY: run
.DEFAULT: run
run: ANARC05B-DoubleHelix.py in.txt
	 python3 ANARC05B-DoubleHelix.py < in.txt
