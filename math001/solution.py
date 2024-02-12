def answer():
    """fucntion"""
    li = []
    for i in range(1000):
        if i % 3 == 0:
            li.append(i)
        elif i % 5 == 0:
            if i not in li:
                li.append(i)

    add = sum(li)
    return add


def solver(factors=[4, 7, 11], start=8912, end=40512):
    """This is the solver funtions"""
    li = []
    for i in factors:
        for j in range(start, end + 1):
            if j % i == 0:
                if j not in li:
                    li.append(j)
    add = sum(li)
    return add


if __name__ == "__main__":
    print(solver([4, 7, 11], 8912, 40512))
    print("answer of math001 = ", answer())
