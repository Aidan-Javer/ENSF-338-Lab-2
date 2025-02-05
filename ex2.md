# Exercise 2

### Question 1:

Mention at least two aspects that make interpolation search better
than binary search [0.1 marks]

1. Instead of going to the middle of each broken up array, interpolation search can go to different locations within the array based on its distrubtion. 

2.

### Question 2:

Interpolation search assumes that data is uniformly distributed.
What happens this data follows a different distribution? Will the
performance be affected? Why? [0.2 pts]

Yes, the performance will be affected.

### Question 3:

If we wanted to modify interpolation search to follow a different
distribution, which part of the code would be affected? [0.1 pts]

If we wanted to change the distribution used for the sorting algorithm we would have to change line 4: __pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))__ to whatever distrubtion system intended for the new search algorithm.

### Question 4:

When is linear search your only option for searching data as
binary and interpolation search may fail? [0.2 pts]

When your data is not sorted, interpolation and binary search will not work as the premise of their respective techniques uses min/max values of arrays to break them in to smaller more easily searchable arays.

### Question 5:

In which case will linear search outperform both binary and
interpolation search, and why? [0.2 pts]

Linear search will outperform both binary and interpolation search when the element being found is at the start of the array being searched.

### Question 6:

Is there a way to improve binary and interpolation search to solve
this issue? [0.2 pts]