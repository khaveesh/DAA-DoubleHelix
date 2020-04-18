""" Generates test cases to check the efficiency of respective 
    algorithms and then analyse them
    
    List Format
        - Since number of terms in the list is a determining factor, 
          we are going to keep varying the size of list from 1 to 10000
        - Since we are calculating Big-O we must make sure that Union of
          list 1 and list 2 is a null set
        - A total of 2*10⁵ values lists will be generated
    
    List Input
        Input
            - list 1 will begin from 0 and go till 9999
            - list 2 will begin from -10000 and go till -1
"""
#!/usr/bin/python3
import matplotlib.pyplot as plt
import time

ip = open("input.dat", "w+")

#Highly inefficient algo
for length in range(1, 10**5+1):
    arr1 = [var1 for var1 in range(length)]
    arr2 = [var2-(10**5) for var2 in range(length)]
    ip.writelines(["%s " % item  for item in arr1])
    ip.writelines("\n")
    ip.writelines(["%s " % item  for item in arr2])
    ip.writelines("\n\n")

ip.close()







