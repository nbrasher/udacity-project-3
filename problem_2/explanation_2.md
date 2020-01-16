# Problem 2: Search in a Rotated Sorted Array

In order to search through a pivoted array in log(n) time, I first used binary search to find the pivoted value. Because the array is otherwise sorted, this boils down to finding the only un-sorted point, where the value one array location to the left is greater. Once the pivot is found, basic binary search can be followed to find the point using rotated array indices (rotated_index = (index + pivot_location) % array length). Because both of these operations involve only array access (a constant time operation) and two instances of binary search, the overall time complexity is still only O(log n).

The call stack for each function has O(log n) steps, while storing the array in memory takes O(n) space, so the space complexity is O(n).