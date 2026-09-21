import numpy as np

def gt(x):
    x1 = x[:,0] > 0.
    x2 = x[:,0] < 0.8
    y1 = x[:,1] > 0.2
    y2 = x[:,1] < 0.8
    return 1*(x1 * x2 * y1 * y2)

def train(n=50):
    np.random.seed(3407)
    X = np.random.rand(n,2)
    Y = gt(X)
    return X, Y

def val(n=50, m=50):
    train(n)
    X = np.random.rand(m,2)
    Y = gt(X)
    return X, Y

def test(n=50, m=50, l=50):
    val(n,m)
    X = np.random.rand(l,2)
    Y = gt(X)
    return X, Y
