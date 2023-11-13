import copy
class FF:
    def __init__(self, attr, data, FO, max_tol, max_kill_count = 0):
        self.attr = attr
        self.data = data
        self.FO = FO
        self.max_tol = max_tol
        self.max_kill_count = max_kill_count
        self.kill_count = 0
        self.last_value = FO(attr, data)

    def compute(self):

        if(self.last_value > self.max_tol):
            self.kill_count += 1

    def isDead(self):
        return self.kill_count >= self.max_kill_count

    def getAttr(self):
        return copy.deepcopy(self.attr)

    def setNewAttr(self, attr):
        self.attr = attr
        value = self.FO(self.attr, self.data)
        self.last_value = value