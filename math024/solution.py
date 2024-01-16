"""
Lexicographic Permutations
"""


def answer():
    """permutation"""
    p = "0123456789"
    q = 1000000
    return solver(p, q)


def factorials(n):
    """Calculate"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def solver(p, q):
    """lexicographic"""
    q = q - 1
    combinations = []
    firtst_value = list(p)

    for i in reversed(range(len(p))):
        index = q // factorials(i)
        q %= factorials(i)
        combinations.append(firtst_value.pop(index))

    return "".join(combinations)


if __name__ == "__main__":
    print(answer())
    print(solver("123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10000000000000))


#     print(solver('123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', 10000000000000))
