"""math29"""


def multiply_carry(num, multiplier, carry):
    """Multiply"""
    result = 0

    while num or carry:
        product = (num % 10) * multiplier + carry
        result = result * 10 + product % 10
        carry = product // 10
        num //= 10

    return result


def powerf(num, power):
    """power"""
    result = 1
    for _ in range(power):
        result = multiply_carry(result, num, 0)

    return result


def solver(n):
    """solver"""
    distinct_terms = [powerf(a, b) for a in range(2, n + 1) for b in range(2, n + 1)]

    return len(set(distinct_terms))


def answer():
    """answer()"""
    return solver(100)


if __name__ == "__main__":
    print("Math029")
    print("solver(5) =", solver(5))
    print("answer() =", answer())


# def solver(n):
#     distinct_terms = {a ** b for a in range(2, n + 1) for b in range(2, n + 1)}
#     return len(distinct_terms)
