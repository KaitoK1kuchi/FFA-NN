import copy
import numpy as np
from numpy.random import default_rng
class DpG:
    def __init__(self, seed, FO, dim):
        self.rng = default_rng(seed)
        self.dim = dim
        self.FO = FO


    def run(self, tries = 100, learning_rate = 0.0001, results = []):
        print(results)
        w = self.rng.normal(scale=0.5, size=self.dim)
        print(w)
        print(self.FO(w))
        print()
        return []