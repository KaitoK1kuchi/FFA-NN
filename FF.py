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
        value = self.FO(self.attr, self.data)

        if(value > self.max_tol):
            print("no es tolerable")
            self.kill_count += 1
        else:
            print("es tolerable")

        self.last_value = value
        print(value)

    def isDead(self):
        return self.kill_count >= self.max_kill_count
