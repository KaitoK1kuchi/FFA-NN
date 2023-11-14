from FFA import FFA
from BP import doCalculate
import math
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt 
from collections import deque 

data_points = deque(maxlen=400)
fig, ax = plt.subplots() 
plt_lines, = ax.plot([10], [50], "b") 
ax.set_xlim(0, 150) 
ax.set_ylim(0, 10)

def Rastringin(X=[], data=[], res = []):
    v = 0
    v += (0 - (10 + sum([(x**2 - 10 * np.cos(2 * math.pi * x)) for x in X])))**2
    return v

datalist = default_rng().uniform(-100, 100, (10, 2))
resultset = default_rng().uniform(0, 3, (1, len(datalist)))

ffa = FFA(dim=10, lb=-5.12, ub=5.12, alpha=0.8, poblacion=5, gamma=0.01)
ffa.create_poblation(data=datalist, results=resultset[0], max_tol= 0.0005, max_kill_count=2)
ffa.emulate(max_eval= 200, least_value=0.0001, data_points=data_points, plt_lines=plt_lines, plt=plt)

doCalculate(datalist, resultset, plt=plt)