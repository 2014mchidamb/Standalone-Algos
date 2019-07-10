"""
This is a basic example of forward mode automatic differentiation
that works with a simple composition of addition and multiplication.

For more details about forward (and general) automatic differentiation, the
following resources are pretty good:

    - https://en.wikipedia.org/wiki/Automatic_differentiation
    - https://rufflewind.com/2016-12-30/reverse-mode-automatic-differentiation
    - https://cs231n.github.io/optimization-2/
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.grad = 0.0

    def __add__(self, other):
        z = Node(self.val + other.val)
        z.grad = self.grad + other.grad # Linearity of derivative.
        return z

    def __mul__(self, other):
        z = Node(self.val * other.val)
        z.grad = self.grad * other.val + other.grad * self.val # Multiplication rule.
        return z

# Our function is e = (a * b) + d, and its derivative with respect to a
# is de/da = b.

a = Node(2.0)
a.grad = 1.0 # Indicating that we want to differentiate with respect to a.

b = Node(3.0)

c = a * b
d = Node(4.0)

e = c + d

print("The output value: ", e.val)
print("The derivative with respect to a: ", e.grad)
print("Expected derivative with respect to a: ", b.val)
