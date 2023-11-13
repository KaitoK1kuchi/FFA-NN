from FF import FF
import copy
import numpy as np
from numpy.random import default_rng

def func(a = [], data = []):
    return (1.0 - max(0, (a[0]*data[0] + a[1]*data[1] + a[2]*data[2] + a[3]))) ** 2
    

def get_last_value(f):
        return f.last_value

class FFA:
    def __init__(self, lb = -1, ub = 1, dim = 4, poblacion=20, alpha=1.0, betamin=1.0, gamma=0.001, seed=None):
        self.poblacion = poblacion
        self.alpha = alpha
        self.betamin = betamin
        self.gamma = gamma
        self.ub = ub
        self.lb = lb
        self.dim = dim
        self.rng = default_rng(seed)
        self.ffs = []

    def handleRemove(f, id):
        return f.id == id
    
    def create_poblation(self, data):
        lists = self.rng.uniform(self.lb, self.ub, (self.poblacion, self.dim))
        for l in lists:
            self.ffs.append(FF(attr = copy.deepcopy(l), data = copy.deepcopy(data), FO=func, max_tol=0.2, max_kill_count = 2))
        

    def emulate(self, max_eval):

        evaluations = 0
        poblation = copy.deepcopy(self.poblacion)
        new_alpha = copy.deepcopy(self.alpha)
        search_range = self.ub - self.lb        

        while evaluations <= max_eval:
            print("---------------- eval ", evaluations, " ---------------" )
            new_alpha *= 0.97
            for (index_i, f_i) in enumerate(self.ffs):
                for (index_j, f_j) in enumerate(self.ffs):
                    if f_i.last_value >= f_j.last_value:
                        temp_i = f_i.getAttr()
                        temp_j = f_j.getAttr()
                        r = np.sum(np.square(temp_i - temp_j), axis=-1)
                        beta = self.betamin * np.exp(-self.gamma * r)
                        steps = new_alpha * (self.rng.random(self.dim) - 0.5) * search_range
                        temp_i += beta * (temp_j - temp_i) + steps
                        temp_i = np.clip(temp_i, self.lb, self.ub)
                        f_i.setNewAttr(attr = copy.deepcopy(temp_i))
            for (index_f, f) in enumerate(self.ffs):
                f.compute()
                if f.isDead():
                    self.ffs.pop(index_f)
                    print("something dies with attr: ", f.getAttr())

            evaluations += 1
            result_list = copy.deepcopy(self.ffs)
            result_list.sort(key=get_last_value)
            if len(result_list) == 0:
                print("murieron todos")
                break
            if get_last_value(result_list[0]) < 0.00001:
                print("existe menor que 0.00001")
                break

        if len(result_list) == 0:
            print("no hay nadie vivo")
        else:
            for (index_f,f) in enumerate(result_list):
                print(index_f, "tiene ", f.last_value, "de valor")