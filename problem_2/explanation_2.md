# Problem 2: Search in a Rotated Sorted Array

In order to search through a pivoted array in log(n) time, I first used binary search to find the pivoted value. Because the array is otherwise sorted, this boils down to finding the only un-sorted point, where the value one array location to the left is greater. Once the pivot is found, the array can be un-pivoted. Array access operations are done in constant time so this step should be as well. Once the array is un-pivoted, simple binary search can be performed to find the value.

Finding the pivot and the final value are done in O(log n) time, this the overall solution is O(log n). The call stack for each function is O(log n), while storing the array in memory takes O(n) space, so the space complexity is O(n).