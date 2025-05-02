# 1
import sympy as sym
x = sym.symbols('x')
y = sym.Function('y')
ode = sym.Eq((2*y(x) - 1/x**3)*sym.diff(x) + x*sym.diff(y(x)), 0)
print(sym.dsolve(ode,y(x)))

# 2
import sympy as sym
x = sym.symbols('x')
y = sym.Function('y')
ode = sym.Eq((2*y(x) - 1/x**3)*sym.diff(x) + x*sym.diff(y(x)), 0)
solution = sym.dsolve(ode, y(x))
general = solution.rhs
C1 = sym.symbols('C1')
specific = sym.Eq(general.subs(x,1),0.5)
C1_value = sym.solve(specific,C1)
print(f'{C1_value[0]:.2f}')

# 3
import sympy as sym
x = sym.symbols('x')
y = sym.Function('y')
ode = sym.Eq((2*y(x) - 1/x**3)*sym.diff(x) + x*sym.diff(y(x)), 0)
solution = sym.dsolve(ode, y(x))
general = solution.rhs
C1 = sym.symbols('C1')
specific = sym.Eq(general.subs(x,1),0.5)
C1_value = sym.solve(specific,C1)
specific_solution = general.subs(C1,C1_value[0])
y_vals = specific_solution.subs(x, 5)
print(f'{y_vals:.3f}')

# 4
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
x = sym.symbols('x')
y = sym.Function('y')
C1 = sym.symbols('C1')
ode = sym.Eq((2*y(x) - 1/x**3)*sym.diff(x) + x*sym.diff(y(x)), 0)
solution = sym.dsolve(ode, y(x), ics={y(1): 0.5})
C1_value = 1.5
y_func = sym.lambdify(x,solution.rhs, 'numpy')
x_vals = np.linspace(1, 10, 500)
y_vals = y_func(x_vals)
plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_vals, linewidth=3, label=f'C1 = {C1_value:.2f}')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Graph of y(x) with C1 = 1.50')
plt.xlim(0, 10)
plt.ylim(0, 0.5)
plt.legend()
plt.show()
