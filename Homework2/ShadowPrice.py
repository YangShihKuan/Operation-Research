import numpy as np


A = np.matrix( [[6,5],[10,20]] )
b = np.matrix( [[61],[150]] )
d = np.matrix( [[62],[150]] )
y = np.linalg.solve(A,b)
x = np.linalg.solve(A,d)
a = float(x[0])
b = float(x[1])
z = 500*float(x[0])+450*float(x[1])
sh = z-(500*float(y[0])+450*float(y[1]))
print 'Final: x1=%d,x2=%d,z=%d,Shadow price=%f'%(a,b,z,sh)
