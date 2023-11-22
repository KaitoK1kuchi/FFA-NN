from FFA import FFA
from BP import doCalculate
from DpG import DpG
import math
import copy
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt 
from collections import deque 

data_points = deque(maxlen=400)
fig, ax = plt.subplots() 
plt_lines, = ax.plot([10], [50], "b") 
ax.set_xlim(0, 500) 
ax.set_ylim(0, 150)

datalist = default_rng().uniform(-10, 10, (20, 50))
resultset = default_rng().uniform(0, 3, (1, len(datalist)))

def Rastringin(X=[], data=[], res = []):
    v = 0
    v += (0 - (10 + sum([(x**2 - 10 * np.cos(2 * math.pi * x)) for x in X])))**2
    return v

def funchc(X=[], data=[], res = []):
    v = 0
    values = np.array(X)
    array1 = np.array(values[0:5000]).reshape(50,100)
    array2 = np.array(values[5000:5100]).reshape(100,1)
    for i in range(len(res)):
        Z1 = np.dot(data[i], copy.deepcopy(array1))
        A1 = 1 / (1 + np.exp(-Z1))
        Z2 = np.dot(A1, array2)
        A2 = 1 / (1 + np.exp(-Z2))
        v += (res[i] - A2[0])**2
    return v/len(data)

# values = np.random.normal(scale=0.5, size=(1, 5100))[0]
# funchc(X=values, data=datalist, res=resultset[0])

# ffa = FFA(dim=50, alpha=1, poblacion=20, gamma=0.001, FO=Rastringin, seed=1)
# ffa.create_poblation(data=datalist, results=resultset[0], max_tol= 0.000000005, max_kill_count=10)
# ffa.emulate(max_eval= 500, least_value=0.000000001, data_points=data_points, plt_lines=plt_lines, plt=plt)

# doCalculate(datalist, resultset, plt=plt)

dpg = DpG(seed=1, FO=Rastringin, dim=50)
dpg.run(learning_rate=0.001, results = resultset[0])
plt.show()