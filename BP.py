import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def doCalculate(datas, targets, plt):

    # Get features and target
    X=datas
    y=np.transpose(targets)

    # y = pd.get_dummies(y).values

    learning_rate = 0.01
    iterations = 200
    N = y.size

    # number of input features
    input_size = 50

    # number of hidden layers neurons
    hidden_size = 100

    # number of neurons at the output layer
    output_size = 1  

    results_mse = []
    results_acc = []

    # Initialize weights
    np.random.seed(10)

    # initializing weight for the hidden layer
    W1 = np.random.normal(scale=0.5, size=(input_size, hidden_size))   

    # initializing weight for the output layer
    W2 = np.random.normal(scale=0.5, size=(hidden_size , output_size)) 

    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def mean_squared_error(y_pred, y_true):
        return ((y_pred - y_true)**2).sum() / (2*y_pred.size)
        
    def accuracy(y_pred, y_true):
        acc = y_pred.argmax(axis=1) == y_true.argmax(axis=1)
        return acc.mean()

    for itr in range(iterations):    
        
        # feedforward propagation
        # on hidden layer
        Z1 = np.dot(X, W1)
        A1 = sigmoid(Z1)

        # on output layer
        Z2 = np.dot(A1, W2)
        A2 = sigmoid(Z2)
        
        
        # Calculating error
        mse = mean_squared_error(A2, y[0])
        acc = accuracy(A2, y)
        results_mse.append(mse)
        results_acc.append(acc)
        
        # backpropagation
        E1 = A2 - y
        dW1 = E1 * A2 * (1 - A2)

        E2 = np.dot(dW1, W2.T)
        dW2 = E2 * A1 * (1 - A1)

        
        # weight updates
        W2_update = np.dot(A1.T, dW1) / N
        W1_update = np.dot(X.T, dW2) / N

        W2 = W2 - learning_rate * W2_update
        W1 = W1 - learning_rate * W1_update


    plt.plot(range(len(results_mse)), results_mse, color="red")

    plt.show()
