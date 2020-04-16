.PHONY: run
.DEFAULT: run
run: anarc05b_double_helix.py in.txt
	 python3 anarc05b_double_helix.py < in.txt
