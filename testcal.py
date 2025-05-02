from pylab import*
x = linspace(-10,10,20)
fig, ax = plt.subplots(figsize=(12,6))
f = x**3
g = x**2
# h = 3*x**5 - 25*x**3 + 60*x
ax.plot(x,f,color="black",linewidth=3)
ax.plot(x,g,color="yellow",linewidth=3)
plt.xlim(-10,10);plt.ylim(-100,100)
# ax.plot(x,h,color="cyan",linewidth=1,linestyle='-.',marker='o')
plt.show()