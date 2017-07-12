import sys


def sqrt(x):
    """Compute sqrt using Method of Heron of Alexandria

    Args:
        x: the number to which the sqrt is to be computed

    Returns:
        the sqrt of x
    Raises:
        ValueError if x is negative
    """

    if x < 0:
        raise ValueError("Cannot compute square root of negative number. Given Input: {}".format(x))

    guess = x
    i = 0

    while guess * guess != x and i < 20:
        guess = (guess + x / guess)/2.
        i += 1
    return guess


def main():
    try:
        print(sqrt(-1))
        print(sqrt(9))
        print(sqrt(2))
        print("in try statement")

    except ValueError as e:
        # pass
        print(e, file=sys.stderr)
        # print("Cannot compute square root of a negative number")
        # raise ValueError()

    print("here")
if __name__ == "__main__":
    main()

