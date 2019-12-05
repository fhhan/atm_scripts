import math
import matplotlib.pyplot as plt 

x0,y0=0,0
x1,y1=3,2

h=0.5
t0 = 60/180


the = math.atan2(y1-y0,x1-x0)

# m0 = x1 - h*math.sin(math.pi/2 - the + t0)
# n0 = y1 - h*math.cos(math.pi/2 - the + t0)
# m1 = x1 + h*math.sin(-math.pi/2 + the + t0)
# n1 = y1 - h*math.cos(-math.pi/2 + the + t0)

m0 = x1 - h*math.cos(the - t0)
n0 = y1 - h*math.sin(the - t0)
m1 = x1 - h*math.cos(the + t0)
n1 = y1 - h*math.sin(the + t0)

#plt.plot((x0,x1),(y0,y1),linewidth=2)
plt.plot((x0,(m0+m1)/2),(y0,(n0+n1)/2))
plt.plot((m0,m1),(n0,n1),linewidth=2)

plt.plot((m0,x1),(n0,y1),linewidth=2)
plt.plot((m1,x1),(n1,y1),linewidth=2)
plt.axis("equal")
plt.show()