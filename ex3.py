import timeit
import cProfile
import re

def sub_function(n):
    # sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
# third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

def main():
    test_function()
    third_function()

if __name__ == '__main__':
    cProfile.run('main()')


# QUESTION 1
"""
A profiler provides a set of statistics which is formulated through the means of
analyzing the performance of a program. In the case of cProfile, it provides the number
of times a function is called (specifies if it was recursive or primitive [not recursive]), the total 
time spent in the function, the total time spent per function call, the cumulative time spent in
the function and all subfunctions, the quotient of the cumulative time divided by primitive calls, and
the respective data of each function.
"""

# QUESTION 2
"""
Benchmarking is the act of testing a program and analyzing how long it takes to execute to completion.
This is done through the means of running multiple standardized tests against the code, testing across
many possible inputs, seeing how the performance may differ.

Profiling is similar to benchmarking, although it provides a far more detailed analysis in terms of the 
functions themselves which are executed. If you're profiling, you're more concerned with where the program may
be spending its time, trying to find bottlenecks in the code.

Benchmarking is more concerned with the overall performance of the program, while profiling is more focused on the details
"""
# QUESTION 3
"""
The execution time was 7.393 seconds.
"""
# QUESTION 4
"""
A good chunk of the execution time was spent in the sub_function function, which was called a total of 10 times
primitively, and 55 times recursively. By the time the sequence of code had reached the third_function(), it had already
spent 6.825 seconds through test_function() and its subfunction, sub_function().
"""