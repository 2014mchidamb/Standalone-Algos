'''
Simple skip list implementation; see Wikipedia for details.
'''

from time import time
import math
import random

class ListNode:
    # Skip list node class that has links to levels below.
    def __init__(self, val, num_levels=1):
        self.val = val
        self.next = None
        self.prev = None
        self.below = None
        self.copy_below(num_levels)

    def copy_below(self, num_levels):
        # Makes this node into a ladder of num_levels nodes.
        cur = self
        for i in range(num_levels-1):
            cur.below = ListNode(self.val)
            cur = cur.below

    def splice(self, node):
        self.next.prev = node
        node.next = self.next
        node.prev = self
        self.next = node

    def connect(self, node):
        self.next = node
        node.prev = self

    def connect_all(self, node):
        cur = self
        while cur and node:
            cur.connect(node)
            cur = cur.below
            node = node.below

    def remove(self):
        if self.prev and self.next:
            # Can't remove head or tail.
            self.prev.connect_all(self.next)
        
class SkipList:
    def __init__(self, vals, max_level=32, insertion_prob=0.5):
        self.max_level = max_level
        self.insertion_prob = insertion_prob

        # Initialize head and tail of list.
        self.head = ListNode(-math.inf, self.max_level)
        self.tail = ListNode(math.inf, self.max_level)
        self.head.connect_all(self.tail)

        # Initialize rest of list.
        self.initialize(vals)

    def find(self, val):
        # Returns node if found, otherwise None.
        cur = self.head
        while cur:
            while val > cur.val:
                cur = cur.next
            if val == cur.val:
                break
            cur = cur.prev.below
        return cur

    def insert(self, val):
        # Keeps previous node at each level.
        prevs = []
        cur = self.head
        while cur:
            while val >= cur.val:
                # Guaranteed to stop since tail has math.inf.
                cur = cur.next
            cur = cur.prev
            prevs.append(cur)
            # Step back, and then move down a level.
            cur = cur.below

        node = None
        prob = 0
        prev_index = len(prevs) - 1
        while prev_index >= 0 and prob <= self.insertion_prob:
            # Add node above current node and splice it into list
            # at that level.
            up_node = ListNode(val)
            up_node.below = node
            prevs[prev_index].splice(up_node)

            # Randomly choose whether to add at next level.
            prev_index -= 1
            node = up_node
            prob = random.random()

    def delete(self, val):
        node = self.find(val)
        if node:
            node.remove()

    def initialize(self, vals):
        for val in vals:
            self.insert(val)

    def print_list(self):
        cur = self.head
        while cur:
            next_cur = cur.below
            while cur:
                print(cur.val, end=' ')
                cur = cur.next
            cur = next_cur
            print()

def TEST_SKIP_LIST(nums_size=1000):
    nums = list(range(nums_size))
    skip = SkipList(nums, 10, 0.5)
    
    def simple_find(val):
        for num in nums:
            if num == val:
                return num
        return None

    queries = [random.randint(-nums_size, nums_size) for i in range(nums_size)]
    simple_ans = [0 for i in range(nums_size)]
    skip_ans = [0 for i in range(nums_size)]

    start = time()
    for i, query in enumerate(queries):
        simple_ans[i] = simple_find(query)
    simple_time = time() - start

    start = time()
    for i, query in enumerate(queries):
        skip_ans[i] = skip.find(query)
    skip_time = time() - start

    for i in range(nums_size):
        if skip_ans[i] != None:
            skip_ans[i] = skip_ans[i].val

    print("Total time taken by simple search: ", simple_time)
    print("Total time taken by skip list: ", skip_time)

    if simple_ans != skip_ans:
        print("TEST FAILED: Answers are not equal.")
    else:
        print("TEST PASSED: Answers are equal.")

if __name__ == '__main__':
    TEST_SKIP_LIST()
