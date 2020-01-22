# Problem 4: Dutch National Flag Problem

This problem is simply a task for putting elements into buckets. Because we only have three elements, we know that twos go on the right end, zeros on the left and ones in the middle. First I group elements into their respeoctive bins in one traversal - this is an O(n) operation. Next, I link each list to create a sorted list of 0s 1s and 2s. Python stats that extending a list is an O(k) operation. Because the total of all these lists is together length n, this is also an O(n) operation. Thus the entire algorithm is O(n) in time complexity. 

The algorithm involves storing the entire array in memory and is thus also O(n) for space complexity.