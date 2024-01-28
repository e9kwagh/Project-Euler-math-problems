"""new reciprocal"""
def reciprocal_length(den):
    """func()"""
    rem_seen ={}
    rem= 1
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
    for den in range(2, limit):
        treverse_len = reciprocal_length(den)

        if all(str(digit) in str(1 / den) for digit in digits) and treverse_len > 0:
            return den

    return 0


if __name__ == "__main__":
    print(answer())
    print(solver(1000, [1, 4, 2, 8, 5, 7]))
