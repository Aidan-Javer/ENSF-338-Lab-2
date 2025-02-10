import timeit

def linear_search(array, key):
    for i in array:
        if (array[i] == key):
            return i
    return -1

def binary_search(array, key):
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def measure_time(search_func, array, key, iterations=100):
    t = timeit.timeit(lambda: search_func(array, key), number=iterations)
    return t / iterations