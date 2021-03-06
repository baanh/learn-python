import math
import random
import sys

from binary_heap import BinaryHeap

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr = _swap(arr, i, min_idx)
    return arr

def merge_sort(arr):
    '''
    As described in "Introduction to Algorithms" (CLRS book)
    Our MERGE procedure takes time O(n), 
    where n = r - p + 1 is the number of elements being merged.
    merge_sort runs in O(nlogn)
    '''
    return _merge_sort_helper(arr, 0, len(arr) - 1)

def heap_sort(arr):
    '''
    This consists of 2 steps:
    1. build a min heap, which is O(nlogn)
    2. extract all n elements of the heap, which is O(nlogn)
    Overall, this takes O(nlogn)
    '''
    heap = BinaryHeap(arr)
    result = []
    while not heap.is_empty():
        result.append(heap.extract_min())
    return result

def quick_sort(arr):
    '''
    As described in "Introduction to Algorithms" (CLRS book)
    '''
    return _quick_sort_helper(arr, 0, len(arr) - 1)

def _swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def _partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr = _swap(arr, i, j)
    arr = _swap(arr, i + 1, r)

    return i + 1, arr

def _quick_sort_helper(arr, p, r):
    if p < r:
        q, arr = _partition(arr, p, r)
        arr = _quick_sort_helper(arr, p, q - 1)
        arr = _quick_sort_helper(arr, q + 1, r)
    return arr

def _merge(arr, p, q, r):
    left = arr[p : q + 1] + [float('inf')]
    right = arr[q + 1 : r + 1] + [float('inf')]
    i = j = 0
    for k in range(p, r + 1):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
    return arr

def _merge_sort_helper(arr, p, r):
    if p < r:
        q = (p + r) // 2
        arr = _merge_sort_helper(arr, p, q)
        arr = _merge_sort_helper(arr, q + 1, r)
        arr = _merge(arr, p, q, r)
    return arr

def _find_bounds(arr):
    lower = float('inf')
    upper = float('-inf')
    for value in arr:
        if value < lower:
            lower = value
        if value > upper:
            upper = value
    return lower, upper

def _counting_sort_on_digit(arr, digit):
    div = 10 ** (digit - 1)
    c = [0 for _ in range(10)]
    for value in arr:
        digit = (value // div) % 10
        c[digit] += 1
    for i in range(1, 10):
        c[i] += c[i-1]

    b = arr[:]
    for i in range(len(arr) - 1, -1, -1):
        digit = (arr[i] // div) % 10
        b[c[digit] - 1] = arr[i]
        c[digit] -= 1
    return b

arrs = [[1, -2, 2, 30, 2, 10, 2, 2, 1], 
        [], 
        [1], 
        [1, 3, -1], 
        [2, 3, 2, 5, 6, 5], 
        [10], 
        [100, 123, 880, 231, 239, 293, 591, 942, 704, 101, 809]]

def test():
    for arr in arrs:
        print(insertion_sort(arr))
        print(selection_sort(arr))
        print(merge_sort(arr))
        print(heap_sort(arr))
        print(quick_sort(arr))
    arr = [random.random() for _ in range(100)]
    for i in range(1, len(a)):
        assert a[i - 1] <= a[i]

test()
