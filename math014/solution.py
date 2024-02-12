"""This is the solver"""


def answer():
    """This is the answer()"""
    return solver(2, 1000000)


def solver(p: int = None, q: int = None):
    """solver()"""
    if p is None and q is None:
        return None
    if p is None:
        p = 2
    if q is None:
        q, p = p, 2
    if p > q:
        q, p = p, q

    hash_map = {}
    add = 0
    for i in range(p, q + 1):
        li = [i]
        num = i
        while num > 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1

            if num in hash_map:
                li = li + hash_map[num]
                break
            li.append(num)

        if len(li) > add:
            add = len(li)
            large = i
        hash_map[i] = li
    return large


if __name__ == "__main__":
    print(solver(1000000, 2))
    print("answer of math014 = ", answer())
