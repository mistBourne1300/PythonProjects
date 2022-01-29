import numpy as np
a = -1
b = 1
c = 3
domainx, domainy = np.meshgrid(np.linspace(a,b,c), np.linspace(a,b,c))
f = lambda x,y: x**2 + y**2 + x + y + 1

z = f(domainx, domainy)