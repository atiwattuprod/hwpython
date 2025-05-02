# 1
import sympy as sym
s = sym.symbols('s')
t = ((s**2)/10) + 5
sol = sym.diff(t,s)
print(f"Rate of change {sol}")
lis = [20,55,99]
for x in lis:
    ans1 = float(sol.subs(s,x))
    print(f"Download time for a file of size {x} MB: {ans1:.2f} seconds")

# 2
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

x1 = sym.symbols('x')
c1 = sym.ln(x1)
dydx = sym.diff(c1,x1)

def tangent_line(x_point,slope,x_range):
    y_point = float(c1.subs(x1,x_point))
    b = y_point - slope * x_point
    return lambda x1: slope * x1 + b

sol1 = float(dydx.subs(x1,1))
sol2 = float(dydx.subs(x1,10))
sol3 = float(dydx.subs(x1,50))

x = np.linspace(0.1, 60, 1000)
c = np.log(x)

plt.figure(figsize=(10,6))
plt.plot(x,c,'-b',label='C(x) = ln(x)')

x_tan1 = np.linspace(0.1,2,100)
tan1 = tangent_line(1,sol1,x_tan1)
plt.plot(x_tan1,[tan1(i) for i in x_tan1],'r--',label = f'Tangent at x = 1 (C(1) = {float(c1.subs(x1,1)):.2f})')

x_tan2 = np.linspace(5,15,100)
tan2 = tangent_line(10,sol2,x_tan2)
plt.plot(x_tan2,[tan2(i) for i in x_tan2],'g--',label = f'Tangent at x = 10 (C(10) = {float(c1.subs(x1,10)):.2f})')

x_tan3 = np.linspace(45,55,100)
tan3 = tangent_line(50,sol3,x_tan3)
plt.plot(x_tan3,[tan3(i) for i in x_tan3],'y--',label = f'Tangent at x = 50 (C(50) = {float(c1.subs(x1,50)):.2f})')

plt.xlabel('x')
plt.ylabel('C(x)')
plt.title('C(x) = ln(x)')

plt.grid(True)
plt.axhline(y = 0,color = 'k',linestyle = '-',alpha = 0.5)
plt.axvline(x = 0,color = 'k',linestyle = '-',alpha = 0.5)

plt.plot([1],[float(c1.subs(x1,1))],'ro')
plt.plot([10],[float(c1.subs(x1,10))],'go')
plt.plot([50],[float(c1.subs(x1,50))],'yo')

plt.legend()

plt.show()

# 3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')

x = np.linspace(-4,4,41)
y = np.linspace(-4,4,41)
X,Y = np.meshgrid(x,y)
Z = (X**2 + Y**2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Star CS-2024')

ax.set_xticks(np.arange(-4, 5, 1))
ax.set_yticks(np.arange(-4, 5, 1))

surf = ax.plot_surface(X,Y,Z,cmap='plasma', edgecolor='none')
fig.colorbar(surf, shrink=0.5, aspect=10)

min_idx = np.unravel_index(np.argmin(Z, axis=None), Z.shape)
min_x = X[min_idx]
min_y = Y[min_idx]
min_z = Z[min_idx]
ax.scatter(min_x, min_y, min_z, color='red', s=100, label="Optimal Base Location")
ax.legend()

ax.view_init(elev=15, azim=45)

plt.show()

# 4
import sympy as sym
x = sym.symbols('x')
y = x - sym.sqrt(x)
print(sym.diff(y,x))

# 5
import sympy as sym
x = sym.symbols('x')
y = sym.sqrt(x) * sym.ln(x)
print(sym.diff(y,x))

# 6
import sympy as sym
x = sym.symbols('x')
y = sym.sqrt(sym.sin(x))
print(sym.diff(y,x))