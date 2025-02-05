"""
Question 1:
The code calculates the nth number of the fibonacci sequence.

Question 2:
No this is not an example of divide and conquer since the algorithm must calculate values for which it has already calculated. Everytime it does a recursive call, the recursive call does essentially the same amount of work as the one before it. For example:
    func(5) calls func(4) + func(3)
        func(4) calls func(3) + func(2)    
    func(5) can be expanded to func(3) + func(2) + func(3)
        Here we can see that fib(3) is being calculated twice.
The branch of each function call divides into two additional branches which increases the number of problems to solve. The branches can only be combined once all branches are n==0 or n==1. While the algorithm does divide, each division does not necessarily reduce the amount of work that each branch has to do.

Question 3:
The expression for the time complexity of this algorithm is O(2^n).
"""

def func(n):
    if n==0 or n==1:
        return n
    else:
        return func(n-1) + func(n-2)
   
def fib(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]

"""
Question 5:
The expression for the time complexity of the improved algorithm is O(n)
Each value is only calculated once since the cache keeps a record of the values that have been calculated.
"""

import timeit
from matplotlib import pyplot as plt

func_avg = []
fib_avg = []
for i in range(36):
    cache = {0:0, 1:1}
    func_tm = timeit.timeit(lambda:func(i), number=10)
    fib_tm = timeit.timeit(lambda:fib(i), number=10)
    func_avg.append(func_tm / 10)
    fib_avg.append(fib_tm / 10)

plt.figure(figsize=(9, 7))
plt.scatter(range(36), func_avg)
plt.savefig("1.6.1.jpg")

plt.figure(figsize=(9, 7))
plt.scatter(range(36), fib_avg)
plt.savefig("1.6.2.jpg")
