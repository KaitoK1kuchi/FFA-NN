import copy
import random
import numpy as np

class FF:
    def __init__(self, attr, data, results, FO, max_tol, max_kill_count = 0):
        self.attr = attr
        self.data = data
        self.FO = FO
        self.max_tol = max_tol
        self.max_kill_count = max_kill_count
        self.kill_count = 0
        self.last_value = FO(attr, data, results)
        self.results = results

    def compute(self):
        if(self.last_value > self.max_tol):
            self.kill_count += 1

    def isDead(self):
        return self.kill_count >= self.max_kill_count

    def getAttr(self):
        return copy.deepcopy(self.attr)

    def setNewAttr(self, attr):
        self.attr = attr
        value = self.FO(self.attr, self.data, self.results)
        self.last_value = value

    def replicate(self, func, attr = [], data = [], results = []):
        temp1 = copy.deepcopy(self.attr)
        temp2 = attr
        ret = []

        for i in range(len(temp1)):
            ret.append((temp1[i] + temp2[i])/2)
        
        return FF(attr = copy.deepcopy(np.array(ret)), data = copy.deepcopy(data), results= copy.deepcopy(results), FO=func, max_tol=0.2, max_kill_count = 2)