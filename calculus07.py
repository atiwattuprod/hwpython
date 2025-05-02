# 1
import sympy as sym
t = sym.symbols('t')
I = sym.Function('I')

ode = sym.Eq(I(t).diff(t), 0.05*(1000-I(t)))
equation = sym.dsolve(ode, I(t), ics={I(0):0})
ics = {I(0):0}
result = sym.solve(equation.rhs - 0.8 * 1000, t)

print("Solution of the differential equation: ", sym.dsolve(ode, I(t), ics=ics))
print("Time required for data to spread to 80% of the network: ",f"{result[0]:.2f}","second")

# 2
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
t = sym.symbols('t')
I = sym.Function('I')
ode = sym.Eq(I(t).diff(t), 0.05*(1000-I(t)))
e = sym.dsolve(ode, I(t), ics={I(0):0})
x = np.linspace(0, 100, 500)
y = [float(e.rhs.subs(t,time)) for time in x]
plt.figure(figsize=(10, 5))
t_80 = round(result[0],2)
plt.plot(x, y, color = 'deepskyblue', label = r'$I(t) = N(1 - e^{-kt})$', linewidth = 3)
plt.axvline(t_80, color='violet', linestyle='--', linewidth = 1.5, alpha = 0.5)
plt.axhline(800, color='violet', linestyle='--', linewidth = 1.5, alpha = 0.5)
plt.scatter(t_80, 800, s = 200, color='red', marker = "x",label = f"80% at t ≈ {t_80} sec", zorder=5)
plt.xlabel('Time (Seconds)')
plt.ylabel('Number of devices with data')
plt.title('Data Propagation in a Network')
plt.xlim(0,100)
plt.ylim(0,1000)
plt.grid(True, linestyle='-', alpha=0.6)
plt.legend()
plt.show()

# 3
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
x = sym.symbols('x')
T = sym.Function('T')
ode = sym.Eq(T(x).diff(x) + 0.3*T(x), 30 + 10*sym.sin(0.5*x))
solution = sym.dsolve(ode, T(x))
general = solution.rhs
C1 = sym.symbols('C1')
x_vals = np.linspace(0, 20, 100)
plt.figure(figsize=(10, 5))
for i in range(40,101,5):
    specific = sym.Eq(general.subs(x,0),i)
    C1_value = sym.solve(specific,C1)[0]
    specific_solution = general.subs(C1,C1_value)
    y_vals = [specific_solution.subs(x, val) for val in x_vals]
    plt.plot(x_vals, y_vals,label = f'y[0] = {i} C1 = {C1_value:.2f}', linewidth = 4)
plt.xlabel("Time (Seconds)")
plt.ylabel("CPU Temperature (°C)")
plt.title("CPU Temperature Variation Over Time")
plt.xlim(0, 20)
plt.legend(fontsize = 'small')
plt.grid(True, linestyle='-', alpha=0.5)
plt.show()