from FFA import FFA

ffa = FFA(dim=15)

ffa.create_poblation(data=[75., 12.5])
ffa.emulate(max_eval= 100)