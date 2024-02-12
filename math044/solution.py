"""math044"""

def is_pentagonal(num):
    """penta"""
    n = int((1 + (1 + 24 * num) ** 0.5) / 6)
    return n * (3 * n - 1) // 2 == num

def answer():
    """answer()"""
    pentagon_numbers = [n * (3 * n - 1) // 2 for n in range(1, 3000)]

    for j, pj in enumerate(pentagon_numbers):
        for k in range(j - 1, -1, -1):
            pk = pentagon_numbers[k]
            if is_pentagonal(pj + pk) and is_pentagonal(pj - pk):
                return abs(pj - pk)

    return 0

if __name__ == "__main__":
    print("Problem no : math044")
    print("answer= :", answer())
