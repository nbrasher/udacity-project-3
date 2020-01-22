'''Problem 2: Search in a Rotated Sorted Array
'''


def find_pivot(l: list) -> int:
    # Find the location of the pivot element in a 
    # pivoted array via binary search
    start = 0
    end = len(l) - 1

    # Find mid-point
    while start <= end:
        mid = (start + end) // 2
        
        # The pivot is the one element that is unsorted
        if l[mid] < l[mid-1]:
            return mid
        elif l[start] > l[mid]:
            end = mid
        else:    
            start = mid


def binary_search(l: list, value: int, pivot: int = 0) -> int:
    # Binary search in a sorted list using index values
    # rotated by a pivot value (if supplied)
    n = len(l)

    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        
        # Rotate indices if a pivot is supplied
        if l[(mid + pivot) % n] == value:
            return (mid + pivot) % n
        elif l[(mid + pivot) % n] > value:
            end = mid-1
        else:    
            start = mid+1
    
    return -1

def rotated_array_search(
    input_list: list, 
    value: int) -> int:
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Test that list elements are integers
    assert input_list, 'Must pass a non-empty array of integers'
    assert all(isinstance(i, int) for i in input_list), 'Must pass an array of integers'

    # Test if the array is sorted
    if input_list[-1] > input_list[0]:
        pivot = 0
    # If not, find pivot point
    else:
        pivot = find_pivot(input_list)

    # Use binary search using rotated array indices
    return binary_search(input_list, value, pivot)


if __name__ == '__main__':
    test_list1 = [4, 5, 6, 7, 0, 1, 2]
    test_list2 = [6, 7, 8, 9, 10, 1, 2, 3, 4]

    # Test proper find_pivot behavior
    assert find_pivot(test_list1) == 4
    assert find_pivot(test_list2) == 5

    # Test proper binary search behavior
    assert binary_search([0, 1, 3, 4, 5], 4) == 3
    assert binary_search([0, 1, 3, 4, 5], 0) == 0

    # Should print 2
    print(rotated_array_search(test_list1, 6))

    # Should print 5
    print(rotated_array_search(test_list1, 1))

    # Should print 6
    print(rotated_array_search(test_list1, 2))

     # Should print 0
    print(rotated_array_search(test_list2, 6))

    # Should print -1
    print(rotated_array_search(test_list2, 5))

    # Sorted and non-rotated array, should print 0
    print(rotated_array_search([1, 2, 3, 4, 5], 1))

    # Empty list, should raise an error
    print(rotated_array_search([], 1))
