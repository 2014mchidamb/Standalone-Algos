'''
See Wikipedia for an overview of the quicksort algorithm:
    https://en.wikipedia.org/wiki/Quicksort

In this implementation, we use the Lomuto partitioning scheme.
'''
import random

def partition(lst, low, high):
    # Selecting middle element is better than selecting last
    # element when list is sorted.
    # Wikipedia details better pivot selection schemes.
    mid_ind = low + (high - low) // 2
    lst[mid_ind], lst[high] = lst[high], lst[mid_ind]
    pivot = lst[high]

    cur_pos = low
    for i in range(low, high):
        if lst[i] < pivot:
            lst[cur_pos], lst[i] = lst[i], lst[cur_pos]
            cur_pos += 1

    lst[cur_pos], lst[high] = lst[high], lst[cur_pos]
    return cur_pos

def quick_sort(lst, low, high):
    # low = first index, high = last index.
    if low < high:
        pivot = partition(lst, low, high)
        quick_sort(lst, low, pivot - 1)
        quick_sort(lst, pivot + 1, high)

def TEST_QUICK_SORT(num_tests=100):
    passed_tests = 0
    for i in range(num_tests):
        rand_lst = [random.uniform(-1000000, 1000000) for j in range(random.randint(1, 1000))]
        actual_sorted = sorted(rand_lst)
        quick_sort(rand_lst, 0, len(rand_lst) - 1)
        if actual_sorted == rand_lst:
            passed_tests += 1
    print("PASSED TESTS: ", passed_tests)
    print("TOTAL TESTS: ", num_tests)

if __name__ == '__main__':
    TEST_QUICK_SORT()
