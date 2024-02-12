"""math040"""

import math


def digits(n):
    """digit"""
    number = "".join(str(i) for i in range(1, 1000000))
    return int(number[n - 1])


def answer():
    """ans"""
    find_value = [1, 10, 100, 1000, 10000, 100000, 1000000]
    product = math.prod(digits(digit) for digit in find_value)

    return product


if __name__ == "__main__":
    print("Question no : Math040")
    print("Answer of math040 = ", answer())
