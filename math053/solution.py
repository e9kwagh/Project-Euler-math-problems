"""math053"""


def factorial(num):
    """factorial"""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def answer():
    """answer()"""
    count = 0
    limit = 1000000
    for n in range(1, 101):
        for r in range(1, n + 1):
            combination = factorial(n) // (factorial(r) * factorial(n - r))
            if combination > limit:
                count += 1

    return count


if __name__ == "__main__":
    print("Answer of math053 =", answer())
