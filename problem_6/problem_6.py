'''Problem 6: Unsorted Integer Array
'''

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    assert ints, 'Must pass a non-empty array of integers'
    assert all(isinstance(i, int) for i in ints), 'Must pass an array of integers'
    
    # Set the initial min and max to the first element
    min = ints[0]
    max = ints[0]

    # Iterate over rest of list to see if larger or smaller elements exist
    for i in ints[1:]:
        if min > i:
            min = i
        if max < i:
            max = i

    return min, max


if __name__ == '__main__':
    test_list_1 = [1, 4, 6, 3, 0, 5, 2]
    test_list_2 = [1, 4, 6, 3, 0, -2, 42]
    test_list_3 = [0, 0, 0, 0, 0, 0, 0]

    # Should print 0, 6
    print(get_min_max(test_list_1))

    # Should print -2, 42
    print(get_min_max(test_list_2))

    # Should print 0, 0
    print(get_min_max(test_list_3))

    # Single digit, should print 1,1
    print(get_min_max([1]))

    # Should raise an error
    print(get_min_max([]))
