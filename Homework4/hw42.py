# hw42

import numpy as np
np.set_printoptions(threshold=np.nan,precision=2)

A = [
[-1,2, 3,  4, 0, 0, 0,   0],
[0,-1, 1, -1, 1, 0, 0, -10],
[0,-1, 2, -3, 0, 1, 0,  -6],
[0,-3, 4, -5, 0, 0, 1, -15]
]
BV = [4,5,6]
[r,c] = [0,0]

def dual(A):
    A = np.array(A)
    A = A.astype(float)
    b_min = A[1,-1]
    b = [0]
    for x in range(1,len(A)):
        if A[x,-1] <= b_min:
            b_min = A[x,-1]
        b.append(A[x,-1])      
    r = b.index(b_min)          
    r_min = "."
    o = [0]
    for y in range(1,len(A[0])-1):
        if A[0,y]/(-A[r,y]) <= r_min and A[0,y]/(-A[r,y]) > 0:
            r_min = A[0,y]/(-A[r,y])
    for y in range(1,len(A[0])-1):        
        if A[0,y] > 0:
            o.append(A[0,y]/(-A[r,y]))
        elif A[0,y] <= 0:
            o.append('.')       
    c = o.index(r_min)   
    return r,c

def pivot(A, BV, r, c):
    A = np.array(A)
    A = A.astype(float)
    A[r,:] = A[r,:]/A[r,c]
    rows = len(A)
    for i in range(rows):
        if i != r:
            A[i,:] = A[i,:] - A[i,c]*A[r,:]
    BV[r-1] = c
    return A, BV

def decide(A, BV):
    A = np.array(A)
    A = A.astype(float)
    for value in A[0]:
        [r,c] = dual(A)
        [A,BV] = pivot(A,BV,r,c)
     
    print
    print [A,BV]
    print
    print 'Opt = %d'%-A[0,-1]
    print

Automatically_Pivot = decide(A, BV)