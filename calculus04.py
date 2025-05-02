# 1
import sympy as sym
t = sym.symbols('t')
f = 10 + 2*sym.tan((sym.pi/4)*t)
ans = sym.simplify(sym.integrate(f,(t,0,1)))
print(f"Integral I = {ans}")

# 2
import sympy as sym
t = sym.symbols('t')
f = 2*t
ans = sym.simplify(sym.integrate(f,(t,0,5)))
ans2  = (ans / 5)
print(f"Integral I = {ans}")
print(f"Average CPU usage = {ans2}%")

# 3
import sympy as sym
from sympy import pprint as sym_print
t,a,b,T = sym.symbols('t a b T')
f = a*t + b
ans = sym.simplify(sym.integrate(f,(t,0,T)))
ans2  = (ans / T)
print("Integral I =")
sym_print(ans)
print("Average BAndwidth = I/T =")
sym_print(ans2)

# 4
import sympy as sym
x,y = sym.symbols('x y')
f = (sym.sin(x)**2)*sym.cos(x)
print(sym.simplify(sym.integrate(f,(x),(y))))

# 5
import sympy as sym
x,y,z = sym.symbols('x y z')
f = (x**2*y*sym.sin(z)) + (8*sym.cos(y)**2)
print(sym.simplify(sym.integrate(f,(x),(y),(z))))

# 6
import sympy as sym
x,y,z = sym.symbols('x y z')
f = (x + y)/sym.sqrt(z)
print(sym.simplify(sym.integrate(f,(x,1,2),(y,3,4),(z,5,6))))