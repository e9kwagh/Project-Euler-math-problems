"""math064
"""


def formula(n):
    """formula
    """
    m, deno, a = 0, 1, int(n**0.5)
    i_a = a
    length = 0

    while a != 2 * i_a:
        m = deno * a - m
        deno = (n - m**2) // deno
        a = (i_a + m) // deno
        length += 1

    return length


def answer():
    """answer()
    """
    limit = 10000
    odd_count = 0
    for num in range(2, limit + 1):
        sqr = int(num**0.5)
        if sqr**2 == num:
            continue
        if formula(num) % 2 == 1:
            odd_count += 1
    return odd_count


if __name__ == "__main__":
    print("Answer of math064 =", answer())
