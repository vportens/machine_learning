from regression_lineaire.model import model
import numpy as np

def grad(X, y, theta):
    m = len(y)
    g =  1/m * (X.T.dot(model(X, theta) - y))
    return g

def gradient_descent(X, y, theta, theta_hist, learning_rate, n_ite):
    for i in range(0, n_ite):
        theta = theta - learning_rate * grad(X, y, theta)
        theta_hist.append(theta.T.tolist()[0])
    return theta