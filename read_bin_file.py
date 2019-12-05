# -*- coding: utf-8 -*-

import numpy as np
import struct

#with open(r'C:\Users\USER\Desktop\2018-07-01_00','br') as f:
#    da = f.read()
    
#每一块 181440
# head 
dtype = np.dtype([('time','S24'),('xfcst','f4'),('field','S9'),('units','S25'),\
       ('DESC','S46'),('Levle','f4'),('nx','i4'),('ny','i4'),('igrid','i4')])
# map project info(4i4)
# data 281*161f4 

#打开一个二进制文件
f = open(r'C:\Users\USER\Desktop\2018-07-01_00','br')

#使用numpy的fromfile来读取，注意dtype必须要对应，要不然读取出的数据不对
a=np.fromfile(f,dtype=dtype)
f.close()
