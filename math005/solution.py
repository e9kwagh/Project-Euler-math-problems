"""Write a function in python that returns the smallest positive number 
that is evenly divisible by all of the numbers between the range p and q, inclusive.
"""


def gcd(a, b):
    """gcd"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """lcm"""
    return a * b // gcd(a, b)


def answer():
    """answer"""
    return solver(1, 20)


def solver(p=1, q=10):
    """solver"""
    if p > q:
        start, end = q, p
    else:
        start, end = p, q

    current_lcm = 1

    for i in range(start, end + 1):
        current_lcm = lcm(current_lcm, i)

    return current_lcm


if __name__ == "__main__":
    print(solver(1, 10))
    print("answer of math005 = ", answer())
