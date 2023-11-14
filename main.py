from FFA import FFA
import math
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt 
from collections import deque 

data_points = deque(maxlen=150)
fig, ax = plt.subplots() 
plt_lines, = ax.plot([10], [50], "b") 
ax.set_xlim(0, 100) 
ax.set_ylim(0, 1000)

def Rastringin(X=[], data=[]):
    v = 0
    v += (0 - (10 + sum([(x**2 - 10 * np.cos(2 * math.pi * x)) for x in X])))**2
    return v

datalist = default_rng().uniform(-5.12, 5.12, (10, 4))

ffa = FFA(dim=20, lb=-5.12, ub=5.12, alpha=1.0, FO=Rastringin, poblacion=100, gamma=0.01)

ffa.create_poblation(data=datalist, max_tol= 0.0005, max_kill_count=20)
ffa.emulate(max_eval= 100, least_value=0.0001, data_points=data_points, plt_lines=plt_lines, plt=plt)