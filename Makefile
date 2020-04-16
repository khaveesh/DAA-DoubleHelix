.PHONY: run
.DEFAULT: run

run: anarc05b_double_helix.py test.py in.txt
	 python3 anarc05b_double_helix.py < in.txt; echo " "
	 
	 python3 anarc05b_double_helix_greedy.py < in.txt; echo " "
	 python3 test.py; echo " "
	 
	 

	 
