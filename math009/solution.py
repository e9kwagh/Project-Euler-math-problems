def answer():
    for i in range(1, 1000):
        for j in range(i, 1000):
            k = 1000 - i - j
            if i**2 + j**2 == k**2:
                x = i * j * k
                return x


def solver(p: int = 1, q: int = 1000):
    """Finds Pythagorean triplets whose sum lies between p and q."""
    if q < p:
        p, q = q, p

    final = {}

    for a in range(p, q):
        for b in range(a, q - a):
            c = int((a**2 + b**2) ** 0.5)
            total = tuple([a, b, c])
            if a < b < c and p <= sum(total) <= q:
                if sum(total) not in final:
                    final[sum(total)] = [total]
                else:
                    final[sum(total)].append(total)

    length = len(final.keys())
    return length


if __name__ == "__main__":
    print(solver(12))
    print("Answer of math009 =", answer())
