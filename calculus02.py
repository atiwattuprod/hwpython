import sympy as sym
n = sym.symbols('n')
sol = sym.limit((n**2+3*n+4)/(2*n**2+5),n,sym.oo)
print(float(sol))

# #2
import sympy as sym
x, y = sym.symbols('x y')
sol1 = sym.limit((5*x**2+7*y)/(3*x**2+2*x*y+y**2),x,sym.oo)
sol2 = sym.limit(sol1,y,10)
print(f"{sol2:.5f}")

#3
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# x = sym.symbols('x')
x = np.linspace(-5, 5, 400) 

y = 1 / (1 + np.exp(-x))

plt.plot(x, y, 'b', linewidth=2)
plt.xlim(-5, 5)
plt.ylim(0, 1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = 1 / (1 + 1/e**x)')
plt.text(0.9, 0.1, r'Sigmoid limit as $x \to \infty$: 1', color='blue', fontsize=10)
plt.text(0.9, 0.05, r'Sigmoid limit as $x \to -\infty$: 0', color='blue', fontsize=10)
plt.show()

# #4
import sympy as sym
x, y = sym.symbols('x y')
sol1 = sym.limit((x*y)/(sym.sqrt(x*y+1)-1),x,0)
sol2 = sym.limit(sol1,y,0)
print(sol2)

# #5
import sympy as sym
x, y = sym.symbols('x y')
sol1 = sym.limit(((1-sym.cos(x**2+y**2))/(x**2+y**2)*sym.exp(x**2+y**2)),x,1)
sol2 = sym.simplify(sym.limit(sol1,y,-1))
print(sol2)

#6
import sympy as sym
x, y = sym.symbols('x y')
f = (1/sym.sqrt((1-x)**2+y**2)+(1/sym.sqrt((1+x)**2+y**2)))
sol1 = sym.limit(f,x,1)
sol2 = sym.limit(sol1,y,0)
print(sol2)