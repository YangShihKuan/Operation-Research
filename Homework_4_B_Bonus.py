# lecture3_ORClass The Simplex Method P.46-P.51

import numpy as np
np.set_printoptions(threshold=np.nan,precision=2)

A = [
[1, 1,-3, 3, 0, 0, 0, 0, 0, 0],
[0, 3,-1,-2, 1, 0, 0, 0, 0, 7],
[0,-2,-4, 4, 0, 1, 0, 0, 0, 3],
[0, 1,-2, 0, 0, 0, 1, 0, 0, 4],
[0,-2, 2, 1, 0, 0, 0, 1, 0, 8],
[0, 3, 0, 0, 0, 0, 0, 0, 1, 5]
]
BV = [4,5,6,7,8]
[r,c] = [0,0]

def primal(A):
    A = np.array(A)
    A = A.astype(float)
    B = A[0,:]
    mini  = 0
    for k in range(1,len(A[1])):
        if A[0,k] < mini:
                mini = A[0,k]
    c = B.tolist().index(mini)
    
    mini_c =[]
    for j in range(1,len(A)):
        if A[j,c] > 0:   
            value = A[j,-1]/A[j,c]
            mini_c.append(value)
        elif A[j,c] <= 0:
            mini_c.append('.')
    mini_value = mini_c[0]
    for w in range(len(mini_c)):
        if mini_c[w] < mini_value:
            mini_value = mini_c[w]
            
    r = mini_c.index(mini_value)+1
    return r,c

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
def obj_rhs(A):
   
    b_list = [A[y][-1] for y in range(1,len(A))]
    for b in b_list:
        if b >= 0:
            rhs = True
        elif b <= 0:
            rhs = False
    return  rhs

def decide(A, BV):
    A = np.array(A)
    A = A.astype(float)
    rhs = obj_rhs(A)
    
    if rhs == True:
        for value in A[0]:
            [r,c] = primal(A)
            [A,BV] = pivot(A,BV,r,c)
        print
        print [A,BV]
        print
        print 'Opt = %.2f'%A[0,-1]
    
    elif rhs == False:
        for value in A[0]:
            [r,c] = dual(A)
            [A,BV] = pivot(A,BV,r,c)
        print
        print [A,BV]
        print
        print 'Opt = %.2f'%A[0,-1]
        print

Automatically_Pivot = decide(A, BV)