# 1
import sympy as sym
t = sym.symbols('t')
S = sym.exp((-3)*t)
eq = sym.diff(S,t,2) + 2*sym.diff(S,t,1) - 3*S
print(sym.simplify(eq))

# 2
import sympy as sym
x = sym.symbols('x')
y = sym.Function('y')
ode = sym.Eq(x*(y(x).diff(x)) + y(x),x)
# print(ode)
sol = sym.dsolve(ode,y(x))
print("General Solution:")
print(sym.simplify(sol))

# ics = 
sol = sym.dsolve(ode, y(x), ics={y(1): 2})
print("Particular Solution:")
print(sym.simplify(sol))

# 3
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
x = np.linspace(-4,4,101)
y = x**2 - 2*x + 2 - np.exp(-x)
plt.plot(x,y,'r')

X, Y = np.meshgrid(np.arange(-4,4,.4),np.arange(-4,4,.4))
U = 1; V = X**2 - Y
vl = np.sqrt(U**2 + V**2)

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.title('Quliver plot of dy/dx = X**2 - Y')
plt.quiver(X, Y, U/vl, V/vl)
plt.show()