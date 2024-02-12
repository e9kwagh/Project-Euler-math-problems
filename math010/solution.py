"""prime  solver"""


def answer():
    """answer()"""
    return solver(2000000)


def solver(p: int, q: int = None):
    """solver"""
    if p is None and q is None:
        return None
    if p is None:
        p, q = 2, p
    if q is None:
        q, p = p, 2
    total = 0
    for i in range(p, q + 1):
        square = int(i**0.5)
        flag = True
        for sqr in range(2, square + 1):
            if i % sqr == 0:
                flag = False
                break
        if flag:
            total += i

    return total


if __name__ == "__main__":
    print(solver(40, 2000000))
    print("answer of math010 = ", answer())
