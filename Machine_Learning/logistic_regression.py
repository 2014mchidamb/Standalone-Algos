'''
Basic implementation of logistic regression.
'''

from sklearn.datasets import load_breast_cancer
from sklearn import linear_model
import numpy as np

class LogisticRegression:
    def __init__(self, data, targets, lr=0.01):
        self.data = data
        self.targets = np.reshape(targets, (-1, 1))

        # For normalization.
        self.dmin = np.amin(self.data, axis=0)
        self.dmax = np.amax(self.data, axis=0)
        self.threshold = 20

        self.weights = np.zeros((self.data.shape[-1], 1))
        self.lr = lr

    def predict(self, data):
        normalized = (data - self.dmin) / (self.dmax - self.dmin)
        scores = -normalized.dot(self.weights)

        # Thresholding to prevent overflow.
        scores[scores > self.threshold] = self.threshold

        # Sigmoid.
        return 1 / (1 + np.exp(scores))

    def train(self, num_iterations=10000):
        # See Andrew Ng's ML notes for a derivation of the following
        # update.
        for i in range(num_iterations):
            self.weights += self.lr * self.data.T.dot(self.targets - self.predict(self.data))

def TEST_LOG_REG():
    X, y = load_breast_cancer(return_X_y=True)

    sk_log = linear_model.LogisticRegression().fit(X, y)
    our_log = LogisticRegression(X, y)
    our_log.train()

    our_pred = np.squeeze(np.around(our_log.predict(X)))
    sk_pred = sk_log.predict(X)

    our_acc = np.sum((our_pred == y)) / y.size
    sk_acc = np.sum((sk_pred == y)) / y.size

    print("OUR ACCURACY: ", our_acc)
    print("SKLEARN ACCURACY: ", sk_acc)

if __name__ == '__main__':
    TEST_LOG_REG()
