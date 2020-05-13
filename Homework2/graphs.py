


import numpy as np  
import matplotlib.pyplot as plt  
fig, ax = plt.subplots()
x = np.arange(0.0,6.0,0.1)  
# MAX z=5*x+4*y5

y1 = (24.0-6*x)/4
y2 = (6.0-x)/2
y3 = 1+x
y4 = 2+0*x


plt.xlabel('X1',fontsize=14, color='black')
plt.ylabel('X2',fontsize=14, color='black')
plt.title('Graphical Solution for LP')
plt.axis([0, 4.5, 0, 6.5])
ax.plot(x, y1,'r:', label='6*x1+4*x2<=24') 
ax.plot(x, y2,'b:',label='x1+2*x2<=6')  
ax.plot(x, y3, 'm:', label='-1*x1+*x2<=1')
ax.plot(x, y4, 'y:', label='x2<=2')

ax.fill_between(x, y3, 0, where=y4 >= y3, facecolor='green', interpolate=True)
ax.fill_between(x, y1, 0, where=y2 >= y1, facecolor='green', interpolate=True)
ax.fill_between(x, y4, 0, where=y2 >= y4, facecolor='green', interpolate=True)
ax.fill_between(x, y4, y3, where=y4 >= y3, facecolor='white', interpolate=True)
ax.fill_between(x, y4, 0, where=y4 >= y2, facecolor='green', interpolate=True)
ax.fill_between(x, y4, y2, where=y4 >= y2, facecolor='white', interpolate=True)
ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='white', interpolate=True)

plt.legend() 



for i in range(15,25,2):
    y5 = (i-5*x)/4
    ax.plot(x, y5, 'c-.', label='max Z=5*x1+4*x2',linewidth=1)

# we know in y1 and y2

A = np.array([[6,4],[1,2]])
b = np.array([[24],[6]])
sol = np.linalg.solve(A,b)
z = 5*sol[0]+4*sol[1]
y5 = (z-5*x)/4
ax.plot(x, y5, 'k-.', label='max Z=5*x1+4*x2',linewidth=5)

plt.show()
######################################################
fig, ax = plt.subplots()
x = np.arange(0.0,6.0,0.1)

plt.xlabel('X1',fontsize=14, color='black')
plt.ylabel('X2',fontsize=14, color='black')
plt.title('Graphical Solution for LP')
plt.axis([0, 4.5, 0, 6.5])

ax.plot(x, y1,'w:') 
ax.plot(x, y2,'w:')  
ax.plot(x, y3, 'w:')
ax.plot(x, y4, 'w:')

ax.fill_between(x, y3, 0, where=y4 >= y3, facecolor='green', interpolate=True)
ax.fill_between(x, y1, 0, where=y2 >= y1, facecolor='green', interpolate=True)
ax.fill_between(x, y4, 0, where=y2 >= y4, facecolor='green', interpolate=True)
ax.fill_between(x, y4, y3, where=y4 >= y3, facecolor='white', interpolate=True)
ax.fill_between(x, y4, 0, where=y4 >= y2, facecolor='green', interpolate=True)
ax.fill_between(x, y4, y2, where=y4 >= y2, facecolor='white', interpolate=True)
ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='white', interpolate=True)



ax.plot(x, y5, 'k-.', label='MAX Z=5*x1+4*x2',linewidth=3)

plt.scatter(sol[0],sol[1],s=80,color='black')
plt.text(3.1,1.5, "<-(x1=3,x2=1.5) is Optimal solution")
plt.legend()
plt.text(2.3,5.4,"MAX Z=5*3+4*1.5=21",fontsize=14)

plt.show()