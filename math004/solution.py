"""Write a function that returns the largest palindrome 
from the product of two n-digit numbers where both numbers are inside a range."""


def answer():
    return solver(3)  # this must be 999


def is_palindrome(n):
    """this fucntions returns palandrom"""
    return str(n) == str(n)[::-1]


def solver(n, p=None, q=None):
    """This function returns the largest palindrome"""
    if p is None:
        p = 10 ** (n - 1)
    if q is None:
        q = 10**n - 1

    greater = 0
    for i in reversed(range(p, q + 1)):  # Included q in the range
        for num in reversed(range(p, i + 1)):  # Included i in the range
            product = i * num
            if product <= greater:
                break
            if is_palindrome(product):
                greater = product

    return greater


if __name__ == "__main__":
    print(solver(3))
    print("answer of math004 = ", answer())
