# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 21:33:48 2018

@author: fhan
"""

import numpy as np

def f(x):
    return 9*np.sin(3*x) - 6*x

def thomas(LA,MB,UC,d):
    n = len(MB)
    UC[0] = UC[0]/MB[0]
    d[0] = d[0]/MB[0]
    for i in range(1,n-1):
        UC[i] = UC[i]/(MB[i]-LA[i]*UC[i-1])
        d[i] = (d[i]-LA[i]*d[i-1])/(MB[i]-LA[i]*UC[i-1])
    d[n-1] = (d[n-1]-LA[n-2]*d[n-2])/(MB[n-1]-LA[n-2]*UC[n-2])
    
    ans = np.ones(n)
    ans[-1] = d[-1]
    for it in range(n-2,-1,-1):
        ans[it] = d[it]-UC[it]*ans[it+1]
    return ans

xa = 0
xb = np.pi
ua = 0
ub = np.power(xb,3)

def solve(n):
    h = (xb-xa)/n
    h2 = h*h
    LA = np.ones((n-2,))
    MB = np.ones((n-1,))
    UC = np.ones((n-2,))
    
    LA[:] = -1./h2
    MB[:] = 2./h2
    UC[:] = -1./h2
    
    x = np.linspace(xa,xb,n+1)[1:-1]
    b = f(x)
    b[0] = b[0]+ua/h2
    b[-1] = b[-1]+ub/h2
     
    ans = thomas(LA,MB,UC,b)
    return ans

ans = solve(100)

    
    

