"""new reciprocal"""


def reciprocal_length(den):
    """func()"""
    rem_seen = {}
    rem = 1
    position = 0

    while rem != 0 and rem not in rem_seen:
        rem_seen[rem] = position
        rem = (rem * 10) % den
        position += 1

    if rem == 0:
        return 0
    return position - rem_seen[rem]


def answer():
    """answer()"""
    return solver(1000, [1, 4, 2, 8, 5, 7])


def solver(limit, digits=None):
    """solver."""
    longest_cycle = 0
    result = 0

    for den in range(2, limit):
        treverse_len = reciprocal_length(den)

        if treverse_len > longest_cycle and all(str(digit) in str(1 / den) for digit in digits):
            longest_cycle = treverse_len
            result = den

    return result



if __name__ == "__main__":
    print("answer of math026 = ", answer())
    print(solver(1000, [1, 4, 2, 8, 5, 7]))
