from regression_lineaire.model import model
def grad(X, y, theta):
    m = len(y)
    return 1/m * (X.T.dot(model(X, theta) - y))

def gradient_descent(X, y, theta, learning_rate, n_ite):
    for i in range(0, n_ite):
        theta = theta - learning_rate * grad(X, y, theta)
    return theta