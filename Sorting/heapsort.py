'''
Implementation of heapsort which includes heap implementation.
'''
import random

class MinHeap:
    def __init__(self, values):
        # Initializes min heap with given list of values.
        self.heap = [None] + values
        self.make_heap()

    def min_heapify(self, ind):
        # Compares current root (ind) to children and swaps if necessary.
        left, right = 2 * ind, 2 * ind + 1
        min_ind = ind

        if left < len(self.heap) and self.heap[left] < self.heap[min_ind]:
            min_ind = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_ind]:
            min_ind = right

        if min_ind != ind:
            self.heap[ind], self.heap[min_ind] = self.heap[min_ind], self.heap[ind]
            self.min_heapify(min_ind)

    def make_heap(self):
        # See Wikipedia for runtime analysis.
        for i in range((len(self.heap) - 1) // 2, 0, -1):
            self.min_heapify(i)

    def empty(self):
        return len(self.heap) < 2

    def peek(self):
        if self.empty():
            return None
        return self.heap[1]

    def push_back(self, val):
        self.heap.append(val)
        ind = len(self.heap) - 1
        parent = ind // 2
        while parent > 0 and self.heap[ind] < self.heap[parent]:
            self.heap[ind], self.heap[parent] = self.heap[parent], self.heap[ind]
            ind = parent
            parent = ind // 2

    def pop(self):
        if self.empty():
            return None
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        min_val = self.heap.pop()
        self.min_heapify(1)
        return min_val

def heapsort(values):
    min_heap = MinHeap(values)
    final_vals = []
    while not min_heap.empty():
        final_vals.append(min_heap.pop())
    return final_vals


def TEST_HEAP_SORT(num_tests=100):
    passed_tests = 0
    for i in range(num_tests):
        rand_lst = [random.uniform(-1000000, 1000000) for j in range(random.randint(1, 1000))]
        actual_sorted = sorted(rand_lst)
        heap_sorted = heapsort(rand_lst)
        if actual_sorted == heap_sorted:
            passed_tests += 1
    print("PASSED TESTS: ", passed_tests)
    print("TOTAL TESTS: ", num_tests)

if __name__ == '__main__':
    TEST_HEAP_SORT()
