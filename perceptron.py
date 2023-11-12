class Perceptron:
    def __init__(self, errorFunc, activationFunc, inputs, weights):
        self.errorFunc = errorFunc
        self.activationFunc = activationFunc
        self.inputs = inputs
        self.weights = weights

    
