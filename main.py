from FFA import FFA
import math
import numpy as np

def Rastringin(X=[], data=[]):
    return (0 - (10 + sum([(x**2 - 10 * np.cos(2 * math.pi * x)) for x in X])))**2

ffa = FFA(dim=10, lb=-5.12, ub=5.12, alpha=1.0, FO=Rastringin)

ffa.create_poblation(data=[75., 12.5], max_tol= 100., max_kill_count=20)
ffa.emulate(max_eval= 100, least_value=0.01)