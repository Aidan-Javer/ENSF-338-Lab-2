# Exercise 4

1.  Assuming that we have no knowledge of the floor plan, and we're trying to get to EY128. We'd proceed with a sequential search algorithm. Lets order the rooms into an array of size 20, from EY100-EY138. Looking at the sign, we choose to start at EY100, as we're told rooms EY100-EY130 are to our left. Thus begins the sequential search, checking every room number we pass, comparing their values to EY128 each time. When EY128 is found, the sequential search is done, and we enter the room, completing the algorithmic search.

2.  Assuming we start at EY100, it would take 15 steps to find room EY128. A step in this instance is us performing a comparison of the current room to the room that we're trying to find. 

3.  Once again, given the fact that we have no knowledge of the floor plan, this is neither a best or worst case scenario, as we have no frame of reference of however many rooms there may be.

4.  With this particular floor sign/layout, assuming a sequential search as before, a best case scenario would involve going to the right, starting from EY138 and going to every room before that. It would take 6 steps as before. The position of EY128 will never change, and assuming a sequential search will be done, the worst case scenario would in fact be our original idea. Turning left at the sign and starting at EY100, taking 15 steps to get to EY128.

5.  A few weeks in the term, we can recognize that both signs lead to the same loop; and that there are only 20 rooms, ordered in a linear fashion [EY100, EY102..., EY136, EY138]. Thus, we can instead perform an interval search (specifically a binary one). By starting at a room in the middle of EY100-138, we can make a comparison by checking whether or not the room we chose is greater than, less than, or matches EY128. If it isn't the latter, we're then only concerned with one half of the rooms left. Following the logic of a binary search, we can reach EY128 in 5 steps.
>[100, 102, 104, 106, 108, 110, 112, 114, 116, **118, 120**, 122, 124, 126, 128, 130, 132, 134, 136, 138]
>[120, 122, 124, 126, **128, 130**, 132, 134, 136, 138]
>[120, 122, **124**, 126, 128]
>[**126, 128**]
>[**128**]
    While it is technically slightly more efficient than a sequential search starting at the right of the sign, in reality we'd probably memorize where the room is located, with no need for algorithmic assistance.
