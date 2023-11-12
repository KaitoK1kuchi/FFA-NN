from FF import FF
import copy
import numpy as np
from numpy.random import default_rng

def func(a = [], data = []):
    return (1.0 - max(0, (a[0]*data[0] + a[1]*data[1] + a[2]*data[2] + a[3]))) ** 2
    

def get_last_value(f):
        return f.last_value

class FFA:
    def __init__(self, poblacion=20, alpha=1.0, betamin=1.0, gamma=0.01, seed=None):
        self.poblacion = poblacion
        self.alpha = alpha
        self.betamin = betamin
        self.gamma = gamma
        self.rng = default_rng(seed)
        self.ffs = []

    def handleRemove(f, id):
        return f.id == id
    
    def create_poblation(self, data):
        lists = self.rng.uniform(-1, 1, (self.poblacion, 4))
        for l in lists:
            self.ffs.append(FF(attr = copy.deepcopy(l), data = copy.deepcopy(data), FO=func, max_tol=0.2, max_kill_count = 3))
        

    def emulate(self):
        for num_iter in range(10):
            print("---------------------------------------")
            print("----------------- ", num_iter, " -----------------")
            print("---------------------------------------")
            for (index_f, f) in enumerate(self.ffs):
                f.compute()
                if(f.isDead()):
                    self.ffs.pop(index_f)
                    print("------------- ",index_f, "se murio -------------")

            result_list = copy.deepcopy(self.ffs)
            result_list.sort(key=get_last_value)

            if len(result_list) == 0:
                print("no hay nadie vivo")
            else:
                for (index_f,f) in enumerate(result_list):
                    print(index_f, "tiene ", f.last_value, "de valor")
