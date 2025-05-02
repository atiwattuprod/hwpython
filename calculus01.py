import sympy as sym
print(sym.N(443**(8/9),10))

import sympy as sym
a,b = sym.symbols('a b')
func2 = ((a**(1/2)+b**(1/2))*(a**(1/2)-b**(1/2)))
print(sym.expand(func2))

import sympy as sym
x = sym.symbols('x')
func3 = 6*x**4 + 28*x**3 - 7*x**2 +14*x -5
print(sym.factor(func3))


import sympy as sym
x,y = sym.symbols('x y')
func4 = sym.cos(x)*sym.cos(y) + sym.sin(x)*sym.sin(y)
print(sym.simplify(func4))

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1,1,500)
f = np.sin(np.pi/x)
plt.figure(figsize=(8, 4))
plt.plot(x,f,color="m",linewidth=1,linestyle='-',marker='^',markersize=3)
plt.xlabel('x');plt.ylabel('f(x)')
plt.xlim(-1,1);plt.ylim(-1.5,1.5)
plt.title('f(x) = sin(pi/x)')
plt.show()

from pylab import*
x = linspace(5,10,20)
fig, ax = plt.subplots(figsize=(12,6))
f = x**3 - x + 1
g = x**4 - 3*x**2 + x
h = 3*x**5 - 25*x**3 + 60*x
ax.plot(x,f,color="black",linewidth=1,linestyle='dotted',marker='s')
ax.plot(x,g,color="yellow",linewidth=1,marker='^')
ax.plot(x,h,color="cyan",linewidth=1,linestyle='-.',marker='o')
plt.show()