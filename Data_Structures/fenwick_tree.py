'''
Simple Fenwick Tree (or Binary Index Tree) implementation.
'''
from time import time
import random

class BIT:
    def __init__(self, vals):
        # One index for convenience.
        self.sums = [0] * (len(vals) + 1)
        self.initialize(vals)

    def add(self, ind, val):
        while ind < len(self.sums):
            self.sums[ind] += val
            ind += ind & (-ind)

    def get_sum(self, ind):
        # Sum of [1, ind].
        total = 0
        while ind > 0:
            total += self.sums[ind]
            ind -= ind & (-ind)
        return total

    def initialize(self, vals):
        for i, val in enumerate(vals):
            self.add(i + 1, val)

class PrefixArray:
    # Prefix sum implementation for comparison.
    def __init__(self, vals):
        self.sums = [0] * (len(vals) + 1)
        self.initialize(vals)

    def add(self, ind, val):
        for i in range(ind, len(self.sums)):
            self.sums[i] += val

    def get_sum(self, ind):
        return self.sums[ind]

    def initialize(self, vals):
        for i, val in enumerate(vals):
            self.sums[i + 1] = self.sums[i] + val

def TEST_BIT(num_q=1000):
    vals = [random.randint(-1e3, 1e3) for i in range(num_q)]
    to_add = [random.randint(-1e3, 1e3) for i in range(num_q)]
    inds = [random.randint(1, num_q) for i in range(num_q)]
    ans1 = [0] * num_q
    ans2 = [0] * num_q

    start = time()
    fentree = BIT(vals)
    for i in range(num_q):
        fentree.add(inds[i], to_add[i])
        ans1[i] = fentree.get_sum(inds[i])
    fentime = time() - start

    start = time()
    prefix = PrefixArray(vals)
    for i in range(num_q):
        prefix.add(inds[i], to_add[i])
        ans2[i] = prefix.get_sum(inds[i])
    prefix_time = time() - start

    print("Total Fenwick Tree time: ", fentime)
    print("Total Prefix Array time: ", prefix_time)

    if ans1 == ans2:
        print("TEST PASSED: ANSWERS EQUAL")
    else:
        print("TEST FAILED: ANSWERS INEQUAL")

if __name__ == '__main__':
    TEST_BIT(5000)
