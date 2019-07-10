'''
See Wikipedia for an overview of the quicksort algorithm:
    https://en.wikipedia.org/wiki/Quicksort

In this implementation, we use the Lomuto partitioning scheme.
'''
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

input_lst = list(map(float, input("Enter a space-separated list of numbers: ").split()))
print("Your list: ", input_lst)

quick_sort(input_lst, 0, len(input_lst) - 1)
print("Your list after quicksort: ", input_lst)
