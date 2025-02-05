# Exercise 2

### Question 1:

__Mention at least two aspects that make interpolation search better
than binary search [0.1 marks]__

1. Interpolation search uses statistics to search a given dataset.
2. Interpolation search intentionally places its split point based on a statistical method allowing the algorithm to pinpont the searched for element faster.

### Question 2:

__Interpolation search assumes that data is uniformly distributed.
What happens this data follows a different distribution? Will the
performance be affected? Why? [0.2 pts]__

Yes, the performance will be affected. Based on the distrubtion method being used, the algorithm will attempt to jump to different spots in the undistrubted array based on the implemented distrubtion system which may cause it to continual break the array up into unoptimal sub-arrays.

### Question 3:

__If we wanted to modify interpolation search to follow a different
distribution, which part of the code would be affected? [0.1 pts]__

If we wanted to change the distribution used for the sorting algorithm we would have to change line 4: __pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))__ to whatever distrubtion system intended for the new search algorithm.

### Question 4:

__When is linear search your only o3ption for searching data as
binary and interpolation search may fail? [0.2 pts]__

When your data is not sorted, interpolation and binary search will not work as the premise of their respective techniques uses min/max values of an array to break them in to smaller more easily searchable arrays.

### Question 5:

__In which case will linear search outperform both binary and
interpolation search, and why? [0.2 pts]__

Linear search will outperform both binary and interpolation search when the element being found is at the start of the array being searched or if the data within the array is sorted.

### Question 6:

__Is there a way to improve binary and interpolation search to solve
this issue? [0.2 pts]__

You may be able to solve the first issue of interpolation and binary search by checking the first few elements on the array being searched. However, there is not a solution to data being unsorted as applying an optimized sorting algorithm to the data would require nlog(n) steps which would make the entire search complexity n * nlog(n) = n^2log(n) > n (linear search).