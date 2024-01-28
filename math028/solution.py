"""math028"""


def answer():
    """anwser()"""
    return solver(1001)


def solver(n):
    """Solver()"""
    if n == 0:
        return 0

    i, add, total = 1, 0, 0

    if n % 2 != 0:
        i, add, total = 2, 1, 1

    while i < n:
        for _ in range(4):
            add += i
            total += add
        i += 2

    return total


if __name__ == "__main__":
    print(answer())
    print(solver(1001))
# 669171001
