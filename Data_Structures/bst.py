'''
Basic binary search tree (BST) implementation.
'''
import random

class BST:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

    def find(self, val):
        # If node with value val exists, returns it.
        if self.val == val:
            return self
        if val < self.val and self.left:
            return self.left.find(val)
        elif val >= self.val and self.right:
            return self.right.find(val)
        return None

    def find_min(self):
        # Returns node with minimum value.
        cur = self
        while cur.left:
            cur = cur.left
        return cur

    def inorder(self):
        # Returns the list of elements contained in the tree
        # in sorted order.
        nums = []
        def inorder_helper(root):
            if root is None:
                return
            inorder_helper(root.left)
            nums.append(root.val)
            inorder_helper(root.right)
        inorder_helper(self)
        return nums

    def insert(self, val):
        # Inserts node into tree. 
        if val < self.val:
            if not self.left: 
                self.left = BST(val)
                self.left.parent = self
                return 
            self.left.insert(val)
        else:
            if not self.right: 
                self.right = BST(val)
                self.right.parent = self
                return 
            self.right.insert(val)

    def replace_node_in_parent(self, new_node=None):
        if self.parent:
            if self == self.parent.left:
                self.parent.left = new_node
            else:
                self.parent.right = new_node
        if new_node:
            # The new node replaced either left or right,
            # so we need to re-attach to their parent.
            new_node.parent = self.parent

    def delete(self, val):
        # Deletes node in tree.
        if val < self.val and self.left: 
            self.left.delete(val)
            return
        elif val > self.val and self.right: 
            self.right.delete(val)
            return
        if val != self.val:
            return
        if self.left and self.right:
            # In this case, we replace the node with the node
            # immediately after in inorder traversal.
            successor = self.right.find_min()
            self.val = successor.val
            successor.delete(successor.val)
        elif self.left:
            # Replace with left.
            self.replace_node_in_parent(self.left)
        elif self.right:
            # Replace with right.
            self.replace_node_in_parent(self.right)
        else:
            self.replace_node_in_parent()

def TEST_BINARY_TREE_INSERT(num_tests=100):
    passed_tests = 0
    for i in range(num_tests):
        rand_lst = [random.uniform(-1000000, 1000000) for j in range(random.randint(1, 1000))]
        actual_sorted = sorted(rand_lst)
        bst = BST(rand_lst[0])
        for j in range(1, len(rand_lst)):
            bst.insert(rand_lst[j])
        if actual_sorted == bst.inorder():
            passed_tests += 1
    print("PASSED INSERT TESTS: ", passed_tests)
    print("TOTAL INSERT TESTS: ", num_tests)

def TEST_BINARY_TREE_DELETE(num_tests=100):
    passed_tests = 0
    for i in range(num_tests):
        rand_lst = [random.uniform(-1000000, 1000000) for j in range(random.randint(1, 1000))]
        bst = BST(rand_lst[0])
        for j in range(1, len(rand_lst)):
            bst.insert(rand_lst[j])
        rand_elem = random.choice(rand_lst)
        bst.delete(rand_elem)
        if bst.find(rand_elem) == None:
            passed_tests += 1
    print("PASSED DELETE TESTS: ", passed_tests)
    print("TOTAL DELETE TESTS: ", num_tests)

if __name__ == '__main__':
    TEST_BINARY_TREE_INSERT()
    TEST_BINARY_TREE_DELETE()
