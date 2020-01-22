'''
Problem 4: Dutch National Flag Problem
'''

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # Test that list elements are 0, 1 or 2
    assert input_list, 'Must pass a non-empty array of 0, 1 or 2'
    assert all(isinstance(i, int) for i in input_list), 'Must pass an array of 0, 1 or 2'
    assert all(i<3 and i >= 0 for i in input_list), 'Must pass an array of 0, 1 or 2'

    # Empty lists to catch sorted elements
    zeros = []
    ones = []
    twos = []
    for i in input_list:
        if i == 2:
            twos.append(i)
        elif i == 1:
            ones.append(i)
        else:
            zeros.append(i)
    
    # Combine into a single list
    zeros.extend(ones)
    zeros.extend(twos)
    return zeros


if __name__ == '__main__':
    test_list_1 = [1, 0, 2, 0]
    test_list_2 = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
    test_list_3 = [0, 0, 0]

    # Should return [0, 0, 1, 2]
    print(sort_012(test_list_1))

    # Should return [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
    print(sort_012(test_list_2))

    # Should return [0, 0, 0]
    print(sort_012(test_list_3))

    # Single digit, should return [1]
    print(sort_012([1]))

    # Empty list, Should raise an error
    print(sort_012([]))