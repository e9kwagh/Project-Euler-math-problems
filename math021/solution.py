"""
Amicable Numbers
"""


def answer():
    """answer()"""
    return solver(1, 10000)


def roots(num):
    """roots"""
    return sum(i for i in range(1, num) if num % i == 0)


def solver(p: int, q: int):
    """solver"""
    if q is None:
        p.q = 1, p
    if p is None:
        p = 1

    amicable = {}
    list_amicable = []
    for val in range(p, q + 1):
        factors = roots(val)

        if factors in amicable and val == amicable[factors]:
            list_amicable.append(val)
            list_amicable.append(factors)
        else:
            amicable[val] = factors

    ans = sum(list_amicable)
    return ans


if __name__ == "__main__":
    print(solver(1, 10000))
    print("answer of math021 = ", answer())
    # 31626
