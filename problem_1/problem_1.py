'''
Problem 1: Square Root of an Integer
'''

def initial_guess(n: int):
    n_digits = len(str(n))

    # For results with even number of zeros (i.e. 10,0000) guess 10^(half as many digits)
    # For results with an odd number, guess 6 * 10 ^(half as many digits - 1)
    if (n_digits-1) % 2 == 0:
        return 10**((n_digits-1) // 2)
    else:
        return 6 * 10**((n_digits-1) // 2)

def sqrt(n: int, guess: int = None):
    """
    Calculate the floored square root of a number

    Args:
       n(int): Number to find the floored squared root
       guess(int): Optional integer guess for the square root
    Returns:
       int: Floored Square Root
    """
    assert isinstance(n, int), 'Must be an integer'
    assert n > 0, 'Must be a positive integer'
    
    # If no guess is supplied, get guess from initial_guess algorithm
    if not guess:
        guess = initial_guess(n)
    else:
        assert isinstance(guess, int) & (guess > 0)
    
    # Check if the guess is the answer, if not use the Babylonian method
    # to update the new guess and iterate
    if (guess ** 2 <= n) & ((guess+1)**2 > n):
        return guess
    else:
        return sqrt(n, (guess + n // guess)//2)


if __name__ == '__main__':

    # Test proper guess behavior
    assert initial_guess(10000) == 100
    assert initial_guess(1000) == 60


    # Should return 3
    print(sqrt(9))

    # Should return 1
    print(sqrt(1))

    # Should return 600
    print(sqrt(360000))

    # Should return 12
    print(sqrt(144))

    # Should raise an error
    print(sqrt(-1))