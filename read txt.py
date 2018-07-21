# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 13:09:24 2018

@author: fhan
"""

import numpy as np

file = open('wang_o.txt','r')
list_arr1 = file.readlines()

list_arr = list_arr1[1:]
n = len(list_arr)
#print(n)

for i in range(n):
    list_arr[i] = list_arr[i].strip()
    list_arr[i] = list_arr[i].replace(',{',',')
    list_arr[i] = list_arr[i].strip('}')
    list_arr[i] = list_arr[i].split(',')

#print(list_arr)  
a = np.array(list_arr)
#print(a)
file.close()

#f2 = open('modify.txt','a')
#f2.writelines(list_arr)
#f2.close()