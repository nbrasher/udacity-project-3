'''
Problem 3: Rearrange Array Elements
'''
def reverse_merge(left: list, right: list) -> list:
    #Merge sorted arrays for merge sort in reverse order

    merged = []
    right_ix = 0
    left_ix = 0

    while left_ix < len(left) and right_ix < len(right):
        if left[left_ix] > right[right_ix]:
            merged.append(left[left_ix])
            left_ix += 1
        else:
            merged.append(right[right_ix])
            right_ix += 1

    merged += left[left_ix:]
    merged += right[right_ix:]

    return merged

def merge_sort(l: list) -> list:
    ''' Basic merge sort, in reverse order

    Args:
       l(list): Unsorted array
    Returns:
       l(list): Sorted array
    '''
    if len(l) <= 1:
        return l

    # Find mid-point and split array
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])

    # Return merged and sorted array
    return reverse_merge(left, right)

def rearrange_digits(input_list: list) -> tuple:
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       list: Two maximum sums
    """
    # Test that list elements are digits
    assert all(isinstance(i, int) for i in input_list), 'Must pass an array of digits'
    assert all(i<10 and i >= 0 for i in input_list), 'Must pass an array of digits'

    # Empty lists to hold final digits
    out1 = []
    out2 = []
    
    # First sort the list
    l = merge_sort(input_list)

    # Build two integers one at a time, starting with the largest digits
    for i, el in enumerate(l):
        if i % 2 == 0:
            out1.append(el)
        else:
            out2.append(el)

    # Convert lists of digits into integers
    out1 = int(''.join([str(i) for i in out1]))
    out2 = int(''.join([str(i) for i in out2]))

    return out1, out2


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5]

    # Test proper merge behavior
    assert reverse_merge([1], [2]) == [2, 1]
    assert reverse_merge([3, 1], [4, 2]) == [4, 3, 2, 1]

    # Test proper sort behavior
    assert merge_sort(test_list) == [5, 4, 3, 2, 1]

    # Should print 531, 42
    print(rearrange_digits([1, 2, 3, 4, 5]))

    # Should print 964, 852
    print(rearrange_digits([4, 6, 2, 5, 9, 8]))

    # Should print 1000, 100
    print(rearrange_digits([0, 0, 1, 1, 0, 0, 0]))

    # Should return 0, 0
    print(rearrange_digits([0, 0, 0, 0, 0, 0, 0]))

    # Should raise an error
    print(rearrange_digits(['a', 'b']))