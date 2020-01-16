'''Problem 2: Search in a Rotated Sorted Array
'''


def find_pivot(l: list, start:int = 0) -> int:
    # Find the location of the pivot element in a 
    # pivoted array via binary search

    # If array is a single element, return address
    if len(l) <= 1:
        return start

    # Find mid-point
    mid = len(l) // 2

    # If mid-point is pivot return
    if l[mid] < l[mid-1]:
        return start+mid
    # Else continue to look for the pivot
    elif l[0] > l[mid-1]:
        return find_pivot(l[0:mid], start)
    else:
        return find_pivot(l[mid:], start+mid)

def binary_search(l: list, value: int, start: int = 0) -> int:
    # Vanilla binary search in a sorted list
    if len(l) == 1:
        if l[0] == value:
            return start
        else:
            return -1

    mid = len(l) // 2

    if l[mid] == value:
        return start+mid
    elif l[mid] > value:
        return binary_search(l[0:mid], value, start)
    else:
        return binary_search(l[mid:], value, start+mid)

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
    pivot = find_pivot(input_list)

    # Un-pivot the list and use binary search
    l = input_list[pivot:] + input_list[:pivot]
    pos = binary_search(l, value)

    # Return value in original array
    if pos == -1:
        return pos
    else:
        return (pos + pivot) % len(l)


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

    # Should print -1
    print(rotated_array_search(test_list2, 4.5))
