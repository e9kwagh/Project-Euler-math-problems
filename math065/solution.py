"""
math065
"""

def formula(n):
    """
    formula
    """
    a, b = 2, 1
    for k in range(1, n):
        if k % 3 == 2:
            value = 2 * (k // 3 + 1)
        else:
            value = 1
        a, b = value * a + b, a
    return a


def sum_of_digits(num):
    """sum"""
    return sum(int(digit) for digit in str(num))


def answer():
    """
    answer()
    """
    result = formula(100)
    return sum_of_digits(result)


if __name__ == "__main__":
    print("Answer of math065 =", answer())
