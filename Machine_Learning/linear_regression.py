'''
Implementation of linear regression using gradient descent
as well as normal equations to learn weights.
'''
from sklearn import datasets, linear_model
import numpy as np
import random

class LinearRegression:
    # Out of laziness, no bias term.
    def __init__(self, data, targets):
        self.data = data
        self.targets = targets
        self.weights = np.zeros((self.data.shape[-1], 1))

        # Only used with gradient descent.
        self.lr = 0.1 
        self.num_iter = 1000

    def learn_with_normal(self):
        # Analytic solution to L2 loss minimization.
        # w = (X^T X)^{-1} X^T y
        cov = self.data.T.dot(self.data)
        if np.linalg.det(cov) == 0:
            return
        self.weights = np.linalg.inv(cov).dot(self.data.T).dot(self.targets)

    def learn_with_gd(self):
        # L2 loss minimization via gradient descent.
        # w -= eta * (X^T X w - X^T y)
        for i in range(self.num_iter):
            prev_weights = self.weights
            self.weights -= self.lr * (self.data.T.dot(self.data).dot(self.weights) \
                    - self.data.T.dot(self.targets))

    def fit(self, method="normal", lr=0.1, num_iter=1000):
        if method.lower() == "normal":
            self.learn_with_normal()
        else:
            self.lr = lr
            self.num_iter = num_iter
            self.learn_with_gd()

    def predict(self, test_data):
        return test_data.dot(self.weights)

def TEST_LIN_REG(method="NORMAL"):
    diabetes = datasets.load_diabetes()
    diabetes_X = diabetes.data[:, np.newaxis, 2]

    regr = linear_model.LinearRegression()
    regr.fit(diabetes_X, diabetes.target)

    ours = LinearRegression(diabetes_X, diabetes.target)
    ours.fit(method=method)

    if np.linalg.norm(ours.weights - regr.coef_) < 1e-6:
        print("LEARNING WITH {} TEST: PASSING".format(method))
    else:
        print("LEARNING WITH {} TEST: FAILING".format(method))
    
if __name__ == '__main__':
    TEST_LIN_REG("NORMAL")
    TEST_LIN_REG("GD")
