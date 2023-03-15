
def cost_func(X, y, theta):
    m = len(y)
    n = 1 / (2* m) * np.sum(np.power(model(X, theta) - y, 2))
    return n