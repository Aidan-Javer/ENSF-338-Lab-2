## Part 1 ##
import timeit
import numpy as np
import random
from matplotlib import pyplot as plt

def linear_search(array, key):
    for index, value in enumerate(array):
        if value == key:
            return index
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


## Part 2 ##
def measure_time(search_func, array, key, iterations=100):
    t = timeit.timeit(lambda: search_func(array, key), number=iterations)
    return t / iterations

average_linear = []
average_binary = []
if __name__ == "__main__":
    listlengths = [1000, 2000, 4000, 8000, 16000, 32000]
    for listlength in listlengths:
        numbers = [x for x in range(listlength)]
        list1 = []
        list2 = []
        random_number = random.randint(numbers)
        for i in range(1000):
            list1.append(measure_time(linear_search, numbers, random_number))
        for j in range(1000):
            list2.append(measure_time(binary_search, numbers, random_number))
        avg_l = sum(list1) / len(list1)
        avg_b = sum(list2) / len(list2)
        average_linear.append(avg_l)
        average_binary.append(avg_b)

## Part 3 ##

    slope, intercept = np.polyfit(listlengths, average_linear, 1)
    plt.scatter(listlengths, average_linear, label='Linear Search')
    linevalues = [slope * x + intercept for x in listlengths]
    plt.plot(listlengths, linevalues, 'r')

    log_lengths = np.log(listlengths) 
    slope, intercept = np.polyfit(log_lengths, average_binary, 1)
    plt.scatter(listlengths, average_binary, label='Binary Search')
    linevalues = [slope * np.log(x) + intercept for x in listlengths]
    plt.plot(listlengths, linevalues, 'g')

    plt.xlabel('List Length')
    plt.ylabel('Average Time (seconds)')
    plt.legend()
    plt.show()

## Part 4 ##
"""
1. The function for the linear_search method is a linear function of the formm t = a * n + b. Where b is a constant time applied to any computations made, a is the average time when another element is added to the vector, n is the number of elements in the given vector, and lastly, t is the average time to find a given element within the vector. This follows the expected results as O(m * n + b) = O(n) which is the upper bound of the linear search method.

2. The function for the binary_search method is a logarithmic function of the formm t = a * log (n) + b. Where b is a constant time applied to any computations made, a is the average time when another element is added to the vector, n is the number of elements in the given vector, and lastly, t is the average time to find a given element within the vector. This follows the expected results as O(a * log (n) + b) = O(log(n)) which is the upper bound of the binary search method.
"""
